from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'notify')
    list_filter = ('is_staff', 'is_superuser', 'notify')
    fieldsets = UserAdmin.fieldsets + (
        ('Notification settings', {'fields': ('notify',)}),
    )
