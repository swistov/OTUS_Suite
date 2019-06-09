from rest_framework import serializers
from .models import Curse


class CurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = 'id', 'name', 'descriptions', 'enabled'

    enabled = serializers.BooleanField(required=False, default=False)
