from django.contrib import admin

from submissions.models import Submission, TestCaseResult


class TestCaseResultInline(admin.TabularInline):
    """Встроенное отображение результатов тест-кейсов на странице отправки."""

    model = TestCaseResult
    extra = 0
    fields = (
        "test_case",
        "status",
        "points_awarded",
        "execution_time_ms",
        "memory_used_mb",
        "actual_output",
        "error_message",
    )
    readonly_fields = ("created_at", "updated_at")
    ordering = ("test_case__order",)


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    """Настройка отображения отправок решений в Django Admin."""

    list_display = (
        "id",
        "student",
        "exercise",
        "status",
        "score",
        "max_score",
        "passed_tests",
        "total_tests",
        "created_at",
        "checked_at",
    )
    list_filter = (
        "status",
        "exercise__lesson__module__course",
        "exercise__lesson",
        "created_at",
        "checked_at",
    )
    search_fields = (
        "student__username",
        "student__email",
        "exercise__title",
        "code",
        "error_message",
    )
    list_select_related = (
        "student",
        "exercise",
        "exercise__lesson",
        "exercise__lesson__module",
        "exercise__lesson__module__course",
    )
    readonly_fields = ("created_at", "updated_at", "checked_at")
    ordering = ("-created_at",)
    inlines = (TestCaseResultInline,)


@admin.register(TestCaseResult)
class TestCaseResultAdmin(admin.ModelAdmin):
    """Настройка отображения результатов тест-кейсов в Django Admin."""

    list_display = (
        "submission",
        "test_case",
        "status",
        "points_awarded",
        "execution_time_ms",
        "memory_used_mb",
        "updated_at",
    )
    list_filter = (
        "status",
        "test_case__exercise__lesson__module__course",
        "test_case__exercise",
    )
    search_fields = (
        "submission__student__username",
        "submission__student__email",
        "test_case__exercise__title",
        "actual_output",
        "error_message",
    )
    list_select_related = (
        "submission",
        "submission__student",
        "submission__exercise",
        "test_case",
        "test_case__exercise",
    )
    readonly_fields = ("created_at", "updated_at")
    ordering = ("submission", "test_case__order")
