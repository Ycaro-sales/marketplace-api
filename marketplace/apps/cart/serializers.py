from marketplace.apps.cart.models import Cart, CartItem, Product
from marketplace.apps.authentication.models import Customer
from rest_framework import serializers


class CartSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source=Customer)

    class Meta:
        model = Cart
        fields = ('id', 'created_at', 'updated_at')


class CartItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CartItem
        fields = ('id', 'item', 'quantity', 'cart')


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'user', 'created_at', 'updated_at')
