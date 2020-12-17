from django.shortcuts import render , redirect
from django.http import HttpResponse

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
# Create your views here.

def Login(request):
    if request.method== 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username , password=password)

        if user is not None:
            login( request ,user )
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
    context={}            
    return render(request,'login.html' , context)

def register(request):
   
    form = CreateUserForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
             form.save()
             user = form.cleaned_data.get('username')
             messages.success(request,'Account was created for :'+user)
             return redirect('login')
           
    context={'form' :form}
    return render(request,'register.html',context)



def Logout(request):
    logout(request)
    return redirect('login')