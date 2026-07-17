from typing import Any

from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from accounts.models import User


def is_teacher_or_admin(user: object) -> bool:
    """Проверить, является ли пользователь преподавателем или администратором."""
    is_admin = bool(getattr(user, "is_staff", False) or getattr(user, "is_superuser", False))

    return is_admin or (isinstance(user, User) and user.is_authenticated and user.role == User.Role.TEACHER)


class IsTeacherOrAdmin(BasePermission):
    """Разрешение только для преподавателей и администраторов."""

    def has_permission(self, request: Request, view: APIView) -> bool:
        """Проверить, может ли пользователь выполнить действие."""
        return is_teacher_or_admin(request.user)


class IsReadOnlyOrTeacherOrAdmin(BasePermission):
    """Чтение разрешено всем, изменение — только преподавателям и администраторам."""

    def has_permission(self, request: Request, view: APIView) -> bool:
        """Проверить доступ к чтению или изменению данных."""
        if request.method in SAFE_METHODS:
            return True

        return is_teacher_or_admin(request.user)


class IsOwnerOrAdmin(BasePermission):
    """Разрешение только владельцу объекта или администратору."""

    def has_object_permission(self, request: Request, view: APIView, obj: Any) -> bool:
        """Проверить доступ к конкретному объекту."""
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if user.is_staff or user.is_superuser:
            return True

        owner = getattr(obj, "student", None)

        return owner == user
