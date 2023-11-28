from rest_framework import (
    viewsets,
    mixins,
    status,
    permissions,
)

from rest_framework.response import Response
from marketplace.apps.authentication.permissions import IsOwnerOrStaff
from marketplace.apps.store.models import Cart, CartItem, Product
from marketplace.apps.store.serializers import CartSerializer, CartItemSerializer, ProductSerializer
from marketplace.apps.store.permissions import IsCartOwner, IsStaffOrReadonly


class CartViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrStaff]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Cart.objects.all()
        return Cart.objects.filter(owner=self.request.user)


class CartItemViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsCartOwner]

    def create(self, request, *args, **kwargs):
        data = dict(**request.data)
        data['cart'] = Cart.objects.filter(owner=request.user)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return CartItem.objects.filter(cart=Cart.objects.filter(owner=self.request.user))


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsStaffOrReadonly]
