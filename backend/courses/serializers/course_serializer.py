from django.db.models.query import QuerySet
from rest_framework.serializers import (
    Serializer,
    IntegerField,
    CharField,
    SerializerMethodField
)

from courses.models import Module


class CourseReadOnlySerializer(Serializer):
    id = IntegerField(read_only=True)
    title = CharField(read_only=True)

    modules = SerializerMethodField(read_only=True)

    def get_modules(self, obj) -> QuerySet:
        modules = Module.objects.filter(course_id=obj.id).order_by('sort').values(
            'id', 'title'
        )
        return modules
