from django.db import models

# Create your models here.
class State(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    abbreviation = models.CharField(max_length=6)

    def __str__(self):
        return self.name