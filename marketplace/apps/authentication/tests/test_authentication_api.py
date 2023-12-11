from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import VerifyJSONWebToken


class AuthenticationAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_login(self):
        response = self.client.post('auth/login/', {'username': 'admin', 'password': 'admin123'})
        self.assertEqual(response.status_code, 200)


