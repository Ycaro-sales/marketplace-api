from django.test import TestCase
from marketplace.apps.authentication.models import Customer
from marketplace.apps.store.models import Cart, CartItem, Product
from django.core.exceptions import ValidationError


class CartModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(username="test_user")
        self.cart = Cart.objects.create(owner=self.customer)

    def test_cart_creation(self):
        self.assertIsInstance(self.cart, Cart)
        self.assertIsNotNone(self.cart.id)
        self.assertEqual(self.cart.owner, self.customer)
        self.assertIsNotNone(self.cart.created_at)

    def test_cart_str_representation(self):
        self.assertEqual(str(self.cart), str(self.cart.id))


class CartItemModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(username="test_user")
        self.cart = Cart.objects.create(owner=self.customer)
        self.product = Product.objects.create(
            name="Test Product",
            price=19.99,
            description="A test product for CartItem",
        )
        self.cart_item = CartItem.objects.create(
            item=self.product, quantity=2, cart=self.cart
        )

    def test_cart_item_creation(self):
        self.assertIsInstance(self.cart_item, CartItem)
        self.assertEqual(self.cart_item.item, self.product)
        self.assertEqual(self.cart_item.quantity, 2)
        self.assertEqual(self.cart_item.cart, self.cart)

    def test_cart_item_default_quantity(self):
        default_cart_item = CartItem.objects.create(item=self.product, cart=self.cart)
        self.assertEqual(default_cart_item.quantity, 1)

    def test_cart_item_deletion(self):
        cart_item_id = self.cart_item.id
        self.cart_item.delete()
        with self.assertRaises(CartItem.DoesNotExist):
            CartItem.objects.get(id=cart_item_id)

    pass


class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(
            name="Test Product",
            price=19.99,
            description="A test product for testing",
        )
        self.assertIsInstance(product, Product)
        self.assertIsNotNone(product.id)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 19.99)
        self.assertEqual(product.description, "A test product for testing")
        self.assertIsNotNone(product.created_at)


class CartModelInvalidationTest(TestCase):
    def test_cart_creation_invalid_owner(self):
        with self.assertRaises(ValidationError):
            Cart.objects.create(owner=None)

    def test_cart_creation_invalid_created_at(self):
        with self.assertRaises(ValidationError):
            Cart.objects.create(owner=Customer.objects.create(), created_at="invalid_date")


class CartItemModelInvalidationTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(username="test_user")
        self.cart = Cart.objects.create(owner=self.customer)
        self.product = Product.objects.create(
            name="Test Product",
            price=19.99,
            description="A test product for CartItem",
        )

    def test_cart_item_creation_invalid_item(self):
        with self.assertRaises(ValidationError):
            CartItem.objects.create(item=None, quantity=2, cart=self.cart)

    def test_cart_item_creation_invalid_quantity(self):
        with self.assertRaises(ValidationError):
            CartItem.objects.create(item=self.product, quantity=-1, cart=self.cart)

    def test_cart_item_creation_invalid_cart(self):
        with self.assertRaises(ValidationError):
            CartItem.objects.create(item=self.product, quantity=2, cart=None)


class ProductModelInvalidationTest(TestCase):
    def test_product_creation_invalid_name(self):
        with self.assertRaises(ValidationError):
            Product.objects.create(
                name="", price=19.99, description="A test product for testing"
            )

    def test_product_creation_invalid_price(self):
        with self.assertRaises(ValidationError):
            Product.objects.create(
                name="Test Product", price="invalid_price", description="A test product for testing"
            )

    def test_product_creation_invalid_description(self):
        with self.assertRaises(ValidationError):
            Product.objects.create(
                name="Test Product", price=19.99, description=None
            )

