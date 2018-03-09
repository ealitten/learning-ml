from django.test import TestCase, Client
from django.urls import reverse

class IndexTest(TestCase):

    client = Client()

    @classmethod
    def test_index_view(self):
        resp = self.client.get('/battle/')

        self.assertEqual(resp.status_code, 200)
        self.assertIn("Hello, world. You're at the battles index.", resp.content)
