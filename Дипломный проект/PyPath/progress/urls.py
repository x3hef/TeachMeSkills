from django.urls import URLPattern, URLResolver, path
from rest_framework.routers import DefaultRouter

from progress.dashboard_views import StudentDashboardView
from progress.views import ExerciseProgressViewSet, LessonProgressViewSet

router = DefaultRouter()
router.register("lesson-progress", LessonProgressViewSet, basename="lesson-progress")
router.register("exercise-progress", ExerciseProgressViewSet, basename="exercise-progress")

urlpatterns: list[URLPattern | URLResolver] = [
    path("student-dashboard/", StudentDashboardView.as_view(), name="student-dashboard"),
    *router.urls,
]
