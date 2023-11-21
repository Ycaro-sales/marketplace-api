import uuid
from django.db import models, transaction
from django.contrib.auth.models import AbstractUser
from marketplace.apps.cart.models import CartManager


class User(AbstractUser):
    is_staff = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='customer')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    objects = CustomerManager()

    def __str__(self):
        return str(self.email)


class CustomerManager(models.Manager):
    @ transaction.atomic
    def create_user(self, email, password):
        user = self.create(email=email, password=password)
        user.save()

        cart = CartManager.create(user=user)
        cart.save()

        return user
