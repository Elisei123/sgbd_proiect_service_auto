from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clienti/', views.clienti, name='clienti'),
    path('comenzi/', views.comenzi, name='comenzi'),
    path('constatari/', views.constatari, name='constatari'),
    path('echipe/', views.echipe, name='echipe'),
    # path('piese/', views.piese, name='piese'),
    # path('sarcini/', views.sarcini, name='sarcini'),
    # path('specialisti/', views.specialisti, name='specialisti'),

]
