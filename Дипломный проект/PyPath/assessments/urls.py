from rest_framework.routers import DefaultRouter

from assessments.views import ExerciseViewSet, TestCaseViewSet

router = DefaultRouter()
router.register("exercises", ExerciseViewSet, basename="exercise")
router.register("test-cases", TestCaseViewSet, basename="test-case")

urlpatterns = router.urls
