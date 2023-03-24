from django.urls import path

from .views import (
    CourseTemplateView,
    ChapterTemplateView
)

urlpatterns = [
    # path('<int:pk>', CourseRetrieveAPI.as_view(), name='retrieve_course_api'),
    path('courses/<int:pk>', CourseTemplateView.as_view(), name='course_template'),
    path('modules/<int:pk>', ChapterTemplateView.as_view(), name='module_template'),
]
