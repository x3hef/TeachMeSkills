from django.db.models import QuerySet
from rest_framework import viewsets

from accounts.permissions import IsReadOnlyOrTeacherOrAdmin, is_teacher_or_admin
from assessments.models import Exercise, TestCase
from assessments.serializers import ExerciseSerializer, TestCaseSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    """API для просмотра и управления практическими заданиями."""

    serializer_class = ExerciseSerializer
    permission_classes = (IsReadOnlyOrTeacherOrAdmin,)
    filterset_fields = (
        "lesson",
        "lesson__module",
        "lesson__module__course",
        "difficulty",
        "check_strategy",
        "is_published",
    )
    search_fields = (
        "title",
        "short_description",
        "statement",
        "lesson__title",
        "lesson__module__title",
        "lesson__module__course__title",
    )
    ordering_fields = (
        "order",
        "title",
        "difficulty",
        "created_at",
        "updated_at",
    )
    ordering = (
        "lesson",
        "order",
    )

    def get_queryset(self) -> QuerySet[Exercise]:
        """Вернуть список заданий с учётом роли пользователя."""
        queryset = Exercise.objects.select_related(
            "lesson",
            "lesson__module",
            "lesson__module__course",
        ).all()

        if is_teacher_or_admin(self.request.user):
            return queryset

        return queryset.filter(
            is_published=True,
            lesson__is_published=True,
            lesson__module__course__is_published=True,
        )


class TestCaseViewSet(viewsets.ModelViewSet):
    """API для просмотра и управления тест-кейсами."""

    serializer_class = TestCaseSerializer
    permission_classes = (IsReadOnlyOrTeacherOrAdmin,)
    filterset_fields = (
        "exercise",
        "exercise__lesson",
        "exercise__lesson__module",
        "exercise__lesson__module__course",
        "is_hidden",
    )
    search_fields = (
        "name",
        "input_data",
        "expected_output",
        "exercise__title",
        "exercise__lesson__title",
    )
    ordering_fields = (
        "order",
        "points",
        "created_at",
        "updated_at",
    )
    ordering = (
        "exercise",
        "order",
    )

    def get_queryset(self) -> QuerySet[TestCase]:
        """Вернуть список тест-кейсов с учётом роли пользователя."""
        queryset = TestCase.objects.select_related(
            "exercise",
            "exercise__lesson",
            "exercise__lesson__module",
            "exercise__lesson__module__course",
        ).all()

        if is_teacher_or_admin(self.request.user):
            return queryset

        return queryset.filter(
            is_hidden=False,
            exercise__is_published=True,
            exercise__lesson__is_published=True,
            exercise__lesson__module__course__is_published=True,
        )
