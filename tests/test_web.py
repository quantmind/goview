from . import GoTestCase


class TestApp(GoTestCase):

    def test_200(self):
        client = self.app.test_client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        client = self.app.test_client()
        response = client.get('/foo')
        self.assertEqual(response.status_code, 404)

    def test_ui_template(self):
        client = self.app.test_client()
        response = client.get('/template/todo')
        self.assertEqual(response.status_code, 200)
