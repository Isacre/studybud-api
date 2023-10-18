from dataclasses import fields
from rest_framework import serializers
from users.models import UserAccount

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'username']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id','email', 'password', 'username', 'picture']

    