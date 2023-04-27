from django.db.models import F, Window
from django.db.models.functions import Lead, Lag
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
        lesson_id = int(request.GET.get('lesson_id', None))
        # TODO: validate params

        module = Module.objects.get(id=module_id)

        lesson_qs = Lesson.objects.filter(
            module_id=module_id
        ).annotate(
            next_id=Window(
                expression=Lead('id'),
                order_by=F('sort').asc()
            ),
            prev_id=Window(
                expression=Lag('id'),
                order_by=F('sort').asc(),
            ),
        )
        current_lesson = None

        if lesson_id is None:
            current_lesson = lesson_qs.order_by('sort').first()

        else:
            lessons = list(lesson_qs)
            for lesson in lessons:
                if lesson.id == lesson_id:
                    current_lesson = lesson
                    break

        if current_lesson is None:
            print()
            # TODO: return 404 if lesson is None

        current_lesson = LessonReadOnlySerializer(instance=current_lesson).data
        print(current_lesson)
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'module': ModuleReadOnlySerializer(instance=module).data,
                'current_lesson': current_lesson,
            }
        )
