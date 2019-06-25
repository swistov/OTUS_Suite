from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from teacher.models import Teacher
from teacher.serializers import TeacherSerializer


class TeacherListView(APIView):

    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)


class TeacherDetailListView(APIView):

    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
