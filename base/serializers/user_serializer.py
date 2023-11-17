from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.conf import settings

User = get_user_model()

class HostSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'picture']
    
    def get_picture(self, obj):
        # Get the request object from the context
        request = self.context.get('request')

        # Check if the request is available and has the necessary information
        if request and request.META.get('HTTP_HOST'):
            domain = request.scheme + '://' + request.META['HTTP_HOST']
        else:
            # Use a default domain or handle the case when the domain is not available
            domain = getattr(settings, 'DEFAULT_DOMAIN', 'http://localhost:8000')

        # Add the domain to the picture field value
        return f"{domain}{obj.picture.url}" if obj.picture else None

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

    