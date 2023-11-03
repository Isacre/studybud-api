from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

User = get_user_model()

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username', 'picture']

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username', 'picture', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate_password(self, value: str) -> str:
        return make_password(value)

    