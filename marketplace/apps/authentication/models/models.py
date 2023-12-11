import uuid
from django.db import models, transaction
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password


class DefaultUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        db_table = 'users'


class CustomerManager(UserManager):

    @transaction.atomic
    def _create_user(self, username, email, password, **extra_fields):
        from marketplace.apps.store.models import Cart
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)

        username = Customer.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        cart = Cart.objects.create(owner=user)
        cart.save()

        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)


class Customer(DefaultUser):
    objects = CustomerManager()
    cart = models.OneToOneField("store.Cart", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.email)
