from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "student", "Ученик"
        TEACHER = "teacher", "Преподаватель"

    email = models.EmailField(
        verbose_name="Электронная почта",
        unique=True,
    )

    role = models.CharField(
        verbose_name="Роль",
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    def __str__(self) -> str:
        return self.get_username()
