from rest_framework import generics, viewsets, permissions, mixins
from marketplace.apps.authentication.models.models import Customer
from marketplace.apps.authentication.serializers import CustomerSerializer, ManagerSerializer


class CustomerViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user)


class SignUpView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [permissions.IsAuthenticated]
