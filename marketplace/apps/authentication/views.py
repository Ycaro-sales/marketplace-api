from django.shortcuts import render
from rest_framework import generics


class CustomerViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated, isOwnerOrAdmin]


