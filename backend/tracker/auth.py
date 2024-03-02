# For Routing
from django.shortcuts import render, redirect
# For User Management
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# For Debugging
import logging
# For Sending Emails
from django.core.mail import send_mail
# Custom Token Generator
from .tokens import generate_reset_link




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
            username_error = None
            password_error = None
            for error_list in form.errors.values():  # Iterate over error lists
                for error in error_list:
                    if 'username' in error and not username_error:
                        username_error = error
                    elif 'password' in error and not password_error:
                        password_error = error

            # Render the template with specific error messages
            context = {'form': form}
            if username_error:
                context['username_error'] = username_error
            if password_error:
                context['password_error'] = password_error

            return render(request, 'tracker/unsuccesfull_login.html', context)
    else:
        form = AuthenticationForm()

    return render(request, 'tracker/unsuccesfull_login.html', {'form': form})


from django.core.mail import send_mail

def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)

            reset_link = generate_reset_link(user)

            subject = "Password Reset Instructions"
            message = f"Click the link below to reset your password:\n{reset_link}"
            from_email = "noreply@example.com" # Sender
            recipient_list = [email]
            variables = {
                'email_sent' : True
            }
            
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except:
            print("Invalid header found.")
            variables = {
                'email_send' : False,
                'forgot_password' : True,
                'errors' : True
        }
        return render(request, 'tracker/unsuccesfull_login.html', variables)
    else:
        variables = {
            'forgot_password': True
        }

        return render(request, 'tracker/unsuccesfull_login.html', variables)

# def password_reset_confirm(request):
#     pass

def logout_auth(request):
    logout(request)
    return redirect('calo-home')


