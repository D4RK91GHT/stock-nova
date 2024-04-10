from rest_framework import serializers
from .models import StocksList

class StockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StocksList