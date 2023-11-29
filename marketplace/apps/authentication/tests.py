from django.test import TestCase
from marketplace.apps.authentication.models import Customer

# Create your tests here.


# TODO: Create tests for the Customer endpoint
class CustomerTestCase(TestCase):
    def setUp(self):
        data = {
            'username': 'test',
            'email': 'teste@example.com',
            'password': '12345678',
        }
        Customer.objects.create_user(data)

    def test_create_customer(self):
        customer = Customer.objects.get(username='test')
        self.assertEqual(customer.username, 'test')
        self.assertEqual(customer.email, 'teste@example.com')
        self.assertTrue(customer.check_password())
