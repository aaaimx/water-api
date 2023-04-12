from django.db import models
from apps.accounts.models import User
from apps.states.models import State

# Create your models here.
class Consult(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_consult = models.DateField()
    lat = models.DecimalField(max_digits=6, decimal_places=4)
    long = models.DecimalField(max_digits=6, decimal_places=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year_consult = models.IntegerField(max_length=4)
    state_consult = models.ForeignKey(State, on_delete=models.CASCADE)