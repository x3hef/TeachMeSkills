from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    meeting_time = models.DateTimeField()
    users = models.ManyToManyField(User, related_name="events", blank=True)

    def __str__(self):
        return self.name