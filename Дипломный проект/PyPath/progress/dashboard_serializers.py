from rest_framework import serializers


class DashboardCourseSerializer(serializers.Serializer):
    """Краткая информация о курсе ученика для dashboard."""

    id = serializers.IntegerField()
    title = serializers.CharField()
    slug = serializers.CharField()
    enrolled_at = serializers.DateTimeField()


class DashboardLessonSerializer(serializers.Serializer):
    """Краткая информация о последних открытых уроках."""

    id = serializers.IntegerField()
    title = serializers.CharField()
    course_title = serializers.CharField()
    status = serializers.CharField()
    last_opened_at = serializers.DateTimeField(allow_null=True)
    completed_at = serializers.DateTimeField(allow_null=True)


class DashboardSubmissionSerializer(serializers.Serializer):
    """Краткая информация о последних отправках решений."""

    id = serializers.IntegerField()
    exercise_id = serializers.IntegerField()
    exercise_title = serializers.CharField()
    status = serializers.CharField()
    score = serializers.IntegerField()
    max_score = serializers.IntegerField()
    passed_tests = serializers.IntegerField()
    total_tests = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    checked_at = serializers.DateTimeField(allow_null=True)


class StudentDashboardSerializer(serializers.Serializer):
    """Сводка личного кабинета ученика."""

    student_id = serializers.IntegerField()
    username = serializers.CharField()

    active_courses_count = serializers.IntegerField()
    opened_lessons_count = serializers.IntegerField()
    completed_lessons_count = serializers.IntegerField()
    attempted_exercises_count = serializers.IntegerField()
    solved_exercises_count = serializers.IntegerField()

    submissions_count = serializers.IntegerField()
    accepted_submissions_count = serializers.IntegerField()

    total_best_score = serializers.IntegerField()
    total_max_score = serializers.IntegerField()
    overall_progress_percent = serializers.FloatField()

    active_courses = DashboardCourseSerializer(many=True)
    recent_lessons = DashboardLessonSerializer(many=True)
    recent_submissions = DashboardSubmissionSerializer(many=True)
