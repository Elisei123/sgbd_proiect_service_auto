from django.shortcuts import render
from  .models import Clienti, Comenzi, Constatari, Echipe, Piese, Sarcini, Specialisti
# Create your views here.

def schita(request):
    return render(
        request,
        'schita.html',
    )

def home(request):
    return render(
        request,
        'home.html',
    )

def piese(request):
    piese = Piese.objects.raw('SELECT * FROM Piese')
    return render(request,
                  'piese.html',
                  {
                      'piese': piese,
                  }
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

def echipe(request):
    echipe = Echipe.objects.raw('SELECT * FROM Echipe')
    return render(request,
                      'echipe.html',
                      {
                        'echipe': echipe,
                      }
    )

def sarcini(request):
    sarcini = Sarcini.objects.raw('SELECT * FROM Sarcini')
    return render(request,
                  'sarcini.html',
                  {
                      'sarcini': sarcini,
                  }
    )

def specialisti(request):
    specialisti = Specialisti.objects.raw('SELECT * FROM Specialisti')
    return render(request,
                  'specialisti.html',
                  {
                      'specialisti': specialisti,
                  }
    )
