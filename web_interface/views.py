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

# - Proiectie
def ComenziDistincte(request):

    from django.db import connection
    ComenziDistincte = connection.cursor()
    ComenziDistincte.execute("SELECT DISTINCT descriere FROM Comenzi GROUP BY descriere")

    lista_comenzi_distincte = []
    for row in ComenziDistincte:
        lista_comenzi_distincte.append(row[0])
    return render(
        request,
        'ComenziDistincte.html',
        {
            'lista_comenzi_distincte':lista_comenzi_distincte
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

# - Diferenta
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

# - Selectie
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

# - Jonctiunea (I)
def incasari(request):
    Incasare = Constatari.objects.raw("SELECT id_constatare,"
                                          " c.nume, c.prenume,"
                                          " const.pret_lucrare"
                                      " from Clienti c "
                                          "INNER JOIN Comenzi com "
                                                "ON c.id=com.CNP_Client "
                                          "INNER JOIN Constatari const "
                                                "ON com.id_comanda = const.id_constatare")

    total_incasari = 0

    for i in Incasare:
        total_incasari = total_incasari + i.pret_lucrare
    print(total_incasari)
    return render(
        request,
        'Incasari.html',
        {
            'Incasare': Incasare,
            'total_incasari': total_incasari,
        }
    )

# - Reuniune
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


#- Jonctiunea (II)
def ConstatariCuPiese(request):
    ConstatariCuPiese = Piese.objects.raw(
        "SELECT p.id_piesa,"
            " p.nume_piesa,"
            " com.data_comanda,"
            " com.stare_comanda,"
            " com.descriere "
        "from Piese p "
            "inner JOIN Constatari const"
                " ON p.id_constatare=const.id_constatare"
            " INNER JOIN Comenzi com"
                " ON const.id_comanda=com.id_comanda")
    return render(
        request,
        'ConstatariCuPiese.html',
        {
            'ConstatariCuPiese': ConstatariCuPiese,
        }
    )
