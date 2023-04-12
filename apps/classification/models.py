from django.db import models
from apps.crop_products.models import SuministryType, CropProduct
from apps.states.models import State

# Create your models here.
class RealClassification(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.IntegerField(max_length=4)
    mm = models.DecimalField(max_digits=5, decimal_places=2)
    av = models.DecimalField(max_digits=6, decimal_places=4)
    hh = models.DecimalField(max_digits=6, decimal_places=4)
    ca = models.DecimalField(max_digits=6, decimal_places=4)
    temp = models.DecimalField(max_digits=6, decimal_places=2)

class PredictionClassification(models.Model):
    id = models.BigAutoField(primary_key=True)
    mm_predict = models.DecimalField(max_digits=5, decimal_places=2)
    av_predict = models.DecimalField(max_digits=6, decimal_places=4)
    hh_predict = models.DecimalField(max_digits=6, decimal_places=4)
    temp_predict = models.DecimalField(max_digits=6, decimal_places=2)
    tons_predict = models.DecimalField(max_digits=6, decimal_places=2)

class ConsultClassification(models.Model):
    id = models.BigAutoField(primary_key=True)
    classification = models.ForeignKey(RealClassification, on_delete=models.CASCADE)
    sum_type = models.ForeignKey(SuministryType, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    crop_product = models.ForeignKey(CropProduct, on_delete=models.CASCADE)