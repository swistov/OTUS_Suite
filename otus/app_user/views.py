from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from app_user import serializers

from app_user.models import ReservedCurse
from app_user.serializers import ReservedUserCurseSerializer


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
    RETURN:
    get: return all reserved user curses
    pk: user_id
    """
    def get(self, request, pk):
        curses = get_object_or_404(ReservedCurse, user=pk)
        serializer = ReservedUserCurseSerializer(curses, many=True)
        return Response(serializer.data)
