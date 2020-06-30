# coding=utf-8
from rest_framework import serializers

from api.models.stock_quant import StockQuant


class StockQuantSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockQuant
        fields = ['product_id.code', 'product_id.name', 'quantity']
