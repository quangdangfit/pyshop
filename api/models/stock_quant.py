# coding=utf-8
import logging

from django.db import models

from api.models.product import Product


_logger = logging.getLogger('api')


# Create your models here.
class StockQuant(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(null=False, blank=False)

    class Meta:
        db_table = 'stock_quant'
