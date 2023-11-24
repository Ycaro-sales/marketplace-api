from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from marketplace.apps.authentication.views import (
    CustomerViewSet,
    # ManagerViewSet,
)

router = routers.DefaultRouter()

router.register(r'customer', CustomerViewSet)

urlpatterns = [
    # path('login/', ),
    # path('signup/', ),
    path('', include(router.urls)),
    path('jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
