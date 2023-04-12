from django.shortcuts import render
from .models import CropProduct, SuministryType
from rest_framework import viewsets
from .serializers import CropProductSerializer, SuministryTypeSerializer

# Create your views here.
class CropProductViewSet(viewsets.ModelViewSet):
    queryset = CropProduct.objects.all()
    serializer_class = CropProductSerializer

class SuministryTypeViewSet(viewsets.ModelViewSet):
    queryset = SuministryType.objects.all()
    serializer_class = SuministryTypeSerializer