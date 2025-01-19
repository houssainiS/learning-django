from django.urls import path
from . import views
from.models import Product

urlpatterns = [
    path('product',views.product, name='product'),
    path('',views.products, name='products'),
]