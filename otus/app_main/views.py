from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from app_main.models import Curse, Lesson
from app_main.serializers import CurseSerializer, LessonSerializer
from app_user.models import ReservedCurse
from app_user.serializers import ReservedCurseSerializer


def index_app_main(request):
    return HttpResponse('<h1>Hello to curse</h1>')


class CurseListView(APIView):

    def get(self, request):
        curses = Curse.objects.all().filter(enabled=True)
        serializer = CurseSerializer(curses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CurseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurseDetailListView(APIView):
    """
    GET: return curse detail
    POST: reserved curse
    """

    def get(self, request, pk):
        curse = get_object_or_404(Curse, pk=pk)
        serializer = CurseSerializer(curse)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = ReservedCurseSerializer(data=request.data)

        if serializer.is_valid():
            if ReservedCurse.objects.filter(curse=pk,
                                            user=request.data.get('user')
                                            ).exists():
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        curse = get_object_or_404(Curse, pk=pk)
        serializer = CurseSerializer(curse)
        data = serializer.data
        curse.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)


class LessonListView(APIView):
    """
    GET: Return enabled list lessons
    pk: Curse ID
    """

    def get(self, request, pk):
        lesson = Lesson.objects.filter(curse=pk, enabled=True)
        serialize = LessonSerializer(lesson, many=True)
        return Response(serialize.data)


class LessonDetailListView(APIView):

    def get(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        serialize = LessonSerializer(lesson)
        return Response(serialize.data)
