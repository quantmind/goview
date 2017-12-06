import json
from random import randint

from faker import Factory

from . import GoTestCase


fake = Factory.create()


class TestApp(GoTestCase):

    def test_meta(self):
        app = self.app
        self.assertTrue(app)
        self.assertTrue(app.config['TESTING'])

    def test_api_root(self):
        client = self.app.test_client()
        response = client.get('/api/')
        self.json(response, 200)
        response = client.post(
            '/api/', data=json.dumps(dict(doo=3))
        )
        self.assertEqual(response.status_code, 405)

    def test_todo_crud(self):
        client = self.app.test_client()
        #
        # create
        response = self.post('/api/todos', text='something to do')
        data = self.json(response, 201)
        self.assertEqual(data['text'], 'something to do')
        self.assertTrue(data['id'])
        #
        # read
        response = client.get('/api/todos/%s' % data['id'])
        data2 = self.json(response, 200)
        self.assertEqual(len(data), len(data2))
        self.assertEqual(data2['text'], 'something to do')
        #
        # update
        response = self.patch('/api/todos/%s' % data['id'],
                              text='maybe something to do')
        data3 = self.json(response, 200)
        self.assertEqual(len(data), len(data2))
        self.assertEqual(data3['text'], 'maybe something to do')
        #
        # delete
        response = client.delete('/api/todos/%s' % data['id'])
        self.assertEqual(response.status_code, 204)
        #
        response = client.get('/api/todos/%s' % data['id'])
        self.assertEqual(response.status_code, 404)

    def test_paginate(self):
        client = self.app.test_client()
        for _ in range(100):
            self.post('/api/todos', text=fake.text(randint(20, 50)))
        response = client.get('/api/todos')
        data = self.json(response, 200)
        self.assertEqual(len(data), 50)
        response = client.get('/api/todos?limit=20')
        data = self.json(response, 200)
        self.assertEqual(len(data), 20)
