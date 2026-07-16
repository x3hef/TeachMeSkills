from typing import Any, cast

from django.db.models import QuerySet
from rest_framework import mixins, permissions, serializers, viewsets
from rest_framework.exceptions import PermissionDenied

from submissions.models import Submission, TestCaseResult
from submissions.serializers import SubmissionSerializer, TestCaseResultSerializer


class SubmissionViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """API для создания и просмотра отправок решений."""

    serializer_class = SubmissionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_fields = ("exercise", "status")
    search_fields = ("code", "exercise__title")
    ordering_fields = ("created_at", "updated_at", "score", "status")
    ordering = ("-created_at",)

    def get_queryset(self) -> QuerySet[Submission]:
        """Вернуть отправки текущего пользователя или все отправки для staff."""
        queryset = (
            Submission.objects.select_related("student", "exercise")
            .prefetch_related("test_results", "test_results__test_case")
            .order_by("-created_at")
        )

        user = self.request.user

        if not user.is_authenticated:
            return queryset.none()

        if user.is_staff:
            return queryset

        return queryset.filter(student=user)

    def perform_create(self, serializer: serializers.BaseSerializer[Any]) -> None:
        """Создать отправку решения от имени текущего пользователя."""
        user = self.request.user

        if not user.is_authenticated:
            raise PermissionDenied("Authentication is required.")

        submission_serializer = cast(SubmissionSerializer, serializer)
        exercise = submission_serializer.validated_data["exercise"]

        submission_serializer.save(
            student=user,
            max_score=exercise.max_score,
            total_tests=exercise.test_cases.count(),
        )


class TestCaseResultViewSet(viewsets.ReadOnlyModelViewSet):
    """API для просмотра результатов тест-кейсов по отправкам решений."""

    serializer_class = TestCaseResultSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_fields = ("submission", "test_case", "status")
    search_fields = (
        "test_case__name",
        "test_case__exercise__title",
        "actual_output",
        "error_message",
    )
    ordering_fields = ("created_at", "updated_at", "points_awarded", "status")
    ordering = ("-created_at",)

    def get_queryset(self) -> QuerySet[TestCaseResult]:
        """Вернуть результаты текущего пользователя или все результаты для staff."""
        queryset = TestCaseResult.objects.select_related(
            "submission",
            "submission__student",
            "test_case",
            "test_case__exercise",
        ).order_by("-created_at")

        user = self.request.user

        if not user.is_authenticated:
            return queryset.none()

        if user.is_staff:
            return queryset

        return queryset.filter(submission__student=user)
