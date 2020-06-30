# coding=utf-8
import logging

from django.db import models


_logger = logging.getLogger('api')


# Create your models here.
class Order(models.Model):
    code = models.CharField(max_length=15, unique=True, null=False, blank=False)

    class Meta:
        db_table = 'order'
