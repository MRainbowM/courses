from rest_framework.serializers import (
    Serializer,
    IntegerField,
    CharField
)


class LessonReadOnlySerializer(Serializer):
    id = IntegerField(read_only=True)
    prev_id = IntegerField(read_only=True)
    next_id = IntegerField(read_only=True)
    title = CharField(read_only=True)
    text = CharField(read_only=True)
    video_url = CharField(read_only=True)
