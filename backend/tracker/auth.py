from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
import logging


# Custom User Creation Form
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

#Register and login are from here on

def register_auth(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        logging.warning(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
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


