from django.urls import path
from marketplace.apps.cart.views import CartViewSet, CartItemViewSet, AddToCartView, RemoveFromCartView, ProductViewSet

path = [
    path('', ProductViewSet.as_view()),
    path('cart/', CartViewSet.as_view()),
    path('cart/items', CartItemViewSet.as_view()),
    path('cart/items/<int:cart_product_id>/add', AddToCartView.as_view()),
    path('cart/items/<int:cart_product_id>/remove', RemoveFromCartView.as_view()),
]
