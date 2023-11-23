from marketplace.apps.store.models import Cart, CartItem, Product
from marketplace.apps.authentication.models import Customer
from rest_framework import serializers


class CartField(serializers.RelatedField):
    def get_queryset(self):
        return Cart.objects.all()

    def to_representation(self, value):
        cart_items = CartItem.objects.filter(cart=value)
        items = []
        for cart_item in cart_items:
            items.append({
                'id': cart_item.id,
                'item': {
                    'id': cart_item.item.id,
                    'name': cart_item.item.name,
                    'quantity': cart_item.item.quantity,
                },
            })

        return {
            'id': value.id,
            'owner': value.owner,
            'items': items,
            'created_at': value.created_at,
            'updated_at': value.updated_at,
        }

    def to_internal_value(self, data):
        try:
            return Cart.objects.get(id=data)
        except Cart.DoesNotExist:
            raise serializers.ValidationError('Cart does not exist')


class CartSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source=Customer)

    class Meta:
        model = Cart
        fields = ('id', 'created_at', 'updated_at', 'owner')


class CartItemSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        try:
            cart_item = CartItem.objects.get(
                cart=validated_data.get('cart'),
                item=validated_data.get('item')
            )
            cart_item.quantity += validated_data.get('quantity')
            cart_item.save()
            return cart_item
        except CartItem.DoesNotExist:
            return CartItem.objects.create(**validated_data)

    class Meta:
        model = CartItem
        fields = ('id', 'item', 'quantity', 'cart')


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'user', 'created_at', 'updated_at')

