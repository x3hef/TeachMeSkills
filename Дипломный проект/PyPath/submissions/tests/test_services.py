import pytest

from accounts.models import User
from assessments.models import Exercise
from assessments.models import TestCase as AssessmentTestCase
from education.models import Course, Lesson, Module
from progress.models import ExerciseProgress
from submissions.models import Submission
from submissions.models import TestCaseResult as SubmissionTestCaseResult
from submissions.services import check_submission, normalize_output


@pytest.mark.django_db
def test_normalize_output_removes_extra_spaces_and_line_endings() -> None:
    """Проверить нормализацию вывода программы."""
    assert normalize_output("Hello   \r\nPython\n\n") == "Hello\nPython"


@pytest.mark.django_db
def test_check_submission_accepts_correct_solution() -> None:
    """Проверить, что правильное решение получает статус accepted."""
    student = create_user(username="student_correct")
    exercise = create_sum_exercise()

    submission = Submission.objects.create(
        student=student,
        exercise=exercise,
        code="a = int(input())\nb = int(input())\nprint(a + b)",
        max_score=exercise.max_score,
        total_tests=exercise.test_cases.count(),
    )

    checked_submission = check_submission(submission)

    assert checked_submission.status == Submission.Status.ACCEPTED
    assert checked_submission.score == 10
    assert checked_submission.passed_tests == 2
    assert checked_submission.total_tests == 2
    assert SubmissionTestCaseResult.objects.filter(submission=submission).count() == 2

    progress = ExerciseProgress.objects.get(student=student, exercise=exercise)
    assert progress.attempts_count == 1
    assert progress.best_score == 10
    assert progress.best_submission == submission


@pytest.mark.django_db
def test_check_submission_marks_wrong_answer() -> None:
    """Проверить, что неправильное решение получает статус wrong_answer."""
    student = create_user(username="student_wrong")
    exercise = create_sum_exercise()

    submission = Submission.objects.create(
        student=student,
        exercise=exercise,
        code="a = int(input())\nb = int(input())\nprint(a - b)",
        max_score=exercise.max_score,
        total_tests=exercise.test_cases.count(),
    )

    checked_submission = check_submission(submission)

    assert checked_submission.status == Submission.Status.WRONG_ANSWER
    assert checked_submission.score == 0
    assert checked_submission.passed_tests == 0
    assert checked_submission.total_tests == 2
    assert SubmissionTestCaseResult.objects.filter(submission=submission).count() == 2

    progress = ExerciseProgress.objects.get(student=student, exercise=exercise)
    assert progress.attempts_count == 1
    assert progress.best_score == 0


def create_user(username: str) -> User:
    """Создать тестового ученика."""
    return User.objects.create_user(
        username=username,
        email=f"{username}@example.com",
        password="test-password-123",
        role=User.Role.STUDENT,
    )


def create_teacher(username: str = "teacher_for_service_test") -> User:
    """Создать тестового преподавателя."""
    return User.objects.create_user(
        username=username,
        email=f"{username}@example.com",
        password="test-password-123",
        role=User.Role.TEACHER,
    )


def create_sum_exercise() -> Exercise:
    """Создать тестовое задание на сумму двух чисел."""
    teacher = create_teacher()
    course = Course.objects.create(
        title="Test Python Course",
        description="Test course description.",
        created_by=teacher,
        is_published=True,
    )
    module = Module.objects.create(
        course=course,
        title="Test Module",
        description="Test module description.",
        order=1,
    )
    lesson = Lesson.objects.create(
        module=module,
        title="Test Lesson",
        content="Test lesson content.",
        order=1,
        is_published=True,
    )
    exercise = Exercise.objects.create(
        lesson=lesson,
        title="Sum two numbers",
        short_description="Read two numbers and print their sum.",
        statement="Read two integers and print their sum.",
        difficulty=Exercise.Difficulty.EASY,
        check_strategy=Exercise.CheckStrategy.STDIN_STDOUT,
        starter_code="a = int(input())\nb = int(input())\nprint(...)",
        reference_solution="a = int(input())\nb = int(input())\nprint(a + b)",
        order=1,
        max_score=10,
        time_limit_ms=1000,
        memory_limit_mb=64,
        is_published=True,
    )

    AssessmentTestCase.objects.create(
        exercise=exercise,
        name="Simple test",
        input_data="2\n3",
        expected_output="5",
        is_hidden=False,
        order=1,
        points=5,
    )
    AssessmentTestCase.objects.create(
        exercise=exercise,
        name="Negative number test",
        input_data="-10\n7",
        expected_output="-3",
        is_hidden=True,
        order=2,
        points=5,
    )

    return exercise
