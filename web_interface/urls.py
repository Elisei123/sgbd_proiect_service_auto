from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('schita/', views.schita, name='schita'),
    path('clienti/', views.clienti, name='clienti'),
    path('comenzi/', views.comenzi, name='comenzi'),
    path('constatari/', views.constatari, name='constatari'),
    path('echipe/', views.echipe, name='echipe'),
    path('piese/', views.piese, name='piese'),
    path('sarcini/', views.sarcini, name='sarcini'),
    path('specialisti/', views.specialisti, name='specialisti'),
    path('especialisti/', views.especialisti, name='especialisti'),
    path('incasari/', views.incasari, name='incasari'),
    path('StareComenzi/', views.StareComenzi, name='StareComenzi'),
    path('CautareClient/', views.CautareClient, name='CautareClient'),
    path('ComenziEfectuate/', views.ComenziEfectuate, name='ComenziEfectuate'),
    path('ConstatariCuPiese/', views.ConstatariCuPiese, name='ConstatariCuPiese'),
    path('ComenziDistincte/', views.ComenziDistincte, name='ComenziDistincte'),
]
