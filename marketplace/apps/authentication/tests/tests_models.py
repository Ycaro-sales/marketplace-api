from django.test import TestCase

from marketplace.apps.authentication.models import Customer
from marketplace.apps.store.models import Cart
<<<<<<< HEAD:marketplace/apps/authentication/tests/tests_models.py


# from rest_framework.test import APIClient, RequestsClient

# Create your tests here.
=======
>>>>>>> cda8398 (Created Tests):marketplace/apps/authentication/tests.py


class CustomerModelTestCase(TestCase):

    def setUp(self):
        data = {
            'username': 'test',
            'email': 'test@example.com',
            'password': '12345678',
        }
        Customer.objects.create_user(**data)

    def test_create_customer(self):
        customer = Customer.objects.get(username='test')
        print("Customer: ", customer)

        self.assertEqual(customer.username, 'test')
        self.assertEqual(customer.email, 'test@example.com')
        self.assertEqual(customer.is_active, True)
        self.assertEqual(customer.is_staff, False)
        self.assertEqual(Cart.objects.get(owner=customer).owner, customer)


class ManagerModelTestCase(TestCase):
    def setUp(self):
        data = {
            'username': 'admin',
            'email': 'admin@example.com',
            'password': '12345678',
        }
        Customer.objects.create_user(**data)

    def test_create_manager(self):
        manager = Customer.objects.get(username='admin')
        print("Manager: ", manager)

        self.assertEqual(manager.username, 'admin')
        self.assertEqual(manager.email, 'admin@example.com')
        self.assertEqual(manager.is_active, True)
        self.assertEqual(manager.is_staff, True)
        self.assertEqual(Cart.objects.get(owner=manager).DoesNotExist, True)


