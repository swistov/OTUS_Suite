from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from main.validations import send_validation_message
from user.models import OtusUser, Teacher
from main.models import Curse


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        TODO: Edit 'is_authenticated' -> False
        :param validated_data:
        :return: user
        """
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()
        Token.objects.create(user=user)
        send_validation_message(user.username)
        return user


class ReservedUserCurseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curse
        fields = 'id', 'curse_name', 'reserved_date_time'

    search_fields = ["curse_name"]


class ReservedCurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = ('user', 'curse')


class OtusUserSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')

    class Meta:
        model = OtusUser
        fields = ('id', 'last_name', 'first_name', 'phone')


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = 'id', 'user', 'biography'
