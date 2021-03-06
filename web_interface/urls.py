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
    path('comenzi_cu_piese_si_sarcini/', views.comenzi_cu_piese_si_sarcini, name='comenzi_cu_piese_si_sarcini'),
    path('CautareClient/', views.CautareClient, name='CautareClient'),
    path('ComenziEfectuate/', views.ComenziEfectuate, name='ComenziEfectuate'),
    path('constatari_piese_mm/', views.constatari_piese_mm, name='constatari_piese_mm'),
    path('ComenziDistincte/', views.ComenziDistincte, name='ComenziDistincte'),
    path('addClient/', views.addClient, name='addClient'),
    path('editareClient/<client_id_client>', views.editareClient, name='editareClient'),
    path('addSpecialist', views.add_specialist, name='addSpecialist'),
    path('editareSpecialist/<client_id_client>', views.editareSpecialist, name='editareSpecialist'),
    path('addteam', views.addteam, name='addteam'),
    path('Comenzi_fara_constatare/', views.Comenzi_fara_constatare, name='Comenzi_fara_constatare'),
]
