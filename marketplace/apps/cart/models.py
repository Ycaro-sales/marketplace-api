from django.db import models
import uuid


class CartManager(models.Manager):
    def create(self, user):
        cart = Cart(
            owner=user
        )
        return cart

    def add_item(self, cart, item, quantity):
        cart_item = CartItem.objects.create(
            item=item, quantity=quantity, cart=cart)
        return cart_item

    def update_item(self, cart, item, quantity):
        cart_item = CartItem.objects.get(CartItem=item, cart=cart)
        cart_item.quantity = quantity
        cart_item.save()

    def remove_item(self, cart, item):
        cart_item = CartItem.objects.get(CartItem=item, cart=cart)
        cart_item.delete()


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        'marketplace.apps.authentication.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    item = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
