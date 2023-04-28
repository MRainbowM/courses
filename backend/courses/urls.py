from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    CourseTemplateView,
    ModuleTemplateView
)

urlpatterns = [
    # path('<int:pk>', CourseRetrieveAPI.as_view(), name='retrieve_course_api'),
    path('courses/<int:pk>', CourseTemplateView.as_view(), name='course_template'),
    path('modules/<int:pk>', login_required(ModuleTemplateView.as_view()), name='module_template'),
]
