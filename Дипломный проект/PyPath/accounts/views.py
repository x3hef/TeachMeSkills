from typing import cast

from rest_framework import generics, permissions

from accounts.models import User
from accounts.serializers import RegisterSerializer, UserProfileSerializer


class RegisterView(generics.CreateAPIView):
    """API для регистрации нового ученика."""

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)


class CurrentUserView(generics.RetrieveAPIView):
    """API для получения данных текущего пользователя."""

    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self) -> User:
        """Вернуть пользователя, который выполнил текущий API-запрос."""
        return cast(User, self.request.user)
