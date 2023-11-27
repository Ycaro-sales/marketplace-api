import uuid
from django.db import models, transaction
from django.contrib.auth.models import AbstractUser


class DefaultUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        db_table = 'users'


class CustomerManager(models.Manager):

    @transaction.atomic
    def create_customer(self, username, email, password):
        from marketplace.apps.store.models import Cart

        customer = Customer.objects.create(username=username, email=email, password=password)
        customer.save()

        customer.cart = Cart.objects.create(owner=customer)
        customer.save()

        return customer


class Customer(DefaultUser):
    objects = CustomerManager()
    cart = models.OneToOneField("store.Cart", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.email)
