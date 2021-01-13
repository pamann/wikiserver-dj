from rest_framework import serializers
from .models import node, emoji, userSubmission

class emojiSerializer(serializers.ModelSerializer):
    class Meta:
        model = emoji
        fields = ("id", "title")

class nodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = node
        fields = ("song_id", "title", "_emoji", "channel", "curator", "N", "S", "E", "W", "N_em", "S_em", "E_em", "W_em")
        
class userSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = userSubmission
        fields = ("id", "youtube_link", "youtube_emojis", "user_name", "user_emojis")

    # def create(self, validated_data):
    #     new_sub = userSubmission.objects.create(**validated_data)
    #     return new_sub
