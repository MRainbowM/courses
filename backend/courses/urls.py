from django.urls import path

from .views import (
    CourseRetrieveAPI,
    CourseTemplateView
)

urlpatterns = [
    # path('<int:pk>', CourseRetrieveAPI.as_view(), name='retrieve_course_api'),
    path('courses/<int:pk>', CourseTemplateView.as_view(), name='course_template'),
]
