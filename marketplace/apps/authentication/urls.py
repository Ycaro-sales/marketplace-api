from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from marketplace.apps.authentication.views import (
    CustomerViewSet,
    ManagerViewSet,
)

urlpatterns = [
    path('login/', ),
    path('signup/', ),
    path('jwt/create', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
