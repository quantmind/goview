import os
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
