from rest_framework.routers import DefaultRouter

from progress.views import ExerciseProgressViewSet, LessonProgressViewSet

router = DefaultRouter()
router.register("lesson-progress", LessonProgressViewSet, basename="lesson-progress")
router.register("exercise-progress", ExerciseProgressViewSet, basename="exercise-progress")

urlpatterns = router.urls
