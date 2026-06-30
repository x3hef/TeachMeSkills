from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    meeting_time = models.DateTimeField()
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="events", blank=True)

    def __str__(self):
        return self.name