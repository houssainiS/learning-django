from django.shortcuts import render

# Create your views here.

def index(request):
    x={'name' : 'ali mazen mohamed hasan','size':984985148}
    return render(request,'pages/index.html',x)

def about(request):
    return render(request,'pages/about.html')