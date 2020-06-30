# coding=utf-8
import logging

from api.repositories.stock_quant import StockQuantRepository
from api.serializers.stock_quant import StockQuantSerializer
from api.services.service import CommonView, CommonSingleView


_logger = logging.getLogger('api')


class StockQuantView(CommonView):
    """
        View to list all stock_quants or create stock_quant in the system.
    """
    repository = StockQuantRepository
    serializer = StockQuantSerializer
    fields_filter = ['code']


class StockQuantSingleView(CommonSingleView):
    """
        View to get/put/delete one stock_quant in the system.
    """
    repository = StockQuantRepository
    serializer = StockQuantSerializer
