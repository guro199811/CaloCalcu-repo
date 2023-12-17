from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.home, name='calo-home'),
    path('about/', views.about, name='calo-about'),
    path('login/', views.login_page, name='calo-login'),
    path('registration/', views.register_page, name='calo-register')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)