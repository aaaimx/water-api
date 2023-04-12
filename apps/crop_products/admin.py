from django.contrib import admin
from .models import CropProduct, SuministryType

# Register your models here.
@admin.register(CropProduct)
class CropProduct(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id',)
    ordering = ('id',)
    search_fields = ('name',)
    list_per_page = 10

class SuministryType(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id',)
    ordering = ('id',)
    search_fields = ('name',)
    list_per_page = 10