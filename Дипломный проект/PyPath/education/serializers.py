from rest_framework import serializers

from education.models import Course, Enrollment, Lesson, Module


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор курса для API."""

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "is_published",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "slug",
            "created_at",
            "updated_at",
        )


class ModuleSerializer(serializers.ModelSerializer):
    """Сериализатор модуля курса для API."""

    course_title = serializers.CharField(source="course.title", read_only=True)

    class Meta:
        model = Module
        fields = (
            "id",
            "course",
            "course_title",
            "title",
            "description",
            "order",
        )
        read_only_fields = (
            "id",
            "course_title",
        )


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор урока для API."""

    course_title = serializers.CharField(source="module.course.title", read_only=True)
    module_title = serializers.CharField(source="module.title", read_only=True)

    class Meta:
        model = Lesson
        fields = (
            "id",
            "module",
            "module_title",
            "course_title",
            "title",
            "slug",
            "content",
            "order",
            "is_published",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "module_title",
            "course_title",
            "slug",
            "created_at",
            "updated_at",
        )


class EnrollmentSerializer(serializers.ModelSerializer):
    """Сериализатор записи ученика на курс."""

    student_username = serializers.CharField(source="student.username", read_only=True)
    course_title = serializers.CharField(source="course.title", read_only=True)

    class Meta:
        model = Enrollment
        fields = (
            "id",
            "student",
            "student_username",
            "course",
            "course_title",
            "enrolled_at",
            "is_active",
        )
        read_only_fields = (
            "id",
            "student",
            "student_username",
            "course_title",
            "enrolled_at",
        )
        validators: list[object] = []
