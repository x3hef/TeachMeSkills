from typing import Any

from rest_framework import serializers

from accounts.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    """Сериализатор текущего пользователя для API."""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
            "is_staff",
            "is_superuser",
            "date_joined",
        )
        read_only_fields = fields


class RegisterSerializer(serializers.ModelSerializer):
    """Сериализатор регистрации нового ученика."""

    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
        )
        read_only_fields = ("id",)

    def create(self, validated_data: dict[str, Any]) -> User:
        """Создать нового пользователя с ролью student."""
        password = validated_data.pop("password")

        user = User(**validated_data)
        user.role = User.Role.STUDENT
        user.set_password(str(password))
        user.save()

        return user
