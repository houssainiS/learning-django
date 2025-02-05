from django.shortcuts import render
from .models import Login
from .forms import LoginForm
# Create your views here.

def index(request):
    x={'name' : 'ali mazen mohamed hasan','size':984985148}
    return render(request,'pages/index.html',x)

def about(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username:  # You could also check for password if needed
            data = Login(username=username, password=password)
            data.save()
            

    return render(request,'pages/about.html',{'lf':LoginForm}) #we pass the form to the about.html template 