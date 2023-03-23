from rest_framework.generics import RetrieveAPIView

from courses.models import Course
from courses.serializers import CourseReadOnlySerializer


class CourseRetrieveAPI(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseReadOnlySerializer
