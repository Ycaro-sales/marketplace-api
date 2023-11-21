import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = 'users'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class UserManager(models.Manager):
    def create_user(self, email, password):
        user = self.create(email=email, password=password)
        user.save()
        return user

