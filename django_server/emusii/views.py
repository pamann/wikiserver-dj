from django.shortcuts import render
from rest_framework import viewsets
from .serializers import emusiiSerializer
from .models import emusii


class emusiiView(viewsets.ModelViewSet):
    serializer_class = emusiiSerializer
    queryset = emusii.objects.all()
