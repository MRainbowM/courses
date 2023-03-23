from rest_framework.serializers import (
    Serializer,
    IntegerField,
    CharField,
    SerializerMethodField
)

from courses.models import Chapter


class CourseReadOnlySerializer(Serializer):
    id = IntegerField(read_only=True)
    title = CharField(read_only=True)

    chapters = SerializerMethodField(read_only=True)

    def get_chapters(self, obj) -> list:
        сhapters = Chapter.objects.filter(course_id=obj.id).order_by('sort').values(
            'id', 'title'
        )
        return сhapters
