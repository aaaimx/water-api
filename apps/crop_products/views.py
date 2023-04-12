from django.http import JsonResponse
from django.shortcuts import render
from requests import Response
from rest_framework.decorators import action
from .models import CropProduct, SuministryType
from rest_framework import viewsets
from .serializers import CropProductSerializer, SuministryTypeSerializer

# Create your views here.
class CropProductViewSet(viewsets.ModelViewSet):
    queryset = CropProduct.objects.all()
    serializer_class = CropProductSerializer

    @action(detail=False, methods=['POST'])
    def load_products(self, request, *args, **kwargs):
        array = request.data.get('productos')
        for item in array:
            print(item)
        return Response({'list': item})

class SuministryTypeViewSet(viewsets.ModelViewSet):
    queryset = SuministryType.objects.all()
    serializer_class = SuministryTypeSerializer