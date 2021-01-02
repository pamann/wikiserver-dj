from django.shortcuts import render
from rest_framework import viewsets
from .serializers import emusiiSerializer, graphSerializer, emojiSerializer
from .models import emusii, graph, emoji



class emusiiView(viewsets.ModelViewSet):
    queryset = emusii.objects.all()
    serializer_class = emusiiSerializer

class graphView(viewsets.ModelViewSet):
    queryset = graph.objects.all()
    serializer_class = graphSerializer

class emojiView(viewsets.ModelViewSet):
    queryset = emoji.objects.all()
    serializer_class = emojiSerializer