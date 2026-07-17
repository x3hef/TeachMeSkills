from typing import Any, cast

import pytest
from rest_framework.test import APIClient

from accounts.models import User
from assessments.models import Exercise, TestCase as AssessmentTestCase
from education.models import Course, Lesson, Module
from progress.models import ExerciseProgress
from submissions.models import Submission


@pytest.mark.django_db
def test_create_submission_requires_authentication() -> None:
    """Проверить, что отправка решения недоступна без авторизации."""
    client = APIClient()
    exercise = create_exercise(identifier="auth_required")

    response = client.post(
        "/api/submissions/",
        {
            "exercise": exercise.id,
            "code": "print('Hello')",
        },
        format="json",
    )

    assert response.status_code == 401


@pytest.mark.django_db
def test_student_can_create_correct_submission_through_api() -> None:
    """Проверить, что правильное решение через API получает accepted."""
    client = APIClient()
    student = create_user(username="submission_correct_student")
    exercise = create_exercise(identifier="correct")

    client.force_authenticate(user=student)

    response = client.post(
        "/api/submissions/",
        {
            "exercise": exercise.id,
            "code": "a = int(input())\nb = int(input())\nprint(a + b)",
        },
        format="json",
    )

    assert response.status_code == 201

    response_data = cast(dict[str, Any], response.data)

    assert response_data["status"] == Submission.Status.ACCEPTED
    assert response_data["score"] == 10
    assert response_data["passed_tests"] == 2
    assert response_data["total_tests"] == 2

    submission = Submission.objects.get(id=response_data["id"])

    assert submission.student == student
    assert submission.exercise == exercise
    assert submission.status == Submission.Status.ACCEPTED

    progress = ExerciseProgress.objects.get(student=student, exercise=exercise)

    assert progress.attempts_count == 1
    assert progress.best_score == 10
    assert progress.best_submission == submission


@pytest.mark.django_db
def test_student_can_create_wrong_submission_through_api() -> None:
    """Проверить, что неправильное решение через API получает wrong_answer."""
    client = APIClient()
    student = create_user(username="submission_wrong_student")
    exercise = create_exercise(identifier="wrong")

    client.force_authenticate(user=student)

    response = client.post(
        "/api/submissions/",
        {
            "exercise": exercise.id,
            "code": "a = int(input())\nb = int(input())\nprint(a - b)",
        },
        format="json",
    )

    assert response.status_code == 201

    response_data = cast(dict[str, Any], response.data)

    assert response_data["status"] == Submission.Status.WRONG_ANSWER
    assert response_data["score"] == 0
    assert response_data["passed_tests"] == 0
    assert response_data["total_tests"] == 2

    progress = ExerciseProgress.objects.get(student=student, exercise=exercise)

    assert progress.attempts_count == 1
    assert progress.best_score == 0


@pytest.mark.django_db
def test_student_sees_only_own_submissions() -> None:
    """Проверить, что ученик видит только свои отправки решений."""
    client = APIClient()
    first_student = create_user(username="submission_owner")
    second_student = create_user(username="submission_other")
    exercise = create_exercise(identifier="visibility")

    first_submission = Submission.objects.create(
        student=first_student,
        exercise=exercise,
        code="print('first')",
        status=Submission.Status.ACCEPTED,
        score=10,
        max_score=10,
        passed_tests=2,
        total_tests=2,
    )
    Submission.objects.create(
        student=second_student,
        exercise=exercise,
        code="print('second')",
        status=Submission.Status.WRONG_ANSWER,
        score=0,
        max_score=10,
        passed_tests=0,
        total_tests=2,
    )

    client.force_authenticate(user=first_student)

    response = client.get("/api/submissions/")

    assert response.status_code == 200

    response_data = cast(dict[str, Any], response.data)
    results = cast(list[dict[str, Any]], response_data["results"])

    assert len(results) == 1
    assert results[0]["id"] == first_submission.id


def create_exercise(identifier: str) -> Exercise:
    """Создать опубликованное задание с двумя тест-кейсами."""
    teacher = create_user(
        username=f"submission_teacher_{identifier}",
        role=User.Role.TEACHER,
    )

    course = Course.objects.create(
        title=f"Submission Course {identifier}",
        description="Course for submission API test.",
        created_by=teacher,
        is_published=True,
    )
    module = Module.objects.create(
        course=course,
        title=f"Submission Module {identifier}",
        description="Module for submission API test.",
        order=1,
    )
    lesson = Lesson.objects.create(
        module=module,
        title=f"Submission Lesson {identifier}",
        content="Lesson content for submission API test.",
        order=1,
        is_published=True,
    )
    exercise = Exercise.objects.create(
        lesson=lesson,
        title=f"Submission Exercise {identifier}",
        short_description="Submission API exercise.",
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

    AssessmentTestCase.objects.create(
        exercise=exercise,
        name="Simple sum",
        input_data="2\n3",
        expected_output="5",
        is_hidden=False,
        order=1,
        points=5,
    )
    AssessmentTestCase.objects.create(
        exercise=exercise,
        name="Negative sum",
        input_data="-10\n7",
        expected_output="-3",
        is_hidden=True,
        order=2,
        points=5,
    )

    return exercise


def create_user(username: str, role: str = User.Role.STUDENT) -> User:
    """Создать тестового пользователя."""
    return User.objects.create_user(
        username=username,
        email=f"{username}@example.com",
        password="test-password-123",
        role=role,
    )
