from django.contrib import admin
from base.models.room import Room
from base.models.topic import Topic
from base.models.message import Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)