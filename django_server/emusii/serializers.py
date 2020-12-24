from rest_framework import serializers
from .models import emusii


class emusiiSerializer(serializers.ModelSerializer):
    class Meta:
        model = emusii
        fields = ("id", "title", "emoji")
