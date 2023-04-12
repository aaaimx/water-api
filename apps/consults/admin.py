from django.contrib import admin
from .models import Consult

# Register your models here.
@admin.register(Consult)
class Consult(admin.ModelAdmin):
    list_display = ('id', 'user', 'year_consult')
    list_filter = ('id',)
    ordering = ('id',)
    search_fields = ('year_consult',)
    list_per_page = 10
