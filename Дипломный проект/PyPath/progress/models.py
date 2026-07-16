from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

from assessments.models import Exercise
from education.models import Lesson
from submissions.models import Submission


class LessonProgress(models.Model):
    """Прогресс ученика по конкретному уроку.

    Модель хранит состояние прохождения урока, время последнего открытия,
    дату завершения и примерное время, которое ученик потратил на урок.
    """

    class Status(models.TextChoices):
        NOT_STARTED = "not_started", "Не начат"
        IN_PROGRESS = "in_progress", "В процессе"
        COMPLETED = "completed", "Завершён"

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Ученик",
        on_delete=models.CASCADE,
        related_name="lesson_progress_records",
    )

    lesson = models.ForeignKey(
        Lesson,
        verbose_name="Урок",
        on_delete=models.CASCADE,
        related_name="progress_records",
    )

    status = models.CharField(
        verbose_name="Статус",
        max_length=20,
        choices=Status.choices,
        default=Status.NOT_STARTED,
    )

    last_opened_at = models.DateTimeField(
        verbose_name="Дата последнего открытия",
        null=True,
        blank=True,
    )

    completed_at = models.DateTimeField(
        verbose_name="Дата завершения",
        null=True,
        blank=True,
    )

    time_spent_seconds = models.PositiveIntegerField(
        verbose_name="Потрачено времени, секунд",
        default=0,
        validators=[MinValueValidator(0)],
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
        verbose_name = "Прогресс урока"
        verbose_name_plural = "Прогресс уроков"
        ordering = ("student", "lesson__module__course", "lesson__module__order", "lesson__order")
        constraints = [
            models.UniqueConstraint(
                fields=("student", "lesson"),
                name="uniq_lesson_progress",
            ),
        ]
        indexes = [
            models.Index(
                fields=("student", "status"),
                name="lesson_prog_student_idx",
            ),
        ]

    def __str__(self) -> str:
        """Вернуть понятное описание прогресса урока."""
        return f"{self.student} → {self.lesson} ({self.status})"

    def mark_opened(self) -> None:
        """Зафиксировать открытие урока учеником."""
        self.last_opened_at = timezone.now()

        if self.status == self.Status.NOT_STARTED:
            self.status = self.Status.IN_PROGRESS
            self.save(update_fields=("last_opened_at", "status", "updated_at"))
            return

        self.save(update_fields=("last_opened_at", "updated_at"))

    def mark_completed(self) -> None:
        """Отметить урок как завершённый."""
        now = timezone.now()
        self.status = self.Status.COMPLETED
        self.completed_at = now
        self.last_opened_at = now
        self.save(update_fields=("status", "completed_at", "last_opened_at", "updated_at"))


class ExerciseProgress(models.Model):
    """Прогресс ученика по конкретному практическому заданию.

    Модель хранит количество попыток, лучший балл, статус решения
    и ссылку на лучшую отправку решения.
    """

    class Status(models.TextChoices):
        NOT_STARTED = "not_started", "Не начато"
        ATTEMPTED = "attempted", "Была попытка"
        SOLVED = "solved", "Решено"

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Ученик",
        on_delete=models.CASCADE,
        related_name="exercise_progress_records",
    )

    exercise = models.ForeignKey(
        Exercise,
        verbose_name="Задание",
        on_delete=models.CASCADE,
        related_name="progress_records",
    )

    best_submission = models.ForeignKey(
        Submission,
        verbose_name="Лучшая отправка",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="best_for_progress_records",
    )

    status = models.CharField(
        verbose_name="Статус",
        max_length=20,
        choices=Status.choices,
        default=Status.NOT_STARTED,
    )

    attempts_count = models.PositiveIntegerField(
        verbose_name="Количество попыток",
        default=0,
    )

    best_score = models.PositiveIntegerField(
        verbose_name="Лучший балл",
        default=0,
    )

    max_score = models.PositiveIntegerField(
        verbose_name="Максимальный балл",
        default=100,
        validators=[MinValueValidator(1)],
    )

    last_submitted_at = models.DateTimeField(
        verbose_name="Дата последней отправки",
        null=True,
        blank=True,
    )

    solved_at = models.DateTimeField(
        verbose_name="Дата решения",
        null=True,
        blank=True,
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
        verbose_name = "Прогресс задания"
        verbose_name_plural = "Прогресс заданий"
        ordering = (
            "student",
            "exercise__lesson__module__course",
            "exercise__lesson__order",
            "exercise__order",
        )
        constraints = [
            models.UniqueConstraint(
                fields=("student", "exercise"),
                name="uniq_exercise_progress",
            ),
        ]
        indexes = [
            models.Index(
                fields=("student", "status"),
                name="exercise_prog_student_idx",
            ),
        ]

    def __str__(self) -> str:
        """Вернуть понятное описание прогресса задания."""
        return f"{self.student} → {self.exercise} ({self.status})"

    def register_attempt(self, submission: Submission) -> None:
        """Зарегистрировать новую попытку решения задания."""
        self.attempts_count += 1
        self.last_submitted_at = timezone.now()

        if self.status == self.Status.NOT_STARTED:
            self.status = self.Status.ATTEMPTED

        if submission.score >= self.best_score:
            self.best_score = submission.score
            self.max_score = submission.max_score
            self.best_submission = submission

        if submission.status == Submission.Status.ACCEPTED:
            self.status = self.Status.SOLVED
            self.solved_at = timezone.now()

        self.save(
            update_fields=(
                "attempts_count",
                "last_submitted_at",
                "status",
                "best_score",
                "max_score",
                "best_submission",
                "solved_at",
                "updated_at",
            )
        )
