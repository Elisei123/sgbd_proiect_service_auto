from django.shortcuts import render
from .models import Clienti, Comenzi, Constatari, Echipe, Piese, Sarcini, Specialisti


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
    return render(
        request,
        'piese.html',
        {
            'piese': piese,
        }
    )


def clienti(request):
    clienti = Clienti.objects.raw('SELECT * FROM Clienti')

    return render(
        request,
        'clienti.html',
        {
            'clienti': clienti,
        }
    )


def CautareClient(request):
    firstname = request.GET.get('firstname', default="")
    lastname = request.GET.get('lastname', default="")
    clienti = Clienti.objects.raw("SELECT * FROM `Clienti` WHERE `nume` LIKE %s AND `prenume` LIKE %s", [
        '%{}%'.format(firstname),
        '%{}%'.format(lastname),
    ])
    return render(
        request,
        'CautareClient.html',
        {
            'clienti': clienti,
            'firstname': firstname,
            'lastname': lastname,

        }
    )


def comenzi(request):
    comenzi = Comenzi.objects.raw('SELECT * FROM Comenzi')
    return render(
        request,
        'comenzi.html',
        {
            'comenzi': comenzi,
        }
    )
def ComenziEfectuate(request):
    comenzi = Comenzi.objects.raw("SELECT * FROM `Comenzi`"
                                  " EXCEPT "
                                  "SELECT * FROM `Comenzi` WHERE stare_comanda = 'In desfasurare!' OR stare_comanda= 'Comanda plasata!'"
 )
    return render(
        request,
        'ComenziEfectuate.html',
        {
            'comenzi': comenzi,
        }
    )


def constatari(request):
    constatari = Constatari.objects.raw('SELECT * FROM Constatari')
    return render(
        request,
        'constatari.html',
        {
            'constatari': constatari,
        }
    )


def echipe(request):
    echipe = Echipe.objects.raw('SELECT * FROM Echipe')
    return render(
        request,
        'echipe.html',
        {
            'echipe': echipe,
        }
    )


def sarcini(request):
    sarcini = Sarcini.objects.raw('SELECT * FROM Sarcini')
    return render(
        request,
        'sarcini.html',
        {
            'sarcini': sarcini,
        }
    )


def specialisti(request):
    specialisti = Specialisti.objects.raw('SELECT * FROM Specialisti')
    return render(
        request,
        'specialisti.html',
        {
            'specialisti': specialisti,
        }
    )


def especialisti(request):
    Mecanici = Specialisti.objects.raw('SELECT * FROM Specialisti WHERE specializare="Mecanic"')
    Electromecanici = Specialisti.objects.raw('SELECT * FROM Specialisti WHERE specializare="Electromecanic"')
    Electricieni = Specialisti.objects.raw('SELECT * FROM Specialisti WHERE specializare="Electrician"')
    return render(
        request,
        'especialisti.html',
        {
            'Mecanici': Mecanici,
            'Electromecanici': Electromecanici,
            'Electricieni': Electricieni
        }
    )


def incasari(request):
    # TODO: De terminat aici. Trebuie sa facem select din baza de date:
    # TODO: SELECT nume, prenume, pret_lucrare from Clienti WHERE p.s CNP este id  (diferit)

    Mecanici = Specialisti.objects.raw('SELECT * FROM Specialisti WHERE specializare="Mecanic"')
    Electromecanici = Specialisti.objects.raw('SELECT * FROM Specialisti WHERE specializare="Electromecanic"')
    Electricieni = Specialisti.objects.raw('SELECT * FROM Specialisti WHERE specializare="Electrician"')
    return render(
        request,
        'incasari.html',
        {
            'Mecanici': Mecanici,
            'Electromecanici': Electromecanici,
            'Electricieni': Electricieni
        }
    )


def StareComenzi(request):
    comenzi = Comenzi.objects.raw("SELECT * FROM Comenzi WHERE stare_comanda = 'In desfasurare!'"
                                  " UNION"
                                  " SELECT * FROM Comenzi WHERE stare_comanda = 'Comanda plasata!'")
    return render(
        request,
        'stare_comenzi.html',
        {
            'comenzi': comenzi,
        }
    )
