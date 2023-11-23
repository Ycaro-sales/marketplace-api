from rest_framework import (
    generics,
    viewsets,
    mixins,
    status,
    # permissions,
)
from rest_framework.response import Response
from marketplace.apps.store.models import Cart, CartItem, Product
from marketplace.apps.store.serializers import CartSerializer, CartItemSerializer, ProductSerializer
# from marketplace.apps.store.permissions import isOwner


class CartViewSet(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # permission_classes = [permissions.IsAuthenticated, isStaff]


class CartItemViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs):
        data = dict(**request.data)
        data['cart'] = request.user.cart.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return CartItem.objects.all().filter(cart=self.request.user.cart)


class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated, isStaffOrReadOnly]
