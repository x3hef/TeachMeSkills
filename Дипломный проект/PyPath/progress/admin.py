from django.contrib import admin

from progress.models import ExerciseProgress, LessonProgress


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    """Настройка отображения прогресса по урокам в Django Admin."""

    list_display = (
        "student",
        "course_title",
        "lesson",
        "status",
        "last_opened_at",
        "completed_at",
        "time_spent_seconds",
        "updated_at",
    )
    list_filter = (
        "status",
        "lesson__module__course",
        "lesson__module",
        "last_opened_at",
        "completed_at",
    )
    search_fields = (
        "student__username",
        "student__email",
        "lesson__title",
        "lesson__module__title",
        "lesson__module__course__title",
    )
    list_select_related = (
        "student",
        "lesson",
        "lesson__module",
        "lesson__module__course",
    )
    readonly_fields = ("created_at", "updated_at")
    ordering = (
        "student",
        "lesson__module__course",
        "lesson__module__order",
        "lesson__order",
    )

    @admin.display(description="Курс", ordering="lesson__module__course__title")
    def course_title(self, obj: LessonProgress) -> str:
        """Вернуть название курса, к которому относится урок."""
        return obj.lesson.module.course.title


@admin.register(ExerciseProgress)
class ExerciseProgressAdmin(admin.ModelAdmin):
    """Настройка отображения прогресса по заданиям в Django Admin."""

    list_display = (
        "student",
        "course_title",
        "exercise",
        "status",
        "attempts_count",
        "best_score",
        "max_score",
        "last_submitted_at",
        "solved_at",
        "updated_at",
    )
    list_filter = (
        "status",
        "exercise__lesson__module__course",
        "exercise__lesson",
        "last_submitted_at",
        "solved_at",
    )
    search_fields = (
        "student__username",
        "student__email",
        "exercise__title",
        "exercise__lesson__title",
        "exercise__lesson__module__title",
        "exercise__lesson__module__course__title",
    )
    list_select_related = (
        "student",
        "exercise",
        "exercise__lesson",
        "exercise__lesson__module",
        "exercise__lesson__module__course",
        "best_submission",
    )
    readonly_fields = ("created_at", "updated_at")
    ordering = (
        "student",
        "exercise__lesson__module__course",
        "exercise__lesson__order",
        "exercise__order",
    )

    @admin.display(description="Курс", ordering="exercise__lesson__module__course__title")
    def course_title(self, obj: ExerciseProgress) -> str:
        """Вернуть название курса, к которому относится задание."""
        return obj.exercise.lesson.module.course.title
