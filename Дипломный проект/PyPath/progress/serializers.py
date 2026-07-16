from rest_framework import serializers

from progress.models import ExerciseProgress, LessonProgress


class LessonProgressSerializer(serializers.ModelSerializer):
    """Сериализатор прогресса ученика по уроку."""

    student_username = serializers.CharField(source="student.username", read_only=True)
    lesson_title = serializers.CharField(source="lesson.title", read_only=True)
    module_title = serializers.CharField(source="lesson.module.title", read_only=True)
    course_title = serializers.CharField(source="lesson.module.course.title", read_only=True)

    class Meta:
        model = LessonProgress
        fields = (
            "id",
            "student",
            "student_username",
            "lesson",
            "lesson_title",
            "module_title",
            "course_title",
            "status",
            "last_opened_at",
            "completed_at",
            "time_spent_seconds",
            "created_at",
            "updated_at",
        )
        read_only_fields = fields


class ExerciseProgressSerializer(serializers.ModelSerializer):
    """Сериализатор прогресса ученика по практическому заданию."""

    student_username = serializers.CharField(source="student.username", read_only=True)
    exercise_title = serializers.CharField(source="exercise.title", read_only=True)
    lesson_title = serializers.CharField(source="exercise.lesson.title", read_only=True)
    course_title = serializers.CharField(source="exercise.lesson.module.course.title", read_only=True)
    best_submission_status = serializers.CharField(source="best_submission.status", read_only=True)

    class Meta:
        model = ExerciseProgress
        fields = (
            "id",
            "student",
            "student_username",
            "exercise",
            "exercise_title",
            "lesson_title",
            "course_title",
            "best_submission",
            "best_submission_status",
            "status",
            "attempts_count",
            "best_score",
            "max_score",
            "last_submitted_at",
            "solved_at",
            "created_at",
            "updated_at",
        )
        read_only_fields = fields
