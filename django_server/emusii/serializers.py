from rest_framework import serializers
from .models import node, emoji

class emojiSerializer(serializers.ModelSerializer):
    class Meta:
        model = emoji
        fields = ("id", "title")

class nodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = node
        fields = ("song_id", "title", "_emoji", "channel", "nav_options")
        