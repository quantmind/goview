from . import GoTestCase


class TestApp(GoTestCase):

    def test_meta(self):
        app = self.app
        self.assertTrue(app)
        self.assertTrue(app.config['TESTING'])
