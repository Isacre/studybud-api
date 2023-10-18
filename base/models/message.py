from django.db import models
from .room import Room
from users.models import UserAccount


class Message(models.Model):
   user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
   room = models.ForeignKey(Room, on_delete=models.CASCADE)
   body = models.TextField()
   updated_at = models.DateTimeField(auto_now=True)  
   created_at = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
        return self.body[0:50]