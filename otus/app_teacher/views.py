from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from app_teacher.models import Teacher
from app_teacher.serializers import TeacherSerializer


class TeacherListView(APIView):

    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)


class TeacherDetailListView(APIView):
    pass
