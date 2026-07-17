from typing import cast

from django.db.models import QuerySet
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from accounts.models import User
from accounts.permissions import is_teacher_or_admin
from education.models import Lesson
from progress.models import ExerciseProgress, LessonProgress
from progress.serializers import ExerciseProgressSerializer, LessonProgressSerializer


class LessonProgressViewSet(viewsets.ReadOnlyModelViewSet):
    """API для просмотра и обновления прогресса по урокам."""

    queryset = LessonProgress.objects.none()
    serializer_class = LessonProgressSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_fields = (
        "lesson",
        "lesson__module",
        "lesson__module__course",
        "status",
    )
    search_fields = (
        "student__username",
        "lesson__title",
        "lesson__module__title",
        "lesson__module__course__title",
    )
    ordering_fields = (
        "last_opened_at",
        "completed_at",
        "time_spent_seconds",
        "status",
    )
    ordering = ("-last_opened_at",)

    def get_queryset(self) -> QuerySet[LessonProgress]:
        """Вернуть прогресс по урокам с учётом роли пользователя."""
        if getattr(self, "swagger_fake_view", False):
            return LessonProgress.objects.none()

        queryset = LessonProgress.objects.select_related(
            "student",
            "lesson",
            "lesson__module",
            "lesson__module__course",
        ).all()

        if is_teacher_or_admin(self.request.user):
            return queryset

        student = cast(User, self.request.user)

        return queryset.filter(student=student)

    def get_available_lesson(self, lesson_id: int | str) -> Lesson:
        """Получить урок, доступный текущему пользователю."""
        queryset = Lesson.objects.select_related(
            "module",
            "module__course",
        ).all()

        if not is_teacher_or_admin(self.request.user):
            queryset = queryset.filter(
                is_published=True,
                module__course__is_published=True,
            )

        try:
            return queryset.get(pk=lesson_id)
        except (Lesson.DoesNotExist, ValueError, TypeError):
            raise ValidationError({"lesson": "Урок не найден или недоступен."}) from None

    @action(detail=False, methods=["post"], url_path="open-lesson")
    def open_lesson(self, request: Request) -> Response:
        """Отметить урок как открытый текущим пользователем."""
        raw_lesson_id = request.data.get("lesson")

        if raw_lesson_id is None:
            raise ValidationError({"lesson": "Укажите ID урока."})

        lesson_id = cast(int | str, raw_lesson_id)
        student = cast(User, request.user)
        lesson = self.get_available_lesson(lesson_id)

        lesson_progress, _created = LessonProgress.objects.get_or_create(
            student=student,
            lesson=lesson,
        )
        lesson_progress.mark_opened()

        serializer = self.get_serializer(lesson_progress)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path="complete-lesson")
    def complete_lesson(self, request: Request) -> Response:
        """Отметить урок как завершённый текущим пользователем."""
        raw_lesson_id = request.data.get("lesson")

        if raw_lesson_id is None:
            raise ValidationError({"lesson": "Укажите ID урока."})

        lesson_id = cast(int | str, raw_lesson_id)
        student = cast(User, request.user)
        lesson = self.get_available_lesson(lesson_id)

        lesson_progress, _created = LessonProgress.objects.get_or_create(
            student=student,
            lesson=lesson,
        )
        lesson_progress.mark_completed()

        serializer = self.get_serializer(lesson_progress)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ExerciseProgressViewSet(viewsets.ReadOnlyModelViewSet):
    """API для просмотра прогресса по практическим заданиям."""

    queryset = ExerciseProgress.objects.none()
    serializer_class = ExerciseProgressSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_fields = (
        "exercise",
        "exercise__lesson",
        "exercise__lesson__module",
        "exercise__lesson__module__course",
    )
    search_fields = (
        "student__username",
        "exercise__title",
        "exercise__lesson__title",
        "exercise__lesson__module__course__title",
    )
    ordering_fields = (
        "attempts_count",
        "best_score",
        "max_score",
        "last_submitted_at",
    )
    ordering = ("-last_submitted_at",)

    def get_queryset(self) -> QuerySet[ExerciseProgress]:
        """Вернуть прогресс по заданиям с учётом роли пользователя."""
        if getattr(self, "swagger_fake_view", False):
            return ExerciseProgress.objects.none()

        queryset = ExerciseProgress.objects.select_related(
            "student",
            "exercise",
            "exercise__lesson",
            "exercise__lesson__module",
            "exercise__lesson__module__course",
            "best_submission",
        ).all()

        if is_teacher_or_admin(self.request.user):
            return queryset

        student = cast(User, self.request.user)

        return queryset.filter(student=student)
