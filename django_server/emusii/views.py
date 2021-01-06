from django.shortcuts import render
from rest_framework import viewsets
from .serializers import nodeSerializer, emojiSerializer
from .models import node, emoji

class nodeView(viewsets.ModelViewSet):
    queryset = node.objects.all()
    serializer_class = nodeSerializer

class emojiView(viewsets.ModelViewSet):
    queryset = emoji.objects.all()
    serializer_class = emojiSerializer
