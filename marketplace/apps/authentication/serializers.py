from rest_framework import serializers
from marketplace.apps.authentication.models import Customer, DefaultUser
from marketplace.apps.store.serializers import CartField


class CustomerSerializer(serializers.ModelSerializer):
    cart = CartField(read_only=True)

    def create(self, validated_data):
        return Customer.objects.create_user(**validated_data)

    class Meta:
        model = Customer
        fields = ('id', 'username', 'email', 'password', 'cart')


class ManagerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return DefaultUser.objects.create_superuser(**validated_data)

    class Meta:
        model = DefaultUser
        fields = ('id', 'username', 'email', 'password')

