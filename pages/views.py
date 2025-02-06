from django.shortcuts import render , redirect
from .models import Login
from .forms import LoginForm
# Create your views here.

def index(request):
    x={'name' : 'ali mazen mohamed hasan','size':984985148}
    return render(request,'pages/index.html',x)

def about(request):
    if request.method == 'POST':  # this condition checks if the form was submitted

        form = LoginForm(request.POST)
        # check if the form is valid  # checks if all the required fields in the form are filled correctly
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username:  # You could also check for password if needed
                data = Login(username=username, password=password)
                data.save()
                return redirect('about') # needed to fix the reload thing after form submission
            

    return render(request,'pages/about.html',{'lf':LoginForm}) #we pass the form to the about.html template 