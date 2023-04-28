from django.db.models import F, Window
from django.db.models.functions import Lead, Lag
from rest_framework.serializers import (
    Serializer,
    IntegerField,
    ValidationError
)

from courses.models import Module, Lesson


class ModuleTemplateSerializer(Serializer):
    module = IntegerField()
    lesson = IntegerField(allow_null=True)

    def validate_module(self, value) -> Module:
        module = Module.objects.filter(id=value).first()

        if module is None:
            raise ValidationError('Модуль не найден')

        return module

    def validate(self, attrs):
        # lesson validate
        lesson_qs = Lesson.objects.filter(
            module_id=attrs['module'].id
        ).annotate(
            next_id=Window(expression=Lead('id'), order_by=F('sort').asc()),
            prev_id=Window(expression=Lag('id'), order_by=F('sort').asc())
        )
        current_lesson = None

        if attrs['lesson'] is None:
            current_lesson = lesson_qs.order_by('sort').first()
        else:
            lessons = list(lesson_qs)
            for lesson in lessons:
                if lesson.id == attrs['lesson']:
                    current_lesson = lesson
                    break

        if current_lesson is None:
            raise ValidationError('Урок не найден')

        attrs['lesson'] = current_lesson

        return attrs
