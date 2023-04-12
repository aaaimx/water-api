from django.contrib import admin
from .models import PredictionClassification, RealClassification, ConsultClassification

# Register your models here.
@admin.register(RealClassification)
class RealClassification(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id',)
    ordering = ('id',)
    search_fields = ('year',)
    list_per_page = 10

@admin.register(PredictionClassification)
class PredictionClassification(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id',)
    ordering = ('id',)
    search_fields = ('year',)
    list_per_page = 10

@admin.register(ConsultClassification)
class ConsultClassification(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id',)
    ordering = ('id',)
    # search_fields = ('year',)
    list_per_page = 10