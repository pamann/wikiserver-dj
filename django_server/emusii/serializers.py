from rest_framework import serializers
from .models import emusii, graph, emoji


class emusiiSerializer(serializers.ModelSerializer):
    class Meta:
        model = emusii
        fields = ("id", "title", "emoji")
        
class graphSerializer(serializers.ModelSerializer):
    class Meta:
        model = graph
        fields = ("id", "active", "nodes", "nav_options")

class emojiSerializer(serializers.ModelSerializer):
    class Meta:
        model = emoji
        fields = ("title", "word")