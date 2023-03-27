from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.generics import RetrieveAPIView

from courses.models import Course, Module, Lesson
from courses.serializers import CourseReadOnlySerializer, ModuleReadOnlySerializer, LessonReadOnlySerializer


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
        module_id = kwargs['pk']
        lesson_id = request.GET.get('lesson_id', None)

        module = Module.objects.get(id=module_id)

        if lesson_id is None:
            lesson = Lesson.objects.filter(
                module_id=module_id
            ).order_by('sort').first()
        else:
            lesson = Lesson.objects.filter(
                module_id=module_id,
                id=lesson_id
            ).first()

        # TODO: return 404 if lesson is None

        return render(
            request=request,
            template_name=self.template_name,
            context={
                'module': ModuleReadOnlySerializer(instance=module).data,
                'current_lesson': LessonReadOnlySerializer(instance=lesson).data,
            }
        )
