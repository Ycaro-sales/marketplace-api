from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from marketplace.apps.authentication.views.views import (
    CustomerViewSet,
    ManagerViewSet,
    SignUpView,
    # ManagerViewSet,
)

router = routers.DefaultRouter()

router.register(r'customer', CustomerViewSet)
router.register(r'staff/customers', ManagerViewSet)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify')
]
