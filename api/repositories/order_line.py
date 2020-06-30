# coding=utf-8
import logging

from api.models.order_line import OrderLine
from api.repositories.repository import Repository


_logger = logging.getLogger('api')


class OrderLineRepository(Repository):
    _name = 'order_line_repository'
    _model = OrderLine
