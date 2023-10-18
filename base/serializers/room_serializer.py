from rest_framework import serializers
from .user_serializer import HostSerializer
from .topic_serializer import TopicSerializer
from base.models.room import Room

class RoomSerializer(serializers.ModelSerializer):
    host = HostSerializer()
    topic = TopicSerializer()

    class Meta:
        model = Room
        fields = '__all__'
        
        

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'