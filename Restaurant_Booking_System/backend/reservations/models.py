from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):

    number = models.IntegerField()

    seats = models.IntegerField()

    image = models.ImageField(
        upload_to='tables/',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Table {self.number}"


class Reservation(models.Model):

    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    hour_start = models.IntegerField()

    hour_end = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user} - {self.table}"

