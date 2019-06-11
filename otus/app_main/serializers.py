from rest_framework import serializers
from app_main.models import Curse


class CurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = 'id', 'name', 'descriptions', 'enabled'

    enabled = serializers.BooleanField(required=False, default=False)
