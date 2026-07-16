from django.contrib import admin

from education.models import Course, Enrollment, Lesson, Module


class ModuleInline(admin.TabularInline):
    """Встроенное отображение модулей на странице курса в Django Admin."""

    model = Module
    extra = 0
    fields = ("title", "order", "description")
    ordering = ("order",)


class LessonInline(admin.TabularInline):
    """Встроенное отображение уроков на странице модуля в Django Admin."""

    model = Lesson
    extra = 0
    fields = ("title", "order", "is_published")
    ordering = ("order",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Настройка отображения курсов в Django Admin."""

    list_display = (
        "title",
        "created_by",
        "is_published",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_published", "created_at", "updated_at")
    search_fields = (
        "title",
        "description",
        "created_by__username",
        "created_by__email",
    )
    list_select_related = ("created_by",)
    readonly_fields = ("created_at", "updated_at")
    inlines = (ModuleInline,)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    """Настройка отображения модулей курса в Django Admin."""

    list_display = ("title", "course", "order")
    list_filter = ("course",)
    search_fields = ("title", "description", "course__title")
    list_select_related = ("course",)
    ordering = ("course", "order")
    inlines = (LessonInline,)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Настройка отображения уроков в Django Admin."""

    list_display = (
        "title",
        "course_title",
        "module",
        "order",
        "is_published",
        "updated_at",
    )
    list_filter = ("is_published", "module__course", "module")
    search_fields = ("title", "content", "module__title", "module__course__title")
    list_select_related = ("module", "module__course")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("module__course", "module__order", "order")

    @admin.display(description="Курс", ordering="module__course__title")
    def course_title(self, obj: Lesson) -> str:
        """Вернуть название курса, к которому относится урок."""
        return obj.module.course.title


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    """Настройка отображения записей учеников на курсы в Django Admin."""

    list_display = ("student", "course", "is_active", "enrolled_at")
    list_filter = ("is_active", "course", "enrolled_at")
    search_fields = ("student__username", "student__email", "course__title")
    list_select_related = ("student", "course")
    readonly_fields = ("enrolled_at",)
    ordering = ("-enrolled_at",)
