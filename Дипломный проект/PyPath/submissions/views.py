from typing import cast

from django.db.models import QuerySet
from rest_framework import mixins, permissions, viewsets

from accounts.models import User
from accounts.permissions import is_teacher_or_admin
from submissions.models import Submission, TestCaseResult
from submissions.serializers import SubmissionSerializer, TestCaseResultSerializer
from submissions.services import check_submission


class SubmissionViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """API для создания и просмотра отправленных решений."""

    queryset = Submission.objects.none()
    serializer_class = SubmissionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_fields = (
        "exercise",
        "status",
        "created_at",
    )
    search_fields = (
        "exercise__title",
        "student__username",
    )
    ordering_fields = (
        "created_at",
        "checked_at",
        "score",
        "status",
    )
    ordering = ("-created_at",)

    def get_queryset(self) -> QuerySet[Submission]:
        """Вернуть отправки решений с учётом роли пользователя."""
        if getattr(self, "swagger_fake_view", False):
            return Submission.objects.none()

        queryset = Submission.objects.select_related(
            "student",
            "exercise",
            "exercise__lesson",
            "exercise__lesson__module",
            "exercise__lesson__module__course",
        ).prefetch_related("test_results")

        if is_teacher_or_admin(self.request.user):
            return queryset

        student = cast(User, self.request.user)

        return queryset.filter(student=student)

    def perform_create(self, serializer) -> None:
        """Создать отправку решения и запустить автоматическую проверку."""
        student = cast(User, self.request.user)
        exercise = serializer.validated_data["exercise"]

        submission = cast(
            Submission,
            serializer.save(
                student=student,
                max_score=exercise.max_score,
                total_tests=exercise.test_cases.count(),
            ),
        )

        check_submission(submission)


class TestCaseResultViewSet(viewsets.ReadOnlyModelViewSet):
    """API для просмотра результатов проверки по тест-кейсам."""

    queryset = TestCaseResult.objects.none()
    serializer_class = TestCaseResultSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_fields = (
        "submission",
        "test_case",
        "status",
    )
    search_fields = (
        "submission__student__username",
        "submission__exercise__title",
        "test_case__name",
    )
    ordering_fields = (
        "execution_time_ms",
        "memory_used_mb",
        "status",
    )
    ordering = ("submission", "test_case")

    def get_queryset(self) -> QuerySet[TestCaseResult]:
        """Вернуть результаты тест-кейсов с учётом роли пользователя."""
        if getattr(self, "swagger_fake_view", False):
            return TestCaseResult.objects.none()

        queryset = TestCaseResult.objects.select_related(
            "submission",
            "submission__student",
            "submission__exercise",
            "test_case",
            "test_case__exercise",
        ).all()

        if is_teacher_or_admin(self.request.user):
            return queryset

        student = cast(User, self.request.user)

        return queryset.filter(submission__student=student)
