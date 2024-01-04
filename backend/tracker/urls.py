from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from . import auth


urlpatterns = [
    path('', views.home, name='calo-home'),
    path('about/', views.about, name='calo-about'),
    path('contact/', views.contact, name='calo-contact'),
    path('login/', auth.login_view, name='calo-login'),
    path('register/', auth.register_view, name='calo-register')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)