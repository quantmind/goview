import json

from . import GoTestCase


class TestApp(GoTestCase):

    def test_meta(self):
        client = self.app.test_client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_meta(self):
        client = self.app.test_client()
        response = client.get('/foo')
        self.assertEqual(response.status_code, 404)
