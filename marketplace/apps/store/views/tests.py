from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from marketplace.apps.store.models import Cart, CartItem, Product
from marketplace.apps.store.serializers import CartSerializer

User = get_user_model()


class CartViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.cart = Cart.objects.create(owner=self.user)

    def test_retrieve_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, CartSerializer(instance=self.cart).data)

    def test_update_cart(self):
        updated_data = {'owner': self.user.id}  # You may modify this data as needed
        response = self.client.patch('/cart/', data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cart.refresh_from_db()
        self.assertEqual(self.cart.owner, self.user)


class CartItemViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.cart = Cart.objects.create(owner=self.user)
        self.product = Product.objects.create(
            name='Test Product', price=19.99, description='A test product')

    def test_create_cart_item(self):
        data = {'item': self.product.id, 'quantity': 2, 'cart': self.cart.id}
        response = self.client.post('/cart/items/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['item'], str(self.product.id))
        self.assertEqual(response.data['quantity'], 2)
        self.assertEqual(response.data['cart'], str(self.cart.id))

    def test_list_cart_items(self):
        CartItem.objects.create(item=self.product, quantity=2, cart=self.cart)
        response = self.client.get('/cart/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_cart_item(self):
        cart_item = CartItem.objects.create(item=self.product, quantity=2, cart=self.cart)
        response = self.client.delete(f'/cart/items/{cart_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(CartItem.DoesNotExist):
            cart_item.refresh_from_db()


class ProductViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(
            name='Test Product', price=19.99, description='A test product')

    def test_list_products(self):
        response = self.client.get('store/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_product(self):
        data = {'name': 'New Product', 'price': 25.99, 'description': 'A new product'}
        response = self.client.post('/store/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'New Product')
        self.assertEqual(response.data['price'], '25.99')
        self.assertEqual(response.data['description'], 'A new product')

    def test_retrieve_product(self):
        response = self.client.get(f'/store/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(self.product.id))
        self.assertEqual(response.data['name'], 'Test Product')
