from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    name = 'gurami'
    context= {
    'name' : name
    }
    return render(request, 'tracker/home.html', context)

def about(request):
    return render(request, 'tracker/about.html')