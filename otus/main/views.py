from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from main.models import Curse, Lesson
from main.serializers import CurseSerializer, LessonSerializer, CursePostSerializer


class CurseListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        curses = Curse.objects.all().filter(enabled=True).select_related()
        serializer = CurseSerializer(curses, many=True)
        return Response(serializer.data)


class CurseCreateView(APIView):
    permission_classes = [IsAuthenticated],

    def post(self, request):
        serializer = CursePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurseDetailListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    """
    GET: return curse detail
    POST: reserved curse
    DELETE: delete curse
    TODO: Create new serializer

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
        if request.user.is_staff:
            curse.delete()
        else:
            return Response(data, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        return Response(data, status=status.HTTP_202_ACCEPTED)


class LessonListView(APIView):
    """
    GET: Return enabled list lessons
    pk: Curse ID
    """

    def get(self, request, pk):
        lesson = Lesson.objects.filter(curse=pk, enabled=True).select_related()
        serialize = LessonSerializer(lesson, many=True)
        return Response(serialize.data)


class LessonDetailListView(APIView):

    def get(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        serialize = LessonSerializer(lesson)
        return Response(serialize.data)
