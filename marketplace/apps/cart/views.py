from django.shortcuts import render
from rest_framework import viewsets
from marketplace.apps.cart.models import Cart, CartItem, Product


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
