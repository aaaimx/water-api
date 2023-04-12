from django.shortcuts import render
from rest_framework import viewsets
from .models import RealClassification, PredictionClassification, ConsultClassification
from .serializers import RCSerializer, PCSerializer, CCSerializer

# Create your views here.
class RCViewSet(viewsets.ModelViewSet):
    queryset = RealClassification.objects.all()
    serializer_class = RCSerializer


class PDViewSet(viewsets.ModelViewSet):
    queryset = PredictionClassification.objects.all()
    serializer_class = PCSerializer

class CCViewSet(viewsets.ModelViewSet):
    queryset = ConsultClassification.objects.all()
    serializer_class = CCSerializer