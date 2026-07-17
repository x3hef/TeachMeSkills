import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

from progress.models import ExerciseProgress
from submissions.models import Submission, TestCaseResult


@dataclass(frozen=True)
class CodeRunResult:
    """Результат запуска пользовательского кода на одном тесте."""

    stdout: str
    stderr: str
    execution_time_ms: int
    timed_out: bool
    return_code: int | None


def normalize_output(value: str) -> str:
    """Нормализовать вывод программы для сравнения с ожидаемым ответом."""
    normalized = value.replace("\r\n", "\n").replace("\r", "\n").strip()

    return "\n".join(line.rstrip() for line in normalized.split("\n"))


def run_python_code(code: str, input_data: str, timeout_seconds: float) -> CodeRunResult:
    """Запустить Python-код локально и вернуть результат выполнения."""
    with tempfile.TemporaryDirectory() as temporary_directory:
        solution_path = Path(temporary_directory) / "solution.py"
        solution_path.write_text(code, encoding="utf-8")

        started_at = time.perf_counter()

        try:
            completed_process = subprocess.run(
                [sys.executable, str(solution_path)],
                input=input_data,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout_seconds,
                check=False,
            )
        except subprocess.TimeoutExpired as error:
            execution_time_ms = int((time.perf_counter() - started_at) * 1000)

            return CodeRunResult(
                stdout=str(error.stdout or ""),
                stderr=str(error.stderr or ""),
                execution_time_ms=execution_time_ms,
                timed_out=True,
                return_code=None,
            )

        execution_time_ms = int((time.perf_counter() - started_at) * 1000)

        return CodeRunResult(
            stdout=completed_process.stdout,
            stderr=completed_process.stderr,
            execution_time_ms=execution_time_ms,
            timed_out=False,
            return_code=completed_process.returncode,
        )


def check_submission(submission: Submission) -> Submission:
    """Проверить отправленное решение по тест-кейсам задания."""
    exercise = submission.exercise
    test_cases = list(exercise.test_cases.order_by("order"))

    submission.status = Submission.Status.RUNNING
    submission.error_message = ""
    submission.save(update_fields=("status", "error_message", "updated_at"))

    submission.test_results.all().delete()

    if not test_cases:
        submission.status = Submission.Status.INTERNAL_ERROR
        submission.error_message = "Для задания не настроены тест-кейсы."
        submission.total_tests = 0
        submission.passed_tests = 0
        submission.score = 0
        submission.save(
            update_fields=(
                "status",
                "error_message",
                "total_tests",
                "passed_tests",
                "score",
                "updated_at",
            )
        )

        return submission

    total_score = 0
    passed_tests = 0
    total_execution_time_ms = 0
    final_status = Submission.Status.ACCEPTED
    error_message = ""

    timeout_seconds = exercise.time_limit_ms / 1000

    for test_case in test_cases:
        run_result = run_python_code(
            code=submission.code,
            input_data=test_case.input_data,
            timeout_seconds=timeout_seconds,
        )
        total_execution_time_ms += run_result.execution_time_ms

        actual_output = normalize_output(run_result.stdout)
        expected_output = normalize_output(test_case.expected_output)

        if run_result.timed_out:
            result_status = TestCaseResult.Status.ERROR
            final_status = Submission.Status.TIME_LIMIT_EXCEEDED
            error_message = "Превышен лимит времени выполнения."
        elif run_result.return_code != 0:
            result_status = TestCaseResult.Status.ERROR
            if final_status == Submission.Status.ACCEPTED:
                final_status = Submission.Status.RUNTIME_ERROR
            error_message = run_result.stderr
        elif actual_output == expected_output:
            result_status = TestCaseResult.Status.PASSED
            passed_tests += 1
            total_score += test_case.points
        else:
            result_status = TestCaseResult.Status.FAILED
            if final_status == Submission.Status.ACCEPTED:
                final_status = Submission.Status.WRONG_ANSWER

        TestCaseResult.objects.create(
            submission=submission,
            test_case=test_case,
            status=result_status,
            input_data=test_case.input_data,
            expected_output=test_case.expected_output,
            actual_output=actual_output,
            error_message=run_result.stderr,
            execution_time_ms=run_result.execution_time_ms,
            memory_used_mb=None,
        )

    submission.status = final_status
    submission.score = total_score
    submission.passed_tests = passed_tests
    submission.total_tests = len(test_cases)
    submission.execution_time_ms = total_execution_time_ms
    submission.error_message = error_message
    submission.save(
        update_fields=(
            "status",
            "score",
            "passed_tests",
            "total_tests",
            "execution_time_ms",
            "error_message",
            "updated_at",
        )
    )

    exercise_progress, _created = ExerciseProgress.objects.get_or_create(
        student=submission.student,
        exercise=exercise,
        defaults={
            "max_score": exercise.max_score,
        },
    )
    exercise_progress.register_attempt(submission)

    return submission
