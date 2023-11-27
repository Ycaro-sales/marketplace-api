from rest_framework import generics, viewsets, permissions
from marketplace.apps.authentication.models import Customer
from marketplace.apps.authentication.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated, isOwnerOrAdmin]


class SignUpView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]
