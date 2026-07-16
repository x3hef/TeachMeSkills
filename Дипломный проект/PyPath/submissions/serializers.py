from rest_framework import serializers

from submissions.models import Submission, TestCaseResult


class TestCaseResultSerializer(serializers.ModelSerializer):
    """Сериализатор результата прохождения одного тест-кейса."""

    test_case_name = serializers.CharField(source="test_case.name", read_only=True)
    test_case_is_hidden = serializers.BooleanField(source="test_case.is_hidden", read_only=True)
    input_data = serializers.SerializerMethodField()
    expected_output = serializers.SerializerMethodField()

    class Meta:
        model = TestCaseResult
        fields = (
            "id",
            "test_case",
            "test_case_name",
            "test_case_is_hidden",
            "status",
            "input_data",
            "expected_output",
            "actual_output",
            "error_message",
            "execution_time_ms",
            "memory_used_mb",
            "points_awarded",
            "created_at",
            "updated_at",
        )
        read_only_fields = fields

    def get_input_data(self, obj: TestCaseResult) -> str:
        """Вернуть входные данные только для открытого тест-кейса."""
        if obj.test_case.is_hidden:
            return ""

        return obj.input_data

    def get_expected_output(self, obj: TestCaseResult) -> str:
        """Вернуть ожидаемый вывод только для открытого тест-кейса."""
        if obj.test_case.is_hidden:
            return ""

        return obj.expected_output


class SubmissionSerializer(serializers.ModelSerializer):
    """Сериализатор отправки решения для API."""

    student_username = serializers.CharField(source="student.username", read_only=True)
    exercise_title = serializers.CharField(source="exercise.title", read_only=True)
    test_results = TestCaseResultSerializer(many=True, read_only=True)

    class Meta:
        model = Submission
        fields = (
            "id",
            "student",
            "student_username",
            "exercise",
            "exercise_title",
            "code",
            "status",
            "score",
            "max_score",
            "passed_tests",
            "total_tests",
            "execution_time_ms",
            "memory_used_mb",
            "stdout",
            "stderr",
            "error_message",
            "test_results",
            "created_at",
            "updated_at",
            "checked_at",
        )
        read_only_fields = (
            "id",
            "student",
            "student_username",
            "exercise_title",
            "status",
            "score",
            "max_score",
            "passed_tests",
            "total_tests",
            "execution_time_ms",
            "memory_used_mb",
            "stdout",
            "stderr",
            "error_message",
            "test_results",
            "created_at",
            "updated_at",
            "checked_at",
        )
