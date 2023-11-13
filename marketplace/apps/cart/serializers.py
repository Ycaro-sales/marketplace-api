from marketplace.apps.cart.models import Cart, CartItem, Product
from rest_framework import serializers


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'created_at', 'updated_at')


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'item', 'quantity', 'cart')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'user', 'created_at', 'updated_at')
