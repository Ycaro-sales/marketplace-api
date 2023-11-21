from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=200)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
