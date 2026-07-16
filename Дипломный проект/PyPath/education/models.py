from typing import Any

from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Course(models.Model):
    """Учебный курс платформы PyPath.

    Курс является верхним уровнем учебной структуры.
    Он создаётся преподавателем и состоит из модулей.
    """

    title = models.CharField(
        verbose_name="Название",
        max_length=200,
    )

    slug = models.SlugField(
        verbose_name="URL-имя",
        max_length=220,
        unique=True,
        allow_unicode=True,
        blank=True,
    )

    description = models.TextField(
        verbose_name="Описание",
        blank=True,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Автор курса",
        on_delete=models.PROTECT,
        related_name="created_courses",
    )

    is_published = models.BooleanField(
        verbose_name="Опубликован",
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
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ("title",)

    def __str__(self) -> str:
        """Вернуть название курса для админки и отладочного вывода."""
        return self.title

    def save(self, *args: Any, **kwargs: Any) -> None:
        """Автоматически создать slug из названия, если он не указан."""
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)

        super().save(*args, **kwargs)


class Module(models.Model):
    """Раздел курса.

    Модуль группирует несколько уроков внутри одного курса.
    Например: «Основы Python», «Условия», «Циклы».
    """

    course = models.ForeignKey(
        Course,
        verbose_name="Курс",
        on_delete=models.CASCADE,
        related_name="modules",
    )

    title = models.CharField(
        verbose_name="Название",
        max_length=200,
    )

    description = models.TextField(
        verbose_name="Описание",
        blank=True,
    )

    order = models.PositiveIntegerField(
        verbose_name="Порядок",
        default=1,
    )

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "Модули"
        ordering = ("course", "order")
        constraints = [
            models.UniqueConstraint(
                fields=("course", "order"),
                name="unique_module_order_per_course",
            ),
        ]

    def __str__(self) -> str:
        """Вернуть понятное название модуля с названием курса."""
        return f"{self.course.title}: {self.title}"


class Lesson(models.Model):
    """Урок внутри модуля.

    Урок содержит теоретический материал, порядок отображения
    и флаг публикации для управления доступностью ученикам.
    """

    module = models.ForeignKey(
        Module,
        verbose_name="Модуль",
        on_delete=models.CASCADE,
        related_name="lessons",
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

    content = models.TextField(
        verbose_name="Содержание",
    )

    order = models.PositiveIntegerField(
        verbose_name="Порядок",
        default=1,
    )

    is_published = models.BooleanField(
        verbose_name="Опубликован",
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
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ("module__course", "module__order", "order")
        constraints = [
            models.UniqueConstraint(
                fields=("module", "order"),
                name="unique_lesson_order_per_module",
            ),
            models.UniqueConstraint(
                fields=("module", "slug"),
                name="unique_lesson_slug_per_module",
            ),
        ]

    def __str__(self) -> str:
        """Вернуть понятное название урока с названием модуля."""
        return f"{self.module.title}: {self.title}"

    def save(self, *args: Any, **kwargs: Any) -> None:
        """Автоматически создать slug из названия урока, если он не указан."""
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)

        super().save(*args, **kwargs)


class Enrollment(models.Model):
    """Запись ученика на курс.

    Модель связывает пользователя и курс.
    Через неё реализуется связь многие-ко-многим:
    один ученик может быть записан на несколько курсов,
    а один курс может иметь много учеников.
    """

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Ученик",
        on_delete=models.CASCADE,
        related_name="enrollments",
    )

    course = models.ForeignKey(
        Course,
        verbose_name="Курс",
        on_delete=models.CASCADE,
        related_name="enrollments",
    )

    enrolled_at = models.DateTimeField(
        verbose_name="Дата записи",
        auto_now_add=True,
    )

    is_active = models.BooleanField(
        verbose_name="Активна",
        default=True,
    )

    class Meta:
        verbose_name = "Запись на курс"
        verbose_name_plural = "Записи на курсы"
        ordering = ("-enrolled_at",)
        constraints = [
            models.UniqueConstraint(
                fields=("student", "course"),
                name="unique_student_course_enrollment",
            ),
        ]

    def __str__(self) -> str:
        """Вернуть строку вида: ученик → курс."""
        return f"{self.student} → {self.course}"
