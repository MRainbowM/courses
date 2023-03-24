from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.generics import RetrieveAPIView

from courses.models import Course, Module
from courses.serializers import CourseReadOnlySerializer, ModuleReadOnlySerializer


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


class ChapterTemplateView(TemplateView):
    template_name = 'chapter.html'

    def get(self, request, *args, **kwargs):
        chapter_id = kwargs['pk']
        chapter = Module.objects.get(id=chapter_id)

        chapter = ModuleReadOnlySerializer(instance=chapter).data

        return render(
            request=request,
            template_name=self.template_name,
            context=chapter
        )
