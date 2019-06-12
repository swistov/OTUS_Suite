from rest_framework import serializers
from app_main.models import Curse, Lesson


class CurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = 'id', 'name', 'descriptions', 'enabled'

    enabled = serializers.BooleanField(required=False, default=False)


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = 'id', 'name', 'curse_name', 'descriptions', 'date_time_release', 'enabled'

    search_fields = ["curse__name"]
    enabled = serializers.BooleanField(required=False, default=False)
