from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import * 


router = DefaultRouter()
router.register(r'learners', LearnerViewSet)
router.register(r'subjects', SubjectsViewSet)
router.register(r'grades', GradesViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', index, name='index'),
    path('contact/', contact_view, name='contact'),
    path('student/<int:pk>/', student_info, name='student_info'),
    path('learner/add/', add_learner, name='add_learner'),
    path('grade/add/<int:subject_id>/', add_grade, name='add_grade'),

    path('learner/update/<int:pk>/', update_learner, name='update_learner'),
    path('learner/delete/<int:pk>/', delete_learner, name='delete_learner'),
    path('subject/update/<int:pk>/', update_subject, name='update_subject'),
    path('subject/delete/<int:pk>/', delete_subject, name='delete_subject'),
    path('grade/update/<int:pk>/', update_grade, name='update_grade'),
    path('grade/delete/<int:pk>/', delete_grade, name='delete_grade'),
]

