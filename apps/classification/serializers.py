from rest_framework import serializers
from .models import PredictionClassification, RealClassification, ConsultClassification

class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionClassification
        fields = '__all__'

class RCSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealClassification
        fields = '__all__'

class CCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultClassification
        fields = '__all__'