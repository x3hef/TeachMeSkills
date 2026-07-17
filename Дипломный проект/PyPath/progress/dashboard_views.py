from typing import Any, cast

from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from education.models import Enrollment
from progress.dashboard_serializers import StudentDashboardSerializer
from progress.models import ExerciseProgress, LessonProgress
from submissions.models import Submission


class StudentDashboardView(APIView):
    """API для личного кабинета ученика."""

    permission_classes = (permissions.IsAuthenticated,)

    @extend_schema(
        responses=StudentDashboardSerializer,
        tags=["student-dashboard"],
        summary="Student dashboard",
        description="Вернуть сводку прогресса текущего ученика для личного кабинета.",
    )
    def get(self, request: Request) -> Response:
        """Вернуть dashboard текущего ученика."""
        student = cast(User, request.user)

        active_enrollments = Enrollment.objects.select_related("course").filter(
            student=student,
            is_active=True,
        )

        lesson_progress_queryset = LessonProgress.objects.select_related(
            "lesson",
            "lesson__module",
            "lesson__module__course",
        ).filter(student=student)

        exercise_progress_items = list(
            ExerciseProgress.objects.select_related(
                "exercise",
                "exercise__lesson",
                "exercise__lesson__module",
                "exercise__lesson__module__course",
                "best_submission",
            ).filter(student=student)
        )

        submissions_queryset = Submission.objects.select_related(
            "exercise",
            "exercise__lesson",
        ).filter(student=student)

        active_courses = [
            {
                "id": enrollment.course.id,
                "title": enrollment.course.title,
                "slug": enrollment.course.slug,
                "enrolled_at": enrollment.enrolled_at,
            }
            for enrollment in active_enrollments.order_by("-enrolled_at")[:5]
        ]

        recent_lessons = [
            {
                "id": lesson_progress.lesson.id,
                "title": lesson_progress.lesson.title,
                "course_title": lesson_progress.lesson.module.course.title,
                "status": lesson_progress.status,
                "last_opened_at": lesson_progress.last_opened_at,
                "completed_at": lesson_progress.completed_at,
            }
            for lesson_progress in lesson_progress_queryset.order_by("-last_opened_at")[:5]
        ]

        recent_submissions = [
            {
                "id": submission.id,
                "exercise_id": submission.exercise_id,
                "exercise_title": submission.exercise.title,
                "status": submission.status,
                "score": submission.score,
                "max_score": submission.max_score,
                "passed_tests": submission.passed_tests,
                "total_tests": submission.total_tests,
                "created_at": submission.created_at,
                "checked_at": submission.checked_at,
            }
            for submission in submissions_queryset.order_by("-created_at")[:5]
        ]

        total_best_score = sum(item.best_score for item in exercise_progress_items)
        total_max_score = sum(item.max_score for item in exercise_progress_items)

        solved_exercises_count = sum(
            1 for item in exercise_progress_items if item.max_score > 0 and item.best_score >= item.max_score
        )

        overall_progress_percent = 0.0

        if total_max_score > 0:
            overall_progress_percent = round((total_best_score / total_max_score) * 100, 2)

        dashboard_data: dict[str, Any] = {
            "student_id": student.id,
            "username": student.username,
            "active_courses_count": active_enrollments.count(),
            "opened_lessons_count": lesson_progress_queryset.count(),
            "completed_lessons_count": lesson_progress_queryset.filter(status="completed").count(),
            "attempted_exercises_count": len(exercise_progress_items),
            "solved_exercises_count": solved_exercises_count,
            "submissions_count": submissions_queryset.count(),
            "accepted_submissions_count": submissions_queryset.filter(
                status=Submission.Status.ACCEPTED,
            ).count(),
            "total_best_score": total_best_score,
            "total_max_score": total_max_score,
            "overall_progress_percent": overall_progress_percent,
            "active_courses": active_courses,
            "recent_lessons": recent_lessons,
            "recent_submissions": recent_submissions,
        }

        serializer = StudentDashboardSerializer(dashboard_data)

        return Response(serializer.data)
