# coding=utf-8
import logging

from api.models.order import Order
from api.repositories.repository import Repository


_logger = logging.getLogger('api')


class OrderRepository(Repository):
    _name = 'order_repository'
    _model = Order
