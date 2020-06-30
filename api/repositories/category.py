# coding=utf-8
import logging

from api.models.category import Category
from api.repositories.repository import Repository


_logger = logging.getLogger('api')


class CategoryRepository(Repository):
    _name = 'category_repository'
    _model = Category
