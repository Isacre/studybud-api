from rest_framework import viewsets
from base.serializers.user_serializer import  CustomUserSerializer
from users.models import UserAccount


class UserViewset(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = CustomUserSerializer

    
    
