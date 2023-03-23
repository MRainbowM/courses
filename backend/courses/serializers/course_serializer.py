from rest_framework.serializers import (
    Serializer,
    IntegerField,
    CharField
)


class CourseReadOnlySerializer(Serializer):
    id = IntegerField(read_only=True)
    title = CharField(read_only=True)
