from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Настройка отображения пользователей PyPath в Django Admin."""

    list_display = ("username", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")
    search_fields = ("username", "email", "first_name", "last_name")

    fieldsets = tuple(UserAdmin.fieldsets or ()) + (
        (
            "Информация PyPath",
            {
                "fields": ("role",),
            },
        ),
    )

    add_fieldsets = tuple(UserAdmin.add_fieldsets or ()) + (
        (
            "Информация PyPath",
            {
                "fields": ("email", "role"),
            },
        ),
    )
