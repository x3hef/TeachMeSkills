from django.contrib import admin

from assessments.models import Exercise, TestCase


class TestCaseInline(admin.TabularInline):
    """Встроенное отображение тест-кейсов на странице задания."""

    model = TestCase
    extra = 0
    fields = (
        "name",
        "order",
        "is_hidden",
        "points",
        "input_data",
        "expected_output",
    )
    ordering = ("order",)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    """Настройка отображения практических заданий в Django Admin."""

    list_display = (
        "title",
        "course_title",
        "lesson",
        "difficulty",
        "check_strategy",
        "order",
        "max_score",
        "is_published",
        "updated_at",
    )
    list_filter = (
        "difficulty",
        "check_strategy",
        "is_published",
        "lesson__module__course",
        "lesson",
    )
    search_fields = (
        "title",
        "short_description",
        "statement",
        "lesson__title",
        "lesson__module__title",
        "lesson__module__course__title",
    )
    list_select_related = (
        "lesson",
        "lesson__module",
        "lesson__module__course",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    ordering = (
        "lesson__module__course",
        "lesson__module__order",
        "lesson__order",
        "order",
    )
    inlines = (TestCaseInline,)

    @admin.display(description="Курс", ordering="lesson__module__course__title")
    def course_title(self, obj: Exercise) -> str:
        """Вернуть название курса, к которому относится задание."""
        return obj.lesson.module.course.title


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    """Настройка отображения тест-кейсов в Django Admin."""

    list_display = (
        "exercise",
        "name",
        "order",
        "is_hidden",
        "points",
        "updated_at",
    )
    list_filter = (
        "is_hidden",
        "exercise__lesson__module__course",
        "exercise__lesson",
    )
    search_fields = (
        "name",
        "input_data",
        "expected_output",
        "exercise__title",
        "exercise__lesson__title",
    )
    list_select_related = (
        "exercise",
        "exercise__lesson",
        "exercise__lesson__module",
        "exercise__lesson__module__course",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    ordering = (
        "exercise",
        "order",
    )
