from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user import serializers

from user.models import OtusUser, Teacher
from user.serializers import OtusUserSerializer, TeacherSerializer


class UserCreateView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.UserSerializer


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            return Response({'token': user.auth_token.key})

        return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class UserInfoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        user = get_object_or_404(OtusUser, pk=pk)
        serializer = OtusUserSerializer(user)
        return Response(serializer.data)

    def post(self, request, pk):
        """
        TODO: Update user info
        """
        user = get_object_or_404(OtusUser, user=pk)
        serializer = OtusUserSerializer(data=request.data)
        if serializer.is_valid():
            user.last_name = request.data['last_name']
            user.phone = request.data['phone']
            user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


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


class UserVerifyView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user = request.GET.get('user', None)
        token = request.GET.get('token', None)

        if not user or not token:
            return Response({'Error': 'You must send user name and token'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = get_object_or_404(User, username=user)
        except:
            return Response({'Error': 'User not register'}, status=status.HTTP_404_NOT_FOUND)

        if user.is_active:
            return Response({'OK': 'User is active'}, status=status.HTTP_202_ACCEPTED)

        user.is_active = True
        user.save()

        return Response({'Apply': 'User activated'}, status=status.HTTP_200_OK)
