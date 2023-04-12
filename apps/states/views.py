from django.shortcuts import render
from rest_framework import viewsets
from .models import State
from .serializers import StateSerializer

# Create your views here.
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer