from django.shortcuts import render
from.models import Product
# Create your views here.

def product(request):
    return render(request, 'products/product.html')

def products(request):

    pro = Product.objects.all()
    # x = {'pro':Product.objects.all()} #all the products from the database are passed to the products.html template for display
    # x = {'pro':Product.object.get(id=1)} #one product is passed to the products.html template for display with id=1
    
    #x = {'pro':pro.filter(id=1)}  #one product is passed to the products.html template for display with id=1
    #x = {'pro':pro}  #all the products from the database are passed to the products.html template for display
    #x = {'pro':pro.order_by('price')} #all the products  ordered by price
    #x = {'pro':str(pro.count())} #the number of products in the database is passed to the products.html template for display
    #x = {'pro':pro.exclude(price=150)} #all the products  excluding products with price=150
    x = {'pro':pro} 
    return render(request, 'products/products.html', x)

