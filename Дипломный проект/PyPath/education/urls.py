from rest_framework.routers import DefaultRouter

from education.views import CourseViewSet, EnrollmentViewSet, LessonViewSet, ModuleViewSet

router = DefaultRouter()
router.register("courses", CourseViewSet, basename="course")
router.register("modules", ModuleViewSet, basename="module")
router.register("lessons", LessonViewSet, basename="lesson")
router.register("enrollments", EnrollmentViewSet, basename="enrollment")

urlpatterns = router.urls
