# coding=utf-8
import logging

from api.models.stock_quant import StockQuant
from api.repositories.repository import Repository


_logger = logging.getLogger('api')


class StockQuantRepository(Repository):
    _name = 'stock_quant_repository'
    _model = StockQuant
