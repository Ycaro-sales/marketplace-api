from rest_framework_simplejwt.tokens import RefreshToken
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()


class CustomerViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_customers(self):
        response = self.client.get('/customers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming there is only one customer

    def test_retrieve_customer(self):
        response = self.client.get(f'/customers/{self.user.customer.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(self.user.customer.id))
        self.assertEqual(response.data['user']['username'], 'test_user')

    def test_update_customer(self):
        updated_data = {'user': {'username': 'new_username'}}  # You may modify this data as needed
        response = self.client.patch(f'/customers/{self.user.customer.id}/', data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.customer.refresh_from_db()
        self.assertEqual(self.user.customer.user.username, 'new_username')


class SignUpViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_signup_customer(self):
        data = {'user': {'username': 'new_user', 'password': 'new_password'}}
        response = self.client.post('/signup/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('user' in response.data)
        self.assertTrue('token' in response.data)


class ManagerViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='manager_user', password='manager_password', is_staff=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_see_customers(self):
        response = self.client.get('/staff/customers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class loginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client = APIClient()

    def test_obtain_access_token(self):
        data = {'username': 'test_user', 'password': 'test_password'}
        response = self.client.post('auth/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)


class TokenRefreshViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        refresh = RefreshToken.for_user(self.user)
        self.refresh_token = str(refresh)
        self.client = APIClient()

    def test_refresh_access_token(self):
        data = {'refresh': self.refresh_token}
        response = self.client.post('/auth/token/refresh/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)


class TokenVerifyViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client = APIClient()

    def test_verify_access_token(self):
        data = {'token': self.access_token}
        response = self.client.post('/auth/token/verify/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token_type' in response.data)
        self.assertTrue('exp' in response.data)
