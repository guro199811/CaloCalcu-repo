from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from . import auth
from . import logic


urlpatterns = [
    path('', views.home, name='calo-home'),
    path('contact/', views.contact, name='calo-contact'),
    path('login/', auth.login_auth, name='calo-login'),
    path('register/', auth.register_auth, name='calo-register'),
    path('login-error/', auth.login, name='calo-login-error'),
    path('reset-password/', auth.reset_password, name='calo-res-pas'),
    path('logout/', auth.logout_auth, name='calo-logout'),
    path('add-food-history/', logic.add_food_history, name='add_food_history'),
    path('retrieve-food-history/', logic.retrieve_food_history, name='retieve_food_history'),
    path('remove-food-entry/', logic.remove_food_entry, name='remove_food_entry')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)