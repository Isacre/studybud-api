from rest_framework import viewsets
from base.models.message import Message
from base.serializers.message_serializer import MessageSerializer

class MessagesViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer