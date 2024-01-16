from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
import logging


def register_auth(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        logging.warning(request.POST)
        if form.is_valid():
            user = form.save()
            logging.warning("Registered")
            login(request, user)
            logging.warning("Logged In From Registration")
            return redirect('calo-home')
        else:
            logging.warning('Reg Form Is NOT Valid')
            logging.warning(form.errors)
    else:
        form = UserCreationForm()

    return render(request, 'tracker/home.html', {'form': form})

def login_auth(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logging.warning('Logged In')
            return redirect('calo-home')
        else:
            logging.warning('Log Form Is NOT Valid')
            logging.warning(form.errors)
    else:
        form = AuthenticationForm()

    return render(request, 'tracker/home.html', {'form': form})


def logout_auth(request):
    logout(request)
    return redirect('calo-home')