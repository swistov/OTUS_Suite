from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from user.models import OtusUser, Teacher


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

"""
Rename serializers
"""
# class ReservedUserCurseSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = ReservedCurse
#         fields = 'id', 'curse_name', 'reserved_date_time'
#
#     search_fields = ["curse_name"]
#
#
# class ReservedCurseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ReservedCurse
#         fields = ('user', 'curse')


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
