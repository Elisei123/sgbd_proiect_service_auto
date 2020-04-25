from django.shortcuts import render
from  .models import Clienti, Comenzi, Constatari, Echipe, Piese, Sarcini, Specialisti
# Create your views here.

def home(request):
    return render(
        request,
        'home.html',
    )

def clienti(request):
    clienti = Clienti.objects.raw('SELECT * FROM Clienti')
    return render(request,
                      'clienti.html',
                      {
                        'clienti': clienti,
                      }
    )

def comenzi(request):
    comenzi = Comenzi.objects.raw('SELECT * FROM Comenzi')
    return render(request,
                      'comenzi.html',
                      {
                        'comenzi': comenzi,
                      }
    )

def constatari(request):
    constatari = Constatari.objects.raw('SELECT * FROM Constatari')
    return render(request,
                      'constatari.html',
                      {
                        'constatari': constatari,
                      }
    )
# TODO: ValueError: Field 'id_constatare' expected a number but got 'Echipa001'.
def echipe(request):
    echipe = Echipe.objects.raw('SELECT * FROM Echipe')
    return render(request,
                      'echipe.html',
                      {
                        'echipe': echipe,
                      }
    )
