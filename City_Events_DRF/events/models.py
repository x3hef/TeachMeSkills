from django.conf import settings
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    meeting_time = models.DateTimeField()
    place = models.CharField(max_length=200)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='events', blank=True)

    def __str__(self):
        return self.name
