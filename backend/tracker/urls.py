from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from . import auth
from . import logic


urlpatterns = [
    path('', views.home, name='calo-home'),
    path('about/', views.about, name='calo-about'),
    path('contact/', views.contact, name='calo-contact'),
    path('login/', auth.login_auth, name='calo-login'),
    path('register/', auth.register_auth, name='calo-register'), 
    path('logout/', auth.logout_auth, name='calo-logout'),
    path('add-food-history/', logic.add_food_history, name='add_food_history'),
    path('retrieve-food-history/', logic.retrieve_food_history, name='retieve_food_history')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)