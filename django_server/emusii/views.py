from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import nodeSerializer, emojiSerializer
from .models import node, emoji

class nodeView(viewsets.ModelViewSet):
    queryset = node.objects.all()
    serializer_class = nodeSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields =['_emoji']


class emojiView(viewsets.ModelViewSet):
    queryset = emoji.objects.all()
    serializer_class = emojiSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields =['title']
