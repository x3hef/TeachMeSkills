from django.core.management.base import BaseCommand

from accounts.models import User
from assessments.models import Exercise, TestCase
from education.models import Course, Enrollment, Lesson, Module


class Command(BaseCommand):
    """Создать демонстрационные данные для проекта PyPath."""

    help = "Create demo users, courses, lessons, exercises and test cases."

    def handle(self, *args: object, **options: object) -> None:
        """Запустить создание демонстрационных данных."""
        teacher = self.create_demo_teacher()
        student = self.create_demo_student()

        course = self.create_course(teacher)
        module = self.create_module(course)
        lesson_intro = self.create_intro_lesson(module)
        lesson_input = self.create_input_lesson(module)

        hello_exercise = self.create_hello_exercise(lesson_intro)
        sum_exercise = self.create_sum_exercise(lesson_input)

        self.create_hello_test_cases(hello_exercise)
        self.create_sum_test_cases(sum_exercise)
        self.create_enrollment(student, course)

        self.stdout.write(self.style.SUCCESS("Demo data created successfully."))
        self.stdout.write("Teacher login: pypath_teacher / demo12345")
        self.stdout.write("Student login: pypath_student / demo12345")

    def create_demo_teacher(self) -> User:
        """Создать демонстрационного преподавателя."""
        teacher, _created = User.objects.get_or_create(
            username="pypath_teacher",
            defaults={
                "email": "pypath_teacher@example.com",
                "first_name": "Demo",
                "last_name": "Teacher",
                "role": User.Role.TEACHER,
            },
        )
        teacher.email = "pypath_teacher@example.com"
        teacher.first_name = "Demo"
        teacher.last_name = "Teacher"
        teacher.role = User.Role.TEACHER
        teacher.set_password("demo12345")
        teacher.save()

        return teacher

    def create_demo_student(self) -> User:
        """Создать демонстрационного ученика."""
        student, _created = User.objects.get_or_create(
            username="pypath_student",
            defaults={
                "email": "pypath_student@example.com",
                "first_name": "Demo",
                "last_name": "Student",
                "role": User.Role.STUDENT,
            },
        )
        student.email = "pypath_student@example.com"
        student.first_name = "Demo"
        student.last_name = "Student"
        student.role = User.Role.STUDENT
        student.set_password("demo12345")
        student.save()

        return student

    def create_course(self, teacher: User) -> Course:
        """Создать демонстрационный курс Python."""
        course, _created = Course.objects.update_or_create(
            slug="python-basics",
            defaults={
                "title": "Python Basics",
                "description": "Базовый курс по Python для начинающих.",
                "created_by": teacher,
                "is_published": True,
            },
        )

        return course

    def create_module(self, course: Course) -> Module:
        """Создать демонстрационный модуль курса."""
        module, _created = Module.objects.update_or_create(
            course=course,
            order=1,
            defaults={
                "title": "Основы Python",
                "description": "Переменные, вывод, ввод данных и простые вычисления.",
            },
        )

        return module

    def create_intro_lesson(self, module: Module) -> Lesson:
        """Создать урок про первый вывод в Python."""
        lesson, _created = Lesson.objects.update_or_create(
            module=module,
            slug="first-python-program",
            defaults={
                "title": "Первая программа на Python",
                "content": (
                    "В этом уроке ученик знакомится с функцией print " "и пишет первую программу на Python."
                ),
                "order": 1,
                "is_published": True,
            },
        )

        return lesson

    def create_input_lesson(self, module: Module) -> Lesson:
        """Создать урок про ввод данных."""
        lesson, _created = Lesson.objects.update_or_create(
            module=module,
            slug="input-and-numbers",
            defaults={
                "title": "Ввод данных и числа",
                "content": (
                    "В этом уроке ученик использует input, преобразует строки в числа "
                    "и выполняет простые вычисления."
                ),
                "order": 2,
                "is_published": True,
            },
        )

        return lesson

    def create_hello_exercise(self, lesson: Lesson) -> Exercise:
        """Создать задание на вывод текста."""
        exercise, _created = Exercise.objects.update_or_create(
            lesson=lesson,
            slug="print-hello-python",
            defaults={
                "title": "Выведи Hello, Python!",
                "short_description": "Напиши программу, которая выводит Hello, Python!",
                "statement": "Выведи на экран строку: Hello, Python!",
                "difficulty": Exercise.Difficulty.EASY,
                "check_strategy": Exercise.CheckStrategy.STDIN_STDOUT,
                "starter_code": 'print("...")',
                "reference_solution": 'print("Hello, Python!")',
                "order": 1,
                "max_score": 10,
                "time_limit_ms": 1000,
                "memory_limit_mb": 64,
                "is_published": True,
            },
        )

        return exercise

    def create_sum_exercise(self, lesson: Lesson) -> Exercise:
        """Создать задание на сумму двух чисел."""
        exercise, _created = Exercise.objects.update_or_create(
            lesson=lesson,
            slug="sum-two-numbers",
            defaults={
                "title": "Сумма двух чисел",
                "short_description": "Прочитай два числа и выведи их сумму.",
                "statement": ("На вход подаются два целых числа. " "Выведи одно число — их сумму."),
                "difficulty": Exercise.Difficulty.EASY,
                "check_strategy": Exercise.CheckStrategy.STDIN_STDOUT,
                "starter_code": "a = int(input())\nb = int(input())\nprint(...)",
                "reference_solution": "a = int(input())\nb = int(input())\nprint(a + b)",
                "order": 1,
                "max_score": 10,
                "time_limit_ms": 1000,
                "memory_limit_mb": 64,
                "is_published": True,
            },
        )

        return exercise

    def create_hello_test_cases(self, exercise: Exercise) -> None:
        """Создать тесты для задания Hello, Python."""
        TestCase.objects.update_or_create(
            exercise=exercise,
            order=1,
            defaults={
                "name": "Проверка вывода",
                "input_data": "",
                "expected_output": "Hello, Python!",
                "is_hidden": False,
                "points": 10,
            },
        )

    def create_sum_test_cases(self, exercise: Exercise) -> None:
        """Создать тесты для задания на сумму двух чисел."""
        TestCase.objects.update_or_create(
            exercise=exercise,
            order=1,
            defaults={
                "name": "Простой открытый тест",
                "input_data": "2\n3",
                "expected_output": "5",
                "is_hidden": False,
                "points": 5,
            },
        )
        TestCase.objects.update_or_create(
            exercise=exercise,
            order=2,
            defaults={
                "name": "Скрытый тест с отрицательным числом",
                "input_data": "-10\n7",
                "expected_output": "-3",
                "is_hidden": True,
                "points": 5,
            },
        )

    def create_enrollment(self, student: User, course: Course) -> None:
        """Записать демонстрационного ученика на курс."""
        Enrollment.objects.update_or_create(
            student=student,
            course=course,
            defaults={
                "is_active": True,
            },
        )
