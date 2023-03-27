from rest_framework.serializers import (
    Serializer,
    IntegerField,
    CharField
)


class LessonReadOnlySerializer(Serializer):
    id = IntegerField(read_only=True)
    title = CharField(read_only=True)
    text = CharField(read_only=True)
