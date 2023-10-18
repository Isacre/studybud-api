from rest_framework import viewsets
from base.models.topic import Topic
from base.serializers.topic_serializer import TopicSerializer

class TopicViewset(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer