from rest_framework import serializers
from main.models import Curse, Lesson


class CurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = ('id', 'name', 'descriptions', 'date_time_release')


class CursePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = ('name', 'descriptions', 'date_time_release', 'enabled')

    enabled = serializers.BooleanField(required=False, default=False)


class LessonSerializer(serializers.ModelSerializer):
    curse_name = serializers.ReadOnlyField(source='curse.name')

    class Meta:
        model = Lesson
        fields = 'id', 'name', 'curse_name', 'descriptions', 'date_time_release'

    # enabled = serializers.BooleanField(required=False, default=False)
