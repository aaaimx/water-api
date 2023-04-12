from django.db import models

# Create your models here.
class CropProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)

class SuministryType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)