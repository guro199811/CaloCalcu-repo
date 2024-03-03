from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from . import views
from . import auth
from . import logic


urlpatterns = [
    path('', views.home, name='calo-home'),
    path('contact/', views.contact, name='calo-contact'),
    path('login/', auth.login_auth, name='calo-login'),
    path('register/', auth.register_auth, name='calo-register'),
    path('login-error/', auth.login, name='calo-login-error'),

    path('reset_password/', PasswordResetView.as_view(
        template_name='tracker/unsuccesfull_login.html',
        extra_context={'forgot_password' : True}),
        name='reset_password'),

    path('reset_password_sent/', PasswordResetDoneView.as_view(
        template_name='tracker/unsuccesfull_login.html',
        extra_context={'sent_password_reset' : True}), 
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='tracker/unsuccesfull_login.html',
        extra_context={'password_reset': True}), 
        name='password_reset_confirm'),

    path('reset_password_complete/', PasswordResetCompleteView.as_view(
        template_name='tracker/unsuccesfull_login.html',
        extra_context={'password_reset_complete': True}),
        name='password_reset_complete'),
    
    path('logout/', auth.logout_auth, name='calo-logout'),
    path('add-food-history/', logic.add_food_history, name='add_food_history'),
    path('retrieve-food-history/', logic.retrieve_food_history, name='retieve_food_history'),
    path('remove-food-entry/', logic.remove_food_entry, name='remove_food_entry'),
    path('send_contact/', logic.contact_us, name='calo-contact-us')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)