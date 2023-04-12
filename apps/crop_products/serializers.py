from rest_framework import serializers
from .models import CropProduct, SuministryType

class CropProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropProduct
        fields = '__all__'

class SuministryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuministryType