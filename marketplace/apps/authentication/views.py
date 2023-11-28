from rest_framework import generics, viewsets, permissions, mixins
from marketplace.apps.authentication.models import Customer
from marketplace.apps.authentication.serializers import CustomerSerializer, ManagerSerializer

from rest_framework_simplejwt import authentication


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = Customer.objects.all()
        else:
            queryset = Customer.objects.filter(id=user.id)

        return queryset


class SignUpView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [permissions.IsAuthenticated]
