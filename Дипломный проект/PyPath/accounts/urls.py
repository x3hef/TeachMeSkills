from django.urls import path

from accounts.views import CurrentUserView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="auth-register"),
    path("me/", CurrentUserView.as_view(), name="auth-me"),
]
