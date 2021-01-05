from rest_framework import serializers
from .models import node, activesubgraph, emoji, graph


class activesubgraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = activesubgraph
        fields = ("id", "active", "nodes")
        
class graphSerializer(serializers.ModelSerializer):
    class Meta:
        model = graph
        fields = ("id", "graph")

class emojiSerializer(serializers.ModelSerializer):
    class Meta:
        model = emoji
        fields = ("title", "word")

class nodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = node
        fields = ("title", "emoji", "channel", "nav_options")