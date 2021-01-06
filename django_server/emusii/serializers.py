from rest_framework import serializers
from .models import node, emoji

class emojiSerializer(serializers.ModelSerializer):
    class Meta:
        model = emoji
        fields = ("id", "emoji")

class nodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = node
        fields = ("id", "song", "title", "emoji", "channel", "nav_options")
        