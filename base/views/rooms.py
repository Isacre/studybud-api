from django.http import JsonResponse
from rest_framework import viewsets
from base.models.room import Room
from base.serializers.room_serializer import CreateRoomSerializer, RoomSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter

class RoomsViewset(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    search_fields = ['topic__name', 'name', 'description']
    filter_backends = [SearchFilter]

    def get_serializer_class(self):
        if self.action in ['create']:
            return CreateRoomSerializer
        else:
            return RoomSerializer
    
    def create(self, request):
        serialized_data = CreateRoomSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset()).order_by('created_at')
        serialized_rooms = RoomSerializer(queryset, many=True)
        return JsonResponse(serialized_rooms.data, safe=False)
    
    @action(methods=['GET'], detail=True)
    def retrieve_room(self, request, **kwargs):
        pk = kwargs.get('pk')
        room = Room.objects.get(id=pk)
        return JsonResponse(RoomSerializer(room).data)




