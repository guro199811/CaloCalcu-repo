from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='Calocalco-Home'),
    path('about/', views.about, name='Calocalco-About')
]