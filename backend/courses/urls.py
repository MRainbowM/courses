from django.urls import path

from .views import CourseRetrieveAPI

urlpatterns = [
    path('<int:pk>', CourseRetrieveAPI.as_view(), name='retrieve_course_api'),
]
