from rest_framework import serializers
from authentication.models import CustomerManager


class CustomerSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=200)

    def create(self, validated_data):
        return CustomerManager.create(**validated_data)
