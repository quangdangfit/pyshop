# coding=utf-8
import logging

from django.db import models

from api.models.order import Order
from api.models.product import Product


_logger = logging.getLogger('api')


# Create your models here.
class OrderLine(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = 'order_line'
