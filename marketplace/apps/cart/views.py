from rest_framework import generics
from marketplace.apps.cart.models import Cart, CartItem, Product

from marketplace.apps.cart.serializers import CartSerializer, CartItemSerializer, ProductSerializer


class CartViewSet(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class CartItemViewSet(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
