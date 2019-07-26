from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user import serializers

from user.models import ReservedCurse, OtusUser, Teacher
from user.serializers import ReservedUserCurseSerializer, OtusUserSerializer, TeacherSerializer


class UserCreateView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.UserSerializer


class UserLoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class ReservedUserCurseView(APIView):
    """
    TODO: Reserv curse
    RETURN:
    get: return all reserved user curses
    pk: user_id
    """
    def get(self, request, pk):
        curses = get_object_or_404(ReservedCurse, user=pk)
        serializer = ReservedUserCurseSerializer(curses, many=True)
        return Response(serializer.data)


class ReserveCurseView(APIView):

    def post(self, request, pk):
        user = get_object_or_404(OtusUser, user=request.user)
        curse = get_object_or_404(ReservedCurse, user=user)

        if pk not in [p.id for p in curse.curse.all()]:
            curse.curse.add(pk)
            return Response(status=status.HTTP_201_CREATED)

        return Response(data=f'User {request.user} already reserved this curse',
                        status=status.HTTP_409_CONFLICT)


class UserInfoView(APIView):
    permission_classes = AllowAny,

    def get(self, request, pk):
        user = get_object_or_404(OtusUser, user=pk)
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
