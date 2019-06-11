from rest_framework import serializers
from app_teacher.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = 'id', 'user', 'biography'
