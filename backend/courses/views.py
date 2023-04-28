from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.generics import RetrieveAPIView

from basis.settings import DEBUG
from courses.models import Course
from courses.serializers import (
    CourseReadOnlySerializer,
    ModuleReadOnlySerializer,
    LessonReadOnlySerializer,
    ModuleTemplateSerializer
)


class CourseRetrieveAPI(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseReadOnlySerializer


class CourseTemplateView(TemplateView):
    template_name = 'course.html'

    def get(self, request, *args, **kwargs):
        course_id = kwargs['pk']
        course = Course.objects.get(id=course_id)
        course = CourseReadOnlySerializer(instance=course).data

        return render(
            request=request,
            template_name=self.template_name,
            context=course
        )


class ModuleTemplateView(TemplateView):
    template_name = 'module.html'

    def get(self, request, *args, **kwargs):
        serialized = ModuleTemplateSerializer(
            data={
                'module': kwargs['pk'],
                'lesson': request.GET.get('lesson_id', None)
            }
        )

        if serialized.is_valid():
            module = serialized.validated_data.get('module')
            lesson = serialized.validated_data.get('lesson')
        else:
            if bool(DEBUG) is True:
                return HttpResponseNotFound(str(serialized.errors))
            return HttpResponseNotFound('Урок не найден')

        return render(
            request=request,
            template_name=self.template_name,
            context={
                'module': ModuleReadOnlySerializer(instance=module).data,
                'current_lesson': LessonReadOnlySerializer(instance=lesson).data,
            }
        )
