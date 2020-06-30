# coding=utf-8
import logging

from api.repositories.category import CategoryRepository
from api.serializers.category import CategorySerializer
from api.services.service import CommonView, CommonSingleView


_logger = logging.getLogger('api')


class CategoryView(CommonView):
    """
        View to list all categories or create category in the system.
    """
    repository = CategoryRepository
    serializer = CategorySerializer
    fields_filter = ['code']


class CategorySingleView(CommonSingleView):
    """
        View to get/put/delete one category in the system.
    """
    repository = CategoryRepository
    serializer = CategorySerializer
