from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=255, default='guest')
    room = models.CharField(max_length=1000000)
    image = models.ImageField(upload_to='chat_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.user}: {self.value[:50]}..."  # Truncate message preview
