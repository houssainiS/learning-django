from django.shortcuts import render
from.models import Product
# Create your views here.

def product(request):
    return render(request, 'products/product.html')

def products(request):
    # x = {'pro':Product.objects.all()} #all the products from the database are passed to the products.html template for display
    # x = {'pro':Product.object.get(id=1)} #one product is passed to the products.html template for display with id=1
    pro = Product.objects.all()
    x = {'pro':pro.filter(id=1)}  #one product is passed to the products.html template for display with id=1
    return render(request, 'products/products.html', x)