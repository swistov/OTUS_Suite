from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Curse
from .serializers import CurseSerializer


def index_appmain(request):
    return HttpResponse('<h1>Hello to curse</h1>')


class CurseListView(APIView):

    def get(self, request):
        curses = Curse.objects.all()
        serializer = CurseSerializer(curses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CurseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurseDetailListView(APIView):

    def get(self, request, pk):
        curse = get_object_or_404(Curse, pk=pk)
        serializer = CurseSerializer(curse)
        return Response(serializer.data)

    def delete(self, request, pk):
        curse = get_object_or_404(Curse, pk=pk)
        serializer = CurseSerializer(curse)
        data = serializer.data
        curse.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)