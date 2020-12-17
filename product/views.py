from django.shortcuts import render

from .models import Products


def homepage(request):
         prod = Products.objects.all()
         return render(request, 'home.html', {'prod': prod})


def scrap(request):

        return render(request,'scrap.html')