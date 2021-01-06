from django.shortcuts import render
from rest_framework import viewsets
from .serializers import nodeSerializer, emojiSerializer, activesubgraphSerializer, graphSerializer
from .models import node, emoji, activesubgraph, graph



class nodeView(viewsets.ModelViewSet):
    queryset = node.objects.all()
    serializer_class = nodeSerializer

class graphView(viewsets.ModelViewSet):
    queryset = graph.objects.all()
    serializer_class = graphSerializer

class emojiView(viewsets.ModelViewSet):
    queryset = emoji.objects.all()
    serializer_class = emojiSerializer

class activesubgraphView(viewsets.ModelViewSet):
    queryset = activesubgraph.objects.all()
    serializer_class = activesubgraphSerializer

