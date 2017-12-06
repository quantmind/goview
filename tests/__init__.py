import os
import json
import unittest

import goviewbe


TEST_DB = os.path.join(os.path.dirname(__file__), 'data-test.sqlite')


class GoTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = goviewbe.create_app(
            'test',
            SQLALCHEMY_DATABASE_URI='sqlite:///%s' % TEST_DB,
            TESTING=True,
            SERVER_NAME='test.com'
        )
        goviewbe.upgrade_db(cls.app)
        cls.client = cls.app.test_client()
        cls.load_fixtures()

    @classmethod
    def tearDownClass(cls):
        # delete test database after test
        try:
            os.unlink(TEST_DB)
        except OSError:
            pass

    @classmethod
    def load_fixtures(cls):
        pass

    def json(self, response, status_code=None):
        """Get JSON object from response
        """
        if status_code:
            self.assertEqual(response.status_code, status_code)
        self.assertEqual(response.headers['Content-Type'],
                         'application/json')
        return json.loads(response.data.decode())

    def patch(self, url, **kwargs):
        client = self.app.test_client()
        return client.patch(url, **self.json_request(kwargs))

    def post(self, url, **kwargs):
        client = self.app.test_client()
        return client.post(url, **self.json_request(kwargs))

    def json_request(self, data):
        return dict(
            data=json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )
