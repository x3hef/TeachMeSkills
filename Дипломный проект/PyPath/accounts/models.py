from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser): # основа для наследников.
    class Role(models.TextChoices):
        STUDENT = "student", "Студент"
        MENTOR = "mentor", "Наставник"
        COURSE_AUTHOR = "course_author", "Автор курса"

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
        return self.username
