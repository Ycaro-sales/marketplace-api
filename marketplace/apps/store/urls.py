from django.urls import path
from marketplace.apps.store.views import (
    CartViewSet,
    CartItemViewSet,
    ProductViewSet,
)

from rest_framework import routers, include

router = routers.DefaultRouter()

router.register('', ProductViewSet, basename='product')
router.register('cart', CartViewSet, basename='cart')
router.register('cart/items', CartItemViewSet, basename='cart_item')

urlpatterns = [
    path('', include(router.urls)),
]

