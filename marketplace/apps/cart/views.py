from rest_framework import generics
from marketplace.apps.cart.models import Cart, CartItem, Product

from marketplace.apps.cart.serializers import CartSerializer, CartItemSerializer, ProductSerializer
from rest_framework import permissions
from marketplace.apps.cart.permissions import isOwner


class CartViewSet(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated, isOwner]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class CartItemViewSet(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated, isOwner]

    def get_queryset(self):
        return super().get_queryset().filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(cart=self.request.user.cart)


class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, isStaffOrReadOnly]
