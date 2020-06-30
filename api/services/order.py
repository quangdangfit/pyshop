# coding=utf-8
import logging

from api.repositories.order import OrderRepository
from api.serializers.order import OrderSerializer
from api.services.service import CommonView, CommonSingleView


_logger = logging.getLogger('api')


class OrderView(CommonView):
    """
        View to list all orders or create order in the system.
    """
    repository = OrderRepository
    serializer = OrderSerializer
    fields_filter = ['code']


class OrderSingleView(CommonSingleView):
    """
        View to get/put/delete one order in the system.
    """
    repository = OrderRepository
    serializer = OrderSerializer
