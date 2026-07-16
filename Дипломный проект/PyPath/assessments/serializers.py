from rest_framework import serializers

from assessments.models import Exercise, TestCase


class ExerciseSerializer(serializers.ModelSerializer):
    """Сериализатор практического задания для API."""

    course_title = serializers.CharField(source="lesson.module.course.title", read_only=True)
    lesson_title = serializers.CharField(source="lesson.title", read_only=True)

    class Meta:
        model = Exercise
        fields = (
            "id",
            "lesson",
            "lesson_title",
            "course_title",
            "title",
            "slug",
            "short_description",
            "statement",
            "difficulty",
            "check_strategy",
            "starter_code",
            "order",
            "max_score",
            "time_limit_ms",
            "memory_limit_mb",
            "is_published",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "lesson_title",
            "course_title",
            "slug",
            "created_at",
            "updated_at",
        )


class TestCaseSerializer(serializers.ModelSerializer):
    """Сериализатор открытого тест-кейса для API."""

    exercise_title = serializers.CharField(source="exercise.title", read_only=True)

    class Meta:
        model = TestCase
        fields = (
            "id",
            "exercise",
            "exercise_title",
            "name",
            "input_data",
            "expected_output",
            "is_hidden",
            "order",
            "points",
        )
        read_only_fields = ("id", "exercise_title")
