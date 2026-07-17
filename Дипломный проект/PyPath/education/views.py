from typing import cast

from django.db.models import QuerySet
from rest_framework import mixins, permissions, viewsets
from rest_framework.exceptions import ValidationError

from accounts.models import User
from accounts.permissions import IsReadOnlyOrTeacherOrAdmin, is_teacher_or_admin
from education.models import Course, Enrollment, Lesson, Module
from education.serializers import CourseSerializer, EnrollmentSerializer, LessonSerializer, ModuleSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """API для курсов."""

    serializer_class = CourseSerializer
    permission_classes = (IsReadOnlyOrTeacherOrAdmin,)
    filterset_fields = ("is_published",)
    search_fields = ("title", "description")
    ordering_fields = ("title", "created_at", "updated_at")
    ordering = ("title",)

    def get_queryset(self) -> QuerySet[Course]:
        """Вернуть курсы с учётом роли пользователя."""
        queryset = Course.objects.select_related("created_by").all()

        if is_teacher_or_admin(self.request.user):
            return queryset

        return queryset.filter(is_published=True)

    def perform_create(self, serializer) -> None:
        """Сохранить курс и автоматически указать автора."""
        serializer.save(created_by=self.request.user)


class ModuleViewSet(viewsets.ModelViewSet):
    """API для модулей курса."""

    serializer_class = ModuleSerializer
    permission_classes = (IsReadOnlyOrTeacherOrAdmin,)
    filterset_fields = ("course",)
    search_fields = ("title", "description", "course__title")
    ordering_fields = ("order", "title")
    ordering = ("course", "order")

    def get_queryset(self) -> QuerySet[Module]:
        """Вернуть модули с учётом публикации курса."""
        queryset = Module.objects.select_related("course").all()

        if is_teacher_or_admin(self.request.user):
            return queryset

        return queryset.filter(course__is_published=True)


class LessonViewSet(viewsets.ModelViewSet):
    """API для уроков."""

    serializer_class = LessonSerializer
    permission_classes = (IsReadOnlyOrTeacherOrAdmin,)
    filterset_fields = ("module", "module__course", "is_published")
    search_fields = ("title", "content", "module__title", "module__course__title")
    ordering_fields = ("order", "title", "created_at", "updated_at")
    ordering = ("module", "order")

    def get_queryset(self) -> QuerySet[Lesson]:
        """Вернуть уроки с учётом публикации урока и курса."""
        queryset = Lesson.objects.select_related("module", "module__course").all()

        if is_teacher_or_admin(self.request.user):
            return queryset

        return queryset.filter(
            is_published=True,
            module__course__is_published=True,
        )


class EnrollmentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """API для записей учеников на курсы."""

    queryset = Enrollment.objects.none()
    serializer_class = EnrollmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_fields = ("course", "is_active")
    search_fields = ("student__username", "course__title")
    ordering_fields = ("enrolled_at", "is_active")
    ordering = ("-enrolled_at",)

    def get_queryset(self) -> QuerySet[Enrollment]:
        """Вернуть записи на курсы с учётом роли пользователя."""
        if getattr(self, "swagger_fake_view", False):
            return Enrollment.objects.none()

        queryset = Enrollment.objects.select_related("student", "course").all()

        if is_teacher_or_admin(self.request.user):
            return queryset

        student = cast(User, self.request.user)

        return queryset.filter(student=student)

    def perform_create(self, serializer) -> None:
        """Записать текущего ученика на выбранный курс."""
        student = cast(User, self.request.user)
        course = serializer.validated_data["course"]

        if Enrollment.objects.filter(student=student, course=course).exists():
            raise ValidationError({"course": "Вы уже записаны на этот курс."})

        serializer.save(student=student)
