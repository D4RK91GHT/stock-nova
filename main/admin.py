from django.contrib import admin
from .models import  *

# Register your models here.
@admin.register(StocksList)
class StockListObject(admin.ModelAdmin):
    list_display = [];