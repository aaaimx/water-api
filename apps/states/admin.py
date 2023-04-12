from django.contrib import admin
from .models import State

# Register your models here.
@admin.register(State)
class State(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id',)
    ordering = ('id',)
    search_fields = ('name',)
    list_per_page = 10
