from rest_framework import permissions, viewsets

from education.models import Course, Lesson, Module
from education.serializers import CourseSerializer, LessonSerializer, ModuleSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Публичный API для просмотра опубликованных курсов."""

    queryset = Course.objects.filter(is_published=True).order_by("title")
    serializer_class = CourseSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_fields = ("is_published",)
    search_fields = ("title", "description")
    ordering_fields = ("title", "created_at", "updated_at")
    ordering = ("title",)


class ModuleViewSet(viewsets.ReadOnlyModelViewSet):
    """Публичный API для просмотра модулей опубликованных курсов."""

    queryset = (
        Module.objects.filter(course__is_published=True)
        .select_related("course")
        .order_by("course__title", "order")
    )
    serializer_class = ModuleSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_fields = ("course",)
    search_fields = ("title", "description", "course__title")
    ordering_fields = ("course__title", "order", "title")
    ordering = ("course__title", "order")


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    """Публичный API для просмотра опубликованных уроков."""

    queryset = (
        Lesson.objects.filter(is_published=True, module__course__is_published=True)
        .select_related("module", "module__course")
        .order_by("module__course__title", "module__order", "order")
    )
    serializer_class = LessonSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_fields = ("module", "module__course", "is_published")
    search_fields = ("title", "content", "module__title", "module__course__title")
    ordering_fields = ("title", "order", "created_at", "updated_at", "module__order")
    ordering = ("module__course__title", "module__order", "order")
