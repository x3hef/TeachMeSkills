from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

from assessments.models import Exercise, TestCase


class Submission(models.Model):
    """Отправка решения ученика на практическое задание.

    Модель хранит код ученика, статус проверки, количество баллов
    и техническую информацию, которая появится после запуска code runner.
    """

    class Status(models.TextChoices):
        QUEUED = "queued", "В очереди"
        RUNNING = "running", "Проверяется"
        ACCEPTED = "accepted", "Принято"
        WRONG_ANSWER = "wrong_answer", "Неверный ответ"
        RUNTIME_ERROR = "runtime_error", "Ошибка выполнения"
        TIME_LIMIT_EXCEEDED = "time_limit_exceeded", "Превышен лимит времени"
        MEMORY_LIMIT_EXCEEDED = "memory_limit_exceeded", "Превышен лимит памяти"
        INTERNAL_ERROR = "internal_error", "Внутренняя ошибка проверки"

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Ученик",
        on_delete=models.CASCADE,
        related_name="submissions",
    )

    exercise = models.ForeignKey(
        Exercise,
        verbose_name="Задание",
        on_delete=models.PROTECT,
        related_name="submissions",
    )

    code = models.TextField(
        verbose_name="Код решения",
    )

    status = models.CharField(
        verbose_name="Статус",
        max_length=40,
        choices=Status.choices,
        default=Status.QUEUED,
    )

    score = models.PositiveIntegerField(
        verbose_name="Полученные баллы",
        default=0,
    )

    max_score = models.PositiveIntegerField(
        verbose_name="Максимальный балл",
        default=100,
        validators=[MinValueValidator(1)],
    )

    passed_tests = models.PositiveIntegerField(
        verbose_name="Пройдено тестов",
        default=0,
    )

    total_tests = models.PositiveIntegerField(
        verbose_name="Всего тестов",
        default=0,
    )

    execution_time_ms = models.PositiveIntegerField(
        verbose_name="Время выполнения, мс",
        null=True,
        blank=True,
    )

    memory_used_mb = models.PositiveIntegerField(
        verbose_name="Использовано памяти, МБ",
        null=True,
        blank=True,
    )

    stdout = models.TextField(
        verbose_name="Стандартный вывод",
        blank=True,
        default="",
    )

    stderr = models.TextField(
        verbose_name="Стандартный поток ошибок",
        blank=True,
        default="",
    )

    error_message = models.TextField(
        verbose_name="Сообщение об ошибке",
        blank=True,
        default="",
    )

    created_at = models.DateTimeField(
        verbose_name="Дата отправки",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="Дата обновления",
        auto_now=True,
    )

    checked_at = models.DateTimeField(
        verbose_name="Дата проверки",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Отправка решения"
        verbose_name_plural = "Отправки решений"
        ordering = ("-created_at",)
        indexes = [
            models.Index(
                fields=("student", "exercise", "-created_at"),
                name="sub_student_ex_idx",
            ),
            models.Index(
                fields=("status", "-created_at"),
                name="sub_status_created_idx",
            ),
        ]

    def __str__(self) -> str:
        """Вернуть понятное описание отправки решения."""
        return f"{self.student} → {self.exercise} ({self.status})"

    def mark_as_checked(self) -> None:
        """Зафиксировать дату завершения проверки решения."""
        self.checked_at = timezone.now()
        self.save(update_fields=("checked_at", "updated_at"))


class TestCaseResult(models.Model):
    """Результат прохождения одного тест-кейса в рамках одной отправки.

    Модель хранит фактический вывод программы, статус прохождения теста,
    начисленные баллы и техническую информацию по конкретному тесту.
    """

    class Status(models.TextChoices):
        PASSED = "passed", "Пройден"
        FAILED = "failed", "Не пройден"
        ERROR = "error", "Ошибка"
        SKIPPED = "skipped", "Пропущен"

    submission = models.ForeignKey(
        Submission,
        verbose_name="Отправка решения",
        on_delete=models.CASCADE,
        related_name="test_results",
    )

    test_case = models.ForeignKey(
        TestCase,
        verbose_name="Тест-кейс",
        on_delete=models.PROTECT,
        related_name="results",
    )

    status = models.CharField(
        verbose_name="Статус",
        max_length=20,
        choices=Status.choices,
        default=Status.SKIPPED,
    )

    input_data = models.TextField(
        verbose_name="Входные данные",
        blank=True,
        default="",
    )

    expected_output = models.TextField(
        verbose_name="Ожидаемый вывод",
        blank=True,
        default="",
    )

    actual_output = models.TextField(
        verbose_name="Фактический вывод",
        blank=True,
        default="",
    )

    error_message = models.TextField(
        verbose_name="Сообщение об ошибке",
        blank=True,
        default="",
    )

    execution_time_ms = models.PositiveIntegerField(
        verbose_name="Время выполнения, мс",
        null=True,
        blank=True,
    )

    memory_used_mb = models.PositiveIntegerField(
        verbose_name="Использовано памяти, МБ",
        null=True,
        blank=True,
    )

    points_awarded = models.PositiveIntegerField(
        verbose_name="Начисленные баллы",
        default=0,
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
        verbose_name = "Результат тест-кейса"
        verbose_name_plural = "Результаты тест-кейсов"
        ordering = ("submission", "test_case__order")
        constraints = [
            models.UniqueConstraint(
                fields=("submission", "test_case"),
                name="uniq_result_submission_test",
            ),
        ]

    def __str__(self) -> str:
        """Вернуть понятное описание результата тест-кейса."""
        return f"{self.submission} → {self.test_case} ({self.status})"
