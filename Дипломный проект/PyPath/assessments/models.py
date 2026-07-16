from typing import Any

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from education.models import Lesson


class Exercise(models.Model):
    """Практическое задание внутри урока.

    Модель хранит условие задачи, стартовый код, ограничения проверки
    и настройки отображения задания на платформе PyPath.
    """

    class Difficulty(models.TextChoices):
        EASY = "easy", "Лёгкая"
        MEDIUM = "medium", "Средняя"
        HARD = "hard", "Сложная"

    class CheckStrategy(models.TextChoices):
        STDIN_STDOUT = "stdin_stdout", "Проверка через stdin/stdout"
        UNIT_TEST = "unit_test", "Проверка через unit-тесты"

    lesson = models.ForeignKey(
        Lesson,
        verbose_name="Урок",
        on_delete=models.CASCADE,
        related_name="exercises",
    )

    title = models.CharField(
        verbose_name="Название",
        max_length=200,
    )

    slug = models.SlugField(
        verbose_name="URL-имя",
        max_length=220,
        allow_unicode=True,
        blank=True,
    )

    short_description = models.CharField(
        verbose_name="Краткое описание",
        max_length=255,
        blank=True,
    )

    statement = models.TextField(
        verbose_name="Условие задания",
    )

    difficulty = models.CharField(
        verbose_name="Сложность",
        max_length=20,
        choices=Difficulty.choices,
        default=Difficulty.EASY,
    )

    check_strategy = models.CharField(
        verbose_name="Способ проверки",
        max_length=30,
        choices=CheckStrategy.choices,
        default=CheckStrategy.STDIN_STDOUT,
    )

    starter_code = models.TextField(
        verbose_name="Стартовый код",
        blank=True,
        default="",
    )

    reference_solution = models.TextField(
        verbose_name="Эталонное решение",
        blank=True,
        default="",
    )

    order = models.PositiveIntegerField(
        verbose_name="Порядок",
        default=1,
        validators=[MinValueValidator(1)],
    )

    max_score = models.PositiveIntegerField(
        verbose_name="Максимальный балл",
        default=100,
        validators=[MinValueValidator(1)],
    )

    time_limit_ms = models.PositiveIntegerField(
        verbose_name="Лимит времени, мс",
        default=2000,
        validators=[MinValueValidator(100)],
    )

    memory_limit_mb = models.PositiveIntegerField(
        verbose_name="Лимит памяти, МБ",
        default=128,
        validators=[MinValueValidator(16)],
    )

    is_published = models.BooleanField(
        verbose_name="Опубликовано",
        default=False,
    )

    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="Дата обновления",
        auto_now=True,
    )

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
        ordering = ("lesson__module__course", "lesson__module__order", "lesson__order", "order")
        constraints = [
            models.UniqueConstraint(
                fields=("lesson", "order"),
                name="unique_exercise_order_per_lesson",
            ),
            models.UniqueConstraint(
                fields=("lesson", "slug"),
                name="unique_exercise_slug_per_lesson",
            ),
        ]

    def __str__(self) -> str:
        """Вернуть понятное название задания с названием урока."""
        return f"{self.lesson.title}: {self.title}"

    def save(self, *args: Any, **kwargs: Any) -> None:
        """Автоматически создать slug из названия задания, если он не указан."""
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)

        super().save(*args, **kwargs)


class TestCase(models.Model):
    """Тест-кейс для автоматической проверки задания.

    Тест-кейс хранит входные данные, ожидаемый вывод и настройки видимости.
    Открытые тесты можно показывать ученику, скрытые используются для финальной проверки.
    """

    exercise = models.ForeignKey(
        Exercise,
        verbose_name="Задание",
        on_delete=models.CASCADE,
        related_name="test_cases",
    )

    name = models.CharField(
        verbose_name="Название",
        max_length=120,
        blank=True,
    )

    input_data = models.TextField(
        verbose_name="Входные данные",
        blank=True,
    )

    expected_output = models.TextField(
        verbose_name="Ожидаемый вывод",
    )

    is_hidden = models.BooleanField(
        verbose_name="Скрытый тест",
        default=False,
    )

    order = models.PositiveIntegerField(
        verbose_name="Порядок",
        default=1,
        validators=[MinValueValidator(1)],
    )

    points = models.PositiveIntegerField(
        verbose_name="Баллы",
        default=10,
        validators=[MinValueValidator(1)],
    )

    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="Дата обновления",
        auto_now=True,
    )

    class Meta:
        verbose_name = "Тест-кейс"
        verbose_name_plural = "Тест-кейсы"
        ordering = ("exercise", "order")
        constraints = [
            models.UniqueConstraint(
                fields=("exercise", "order"),
                name="unique_test_case_order_per_exercise",
            ),
        ]

    def __str__(self) -> str:
        """Вернуть понятное название тест-кейса."""
        test_name = self.name or f"Тест {self.order}"
        visibility = "скрытый" if self.is_hidden else "открытый"
        return f"{self.exercise.title}: {test_name} ({visibility})"
