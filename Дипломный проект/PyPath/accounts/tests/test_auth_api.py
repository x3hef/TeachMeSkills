import pytest
from rest_framework.test import APIClient

from accounts.models import User


@pytest.mark.django_db
def test_register_creates_student_user() -> None:
    """Проверить, что регистрация создаёт пользователя с ролью student."""
    client = APIClient()

    response = client.post(
        "/api/auth/register/",
        {
            "username": "new_student",
            "email": "new_student@example.com",
            "password": "strong-password-123",
            "first_name": "New",
            "last_name": "Student",
        },
        format="json",
    )

    assert response.status_code == 201

    user = User.objects.get(username="new_student")

    assert user.email == "new_student@example.com"
    assert user.role == User.Role.STUDENT
    assert user.check_password("strong-password-123")


@pytest.mark.django_db
def test_current_user_requires_authentication() -> None:
    """Проверить, что /api/auth/me/ закрыт без авторизации."""
    client = APIClient()

    response = client.get("/api/auth/me/")

    assert response.status_code == 401


@pytest.mark.django_db
def test_current_user_returns_authenticated_user() -> None:
    """Проверить, что /api/auth/me/ возвращает текущего пользователя."""
    client = APIClient()
    user = User.objects.create_user(
        username="current_student",
        email="current_student@example.com",
        password="test-password-123",
        role=User.Role.STUDENT,
        first_name="Current",
        last_name="Student",
    )

    client.force_authenticate(user=user)

    response = client.get("/api/auth/me/")

    assert response.status_code == 200
    assert response.data["id"] == user.id
    assert response.data["username"] == user.username
    assert response.data["email"] == user.email
    assert response.data["role"] == User.Role.STUDENT
    assert response.data["first_name"] == "Current"
    assert response.data["last_name"] == "Student"
