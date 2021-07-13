from django.http import response
from django.test import TestCase, SimpleTestCase

# Create your tests here.


class SimpleTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_index_page_status_code(self):
        response = self.client.get("/index/")
        self.assertEqual(response.status_code, 200)
