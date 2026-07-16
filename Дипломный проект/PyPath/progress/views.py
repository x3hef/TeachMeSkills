from django.db.models import QuerySet
from rest_framework import permissions, viewsets

from progress.models import ExerciseProgress, LessonProgress
from progress.serializers import ExerciseProgressSerializer, LessonProgressSerializer


class LessonProgressViewSet(viewsets.ReadOnlyModelViewSet):
    """API для просмотра прогресса по урокам."""

    serializer_class = LessonProgressSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_fields = ("lesson", "lesson__module", "lesson__module__course", "status")
    search_fields = (
        "lesson__title",
        "lesson__module__title",
        "lesson__module__course__title",
    )
    ordering_fields = (
        "created_at",
        "updated_at",
        "last_opened_at",
        "completed_at",
        "time_spent_seconds",
        "status",
    )
    ordering = ("lesson__module__course__title", "lesson__module__order", "lesson__order")

    def get_queryset(self) -> QuerySet[LessonProgress]:
        """Вернуть прогресс текущего пользователя или весь прогресс для staff."""
        queryset = LessonProgress.objects.select_related(
            "student",
            "lesson",
            "lesson__module",
            "lesson__module__course",
        ).order_by("lesson__module__course__title", "lesson__module__order", "lesson__order")

        user = self.request.user

        if not user.is_authenticated:
            return queryset.none()

        if user.is_staff:
            return queryset

        return queryset.filter(student=user)


class ExerciseProgressViewSet(viewsets.ReadOnlyModelViewSet):
    """API для просмотра прогресса по практическим заданиям."""

    serializer_class = ExerciseProgressSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_fields = (
        "exercise",
        "exercise__lesson",
        "exercise__lesson__module__course",
        "status",
    )
    search_fields = (
        "exercise__title",
        "exercise__lesson__title",
        "exercise__lesson__module__course__title",
    )
    ordering_fields = (
        "created_at",
        "updated_at",
        "attempts_count",
        "best_score",
        "last_submitted_at",
        "solved_at",
        "status",
    )
    ordering = (
        "exercise__lesson__module__course__title",
        "exercise__lesson__module__order",
        "exercise__lesson__order",
        "exercise__order",
    )

    def get_queryset(self) -> QuerySet[ExerciseProgress]:
        """Вернуть прогресс текущего пользователя или весь прогресс для staff."""
        queryset = ExerciseProgress.objects.select_related(
            "student",
            "exercise",
            "exercise__lesson",
            "exercise__lesson__module",
            "exercise__lesson__module__course",
            "best_submission",
        ).order_by(
            "exercise__lesson__module__course__title",
            "exercise__lesson__module__order",
            "exercise__lesson__order",
            "exercise__order",
        )

        user = self.request.user

        if not user.is_authenticated:
            return queryset.none()

        if user.is_staff:
            return queryset

        return queryset.filter(student=user)
