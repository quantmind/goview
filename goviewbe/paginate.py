from collections import OrderedDict
from urllib.parse import urlencode

from flask import request, jsonify

from werkzeug.urls import url_parse

from marshmallow import Schema, fields


def make_url(url, params):
    if isinstance(params, dict):
        params = tuple(params.items())
    url = url_parse(url)
    query = urlencode(params)
    return str(url.replace(query=query))


class QuerySchema(Schema):
    limit = fields.Integer(
        default=50,
        description='Maximum number of items in response'
        )
    offset = fields.Integer(
        default=0,
        description='Items offset'
    )


class Pagination:
    query_schema = QuerySchema()

    def __init__(self, query, query_schema=None, **params):
        self.query_schema = query_schema or self.query_schema
        params.update(request.args.items())
        self.args = self.query_schema.load(params).data
        self.limit = max(self.args.pop('limit', 50), 0)
        self.offset = max(self.args.pop('offset', 0), 0)
        self.total = query.count()
        self.query = query.limit(self.limit).offset(self.offset)

    def first_link(self):
        offset = self.offset
        n = self._count_part(offset, self.limit, 0)
        if n:
            offset -= n*self.limit
        if offset > 0:
            return self.link(0, min(self.limit, offset))

    def prev_link(self):
        if self.offset:
            olimit = min(self.limit, self.offset)
            prev_offset = self.offset - olimit
            return self.link(prev_offset, olimit)

    def next_link(self):
        next_offset = self.offset + self.limit
        if self.total > next_offset:
            return self.link(next_offset, self.limit)

    def last_link(self):
        n = self._count_part(self.total, self.limit, self.offset)
        if n > 0:
            return self.link(self.offset + n*self.limit, self.limit)

    def link(self, offset, limit):
        args = request.args.copy()
        args['limit'] = limit
        args['offset'] = offset
        return make_url(request.url, tuple(args.items(True)))

    def response(self, schema):
        links = OrderedDict()
        first = self.first_link()
        if first:
            links['first'] = first
            prev = self.prev_link()
            if prev != first:
                links['prev'] = prev
        next = self.next_link()
        if next:
            last = self.last_link()
            if last != next:
                links['next'] = next
            links['last'] = last
        data = schema.dump(self.query, many=True).data
        response = jsonify(data)
        if links:
            response.headers['Link'] = ', '.join(
                ('<%s>; rel="%s"' % (v, k) for k, v in links.items())
            )
        return response

    def _count_part(self, total, limit, offset):
        n = (total - offset) // limit
        # make sure we account for perfect matching
        if n*limit + offset == total:
            n -= 1
        return max(0, n)
