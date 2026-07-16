from rest_framework.routers import DefaultRouter

from submissions.views import SubmissionViewSet, TestCaseResultViewSet

router = DefaultRouter()
router.register("submissions", SubmissionViewSet, basename="submission")
router.register("test-case-results", TestCaseResultViewSet, basename="test-case-result")

urlpatterns = router.urls
