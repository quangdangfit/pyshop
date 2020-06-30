# coding=utf-8

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.services.product import ProductView, ProductSingleView
from api.services.category import CategoryView, CategorySingleView
from api.services.order import OrderView, OrderSingleView
from api.services.stock_quant import StockQuantView, StockQuantSingleView


urlpatterns = [
    path('/products', ProductView.as_view()),
    path('/products/<int:record_id>', ProductSingleView.as_view()),

    path('/categories', CategoryView.as_view()),
    path('/categories/<int:record_id>', CategorySingleView.as_view()),

    path('/orders', OrderView.as_view()),
    path('/orders/<int:record_id>', OrderSingleView.as_view()),

    path('/stock_quants', StockQuantView.as_view()),
    path('/stock_quants/<int:record_id>', StockQuantSingleView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
