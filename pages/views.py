from django.shortcuts import render

# Create your views here.

def index(request):
    x={'name' : 'nana','age':25}
    return render(request,'pages/index.html',x)

def about(requeest):
    pass