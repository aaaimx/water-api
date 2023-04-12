from django.shortcuts import render
from rest_framework import viewsets
from .models import RealClassification, PredictionClassification
from .serializers import RCSerializer, PCSerializer

# Create your views here.
class RCViewSet(viewsets.ModelViewSet):
    queryset = RealClassification.objects.all()
    serializer_class = RCSerializer


class PDViewSet(viewsets.ModelViewSet):
    queryset = PredictionClassification.objects.all()
    serializer_class = PCSerializer