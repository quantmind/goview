from flask import Blueprint, jsonify, abort, request

from flask_cors import CORS

from marshmallow_sqlalchemy import ModelSchema

from .models import db, Task
from .paginate import Pagination
from .config import VERSION


api = Blueprint('api', __name__)

CORS(api)


class TodoSchema(ModelSchema):

    class Meta:
        model = Task


todo_schema = TodoSchema()
edit_schema = TodoSchema(exclude=('id',))


@api.route('/')
def info():
    return jsonify({'version': VERSION})


@api.route('/todos', methods=['GET', 'HEAD', 'POST'])
def todos():
    if request.method == 'POST':
        todo, errors = edit_schema.load(request.get_json(), session=db.session)
        if errors:
            abort(419)
        db.session.add(todo)
        db.session.commit()
        return jsonify(todo_schema.dump(todo).data), 201
    else:
        pag = Pagination(db.session.query(TodoSchema.Meta.model))
        return pag.response(todo_schema)


@api.route('/todos/<id>', methods=['GET', 'HEAD', 'PATCH', 'DELETE'])
def todo(id):
    todo = db.session.query(TodoSchema.Meta.model).get(id)
    if not todo:
        abort(404)
    if request.method == 'PATCH':
        todo, errors = edit_schema.load(request.get_json(), instance=todo)
        if errors:
            abort(419)
        db.session.add(todo)
        db.session.commit()
    elif request.method == 'DELETE':
        db.session.delete(todo)
        db.session.commit()
        return '', 204
    return jsonify(todo_schema.dump(todo).data)
