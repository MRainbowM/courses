from django.db.models.query import QuerySet
from rest_framework.serializers import (
    Serializer,
    IntegerField,
    CharField,
    SerializerMethodField
)

from courses.models import Course


class ChapterReadOnlySerializer(Serializer):
    id = IntegerField(read_only=True)
    title = CharField(read_only=True)
    # course_id = IntegerField(read_only=True)

    course = SerializerMethodField(read_only=True)

    def get_course(self, obj) -> QuerySet:
        course = Course.objects.values(
            'id', 'title'
        ).get(id=obj.course_id)

        return course
