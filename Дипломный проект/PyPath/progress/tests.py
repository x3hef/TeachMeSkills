from typing import Any, cast

import pytest
from django.utils import timezone
from rest_framework.test import APIClient

from accounts.models import User
from assessments.models import Exercise
from education.models import Course, Enrollment, Lesson, Module
from progress.models import ExerciseProgress, LessonProgress
from submissions.models import Submission


@pytest.mark.django_db
def test_student_dashboard_requires_authentication() -> None:
    """Проверить, что dashboard недоступен без авторизации."""
    client = APIClient()

    response = client.get("/api/student-dashboard/")

    assert response.status_code == 401


@pytest.mark.django_db
def test_student_dashboard_returns_current_student_summary() -> None:
    """Проверить, что dashboard возвращает сводку текущего ученика."""
    client = APIClient()
    student = create_user(username="dashboard_student")
    teacher = create_user(username="dashboard_teacher", role=User.Role.TEACHER)

    course = Course.objects.create(
        title="Dashboard Python Course",
        description="Course for dashboard API test.",
        created_by=teacher,
        is_published=True,
    )
    module = Module.objects.create(
        course=course,
        title="Dashboard Module",
        description="Module for dashboard API test.",
        order=1,
    )
    lesson = Lesson.objects.create(
        module=module,
        title="Dashboard Lesson",
        content="Lesson content for dashboard API test.",
        order=1,
        is_published=True,
    )
    exercise = Exercise.objects.create(
        lesson=lesson,
        title="Dashboard Exercise",
        short_description="Exercise for dashboard API test.",
        statement="Read two numbers and print their sum.",
        difficulty=Exercise.Difficulty.EASY,
        check_strategy=Exercise.CheckStrategy.STDIN_STDOUT,
        starter_code="a = int(input())\nb = int(input())\nprint(...)",
        reference_solution="a = int(input())\nb = int(input())\nprint(a + b)",
        order=1,
        max_score=10,
        time_limit_ms=1000,
        memory_limit_mb=64,
        is_published=True,
    )

    Enrollment.objects.create(
        student=student,
        course=course,
        is_active=True,
    )

    lesson_progress = LessonProgress.objects.create(
        student=student,
        lesson=lesson,
    )
    lesson_progress.mark_completed()

    submission = Submission.objects.create(
        student=student,
        exercise=exercise,
        code="a = int(input())\nb = int(input())\nprint(a + b)",
        status=Submission.Status.ACCEPTED,
        score=10,
        max_score=10,
        passed_tests=2,
        total_tests=2,
        checked_at=timezone.now(),
    )

    ExerciseProgress.objects.create(
        student=student,
        exercise=exercise,
        best_submission=submission,
        attempts_count=1,
        best_score=10,
        max_score=10,
        last_submitted_at=submission.created_at,
    )

    client.force_authenticate(user=student)

    response = client.get("/api/student-dashboard/")

    assert response.status_code == 200

    response_data = cast(dict[str, Any], response.data)

    assert response_data["student_id"] == student.id
    assert response_data["username"] == student.username
    assert response_data["active_courses_count"] == 1
    assert response_data["opened_lessons_count"] == 1
    assert response_data["completed_lessons_count"] == 1
    assert response_data["attempted_exercises_count"] == 1
    assert response_data["solved_exercises_count"] == 1
    assert response_data["submissions_count"] == 1
    assert response_data["accepted_submissions_count"] == 1
    assert response_data["total_best_score"] == 10
    assert response_data["total_max_score"] == 10
    assert response_data["overall_progress_percent"] == 100.0

    assert response_data["active_courses"][0]["title"] == course.title
    assert response_data["recent_lessons"][0]["title"] == lesson.title
    assert response_data["recent_submissions"][0]["exercise_title"] == exercise.title
    assert response_data["recent_submissions"][0]["status"] == Submission.Status.ACCEPTED


def create_user(username: str, role: str = User.Role.STUDENT) -> User:
    """Создать тестового пользователя."""
    return User.objects.create_user(
        username=username,
        email=f"{username}@example.com",
        password="test-password-123",
        role=role,
    )
