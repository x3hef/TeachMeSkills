from rest_framework import permissions, viewsets

from assessments.models import Exercise, TestCase
from assessments.serializers import ExerciseSerializer, TestCaseSerializer


class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    """Публичный API для просмотра опубликованных практических заданий."""

    queryset = (
        Exercise.objects.filter(
            is_published=True,
            lesson__is_published=True,
            lesson__module__course__is_published=True,
        )
        .select_related("lesson", "lesson__module", "lesson__module__course")
        .order_by("lesson__module__course__title", "lesson__module__order", "lesson__order", "order")
    )
    serializer_class = ExerciseSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_fields = ("lesson", "lesson__module", "lesson__module__course", "difficulty", "check_strategy")
    search_fields = (
        "title",
        "short_description",
        "statement",
        "lesson__title",
        "lesson__module__course__title",
    )
    ordering_fields = ("title", "order", "max_score", "created_at", "updated_at")
    ordering = ("lesson__module__course__title", "lesson__module__order", "lesson__order", "order")


class TestCaseViewSet(viewsets.ReadOnlyModelViewSet):
    """Публичный API для просмотра только открытых тест-кейсов."""

    queryset = (
        TestCase.objects.filter(
            is_hidden=False,
            exercise__is_published=True,
            exercise__lesson__is_published=True,
            exercise__lesson__module__course__is_published=True,
        )
        .select_related(
            "exercise", "exercise__lesson", "exercise__lesson__module", "exercise__lesson__module__course"
        )
        .order_by("exercise", "order")
    )
    serializer_class = TestCaseSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_fields = ("exercise", "exercise__lesson", "is_hidden")
    search_fields = ("name", "input_data", "expected_output", "exercise__title")
    ordering_fields = ("order", "points", "created_at", "updated_at")
    ordering = ("exercise", "order")
