from rest_framework.routers import DefaultRouter
from .views import LearnerViewSet, SubjectsViewSet, GradesViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'learners', LearnerViewSet)
router.register(r'subjects', SubjectsViewSet)
router.register(r'grades', GradesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
