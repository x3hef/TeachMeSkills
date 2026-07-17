from typing import Any, cast

import pytest
from rest_framework.test import APIClient

from accounts.models import User
from education.models import Course, Enrollment


@pytest.mark.django_db
def test_course_list_returns_published_courses() -> None:
    """Проверить, что список курсов показывает опубликованные курсы."""
    client = APIClient()
    teacher = create_user(username="education_teacher", role=User.Role.TEACHER)

    Course.objects.create(
        title="Published Python Course",
        description="Visible course.",
        created_by=teacher,
        is_published=True,
    )
    Course.objects.create(
        title="Draft Python Course",
        description="Hidden draft course.",
        created_by=teacher,
        is_published=False,
    )

    response = client.get("/api/courses/")

    assert response.status_code == 200

    response_data = cast(dict[str, Any], response.data)
    results = cast(list[dict[str, Any]], response_data["results"])

    assert len(results) == 1
    assert results[0]["title"] == "Published Python Course"


@pytest.mark.django_db
def test_teacher_can_create_course() -> None:
    """Проверить, что преподаватель может создать курс через API."""
    client = APIClient()
    teacher = create_user(username="course_creator", role=User.Role.TEACHER)
    client.force_authenticate(user=teacher)

    response = client.post(
        "/api/courses/",
        {
            "title": "Teacher Created Course",
            "description": "Course created from API test.",
            "is_published": True,
        },
        format="json",
    )

    assert response.status_code == 201

    course = Course.objects.get(title="Teacher Created Course")

    assert course.created_by == teacher
    assert course.is_published is True


@pytest.mark.django_db
def test_student_cannot_create_course() -> None:
    """Проверить, что обычный ученик не может создавать курсы."""
    client = APIClient()
    student = create_user(username="student_cannot_create")
    client.force_authenticate(user=student)

    response = client.post(
        "/api/courses/",
        {
            "title": "Forbidden Course",
            "description": "Student must not create this.",
            "is_published": True,
        },
        format="json",
    )

    assert response.status_code == 403
    assert not Course.objects.filter(title="Forbidden Course").exists()


@pytest.mark.django_db
def test_student_can_enroll_to_course() -> None:
    """Проверить, что ученик может записаться на курс."""
    client = APIClient()
    teacher = create_user(username="enrollment_teacher", role=User.Role.TEACHER)
    student = create_user(username="enrollment_student")

    course = Course.objects.create(
        title="Enrollment Course",
        description="Course for enrollment test.",
        created_by=teacher,
        is_published=True,
    )

    client.force_authenticate(user=student)

    response = client.post(
        "/api/enrollments/",
        {
            "course": course.id,
            "is_active": True,
        },
        format="json",
    )

    assert response.status_code == 201
    assert Enrollment.objects.filter(student=student, course=course).exists()


def create_user(username: str, role: str = User.Role.STUDENT) -> User:
    """Создать тестового пользователя."""
    return User.objects.create_user(
        username=username,
        email=f"{username}@example.com",
        password="test-password-123",
        role=role,
    )
