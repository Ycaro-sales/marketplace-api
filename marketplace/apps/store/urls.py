from django.urls import path, include
from marketplace.apps.store.views.views import (
    CartViewSet,
    CartItemViewSet,
    ProductViewSet,
)

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'', ProductViewSet, basename='product')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cart/items', CartItemViewSet, basename='cart_item')

urlpatterns = [
    path('', include(router.urls)),
]
