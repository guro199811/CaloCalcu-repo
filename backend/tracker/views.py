from django.shortcuts import render, redirect
from django.http import HttpResponse




def home(request):
    return render(request, 'tracker/home.html')


def contact(request):
    return render(request, 'tracker/contact.html')


