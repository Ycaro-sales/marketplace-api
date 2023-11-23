import uuid
from django.db import models, transaction
from django.contrib.auth.models import AbstractUser
from marketplace.apps.store.models import Cart


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        db_table = 'users'


class CustomerManager(models.Manager):
    @transaction.atomic
    def create_customer(self, email, password):
        customer = self.create(email=email, password=password)

        customer.cart = Cart.objects.create(owner=customer)

        return customer


class Customer(User):
    objects = CustomerManager()
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.email)
