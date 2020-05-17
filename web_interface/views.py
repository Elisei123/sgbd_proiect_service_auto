import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

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

# todo: de facut aici
@csrf_exempt
def clienti(request):
    clienti = Clienti.objects.raw('SELECT * FROM Clienti ORDER BY id_client DESC;')
    if request.POST:
        data = json.loads(request.POST.get("data", "{}"))
        for id in data['checklisturi_apasate']:
            Clienti.objects.filter(id_client=str(id)).delete()

    return render(
        request,
        'clienti.html',
        {
            'clienti': clienti,
        }
    )

def editareClient(request, client_id_client):
    if request.POST:
        CNP_Client=request.POST['CNP_Client']
        Nume=request.POST['Nume']
        Prenume=request.POST['Prenume']
        Telefon=request.POST['Telefon']
        Judet=request.POST['Judet']
        Oras=request.POST['Oras']
        Strada=request.POST['Strada']
        Numar_poarta=request.POST['Numar_poarta']

        with connection.cursor() as cursor:
            cursor.execute("UPDATE `Clienti` SET `CNP_Client` = '"+CNP_Client+"', `nume` = '"+Nume+"', `prenume` = '"+Prenume+"',"
                           " `telefon` = '"+Telefon+"', `judet` = '"+Judet+"', `oras` = '"+Oras+"', `strada` = '"+Strada+"', `numar_poarta` = '"+Numar_poarta+"' WHERE `Clienti`.`id_client` = "+ client_id_client+";")
        return redirect(clienti)

    obj_client_pt_editat = Clienti.objects.get(pk=client_id_client)
    return render(
        request,
        'editClienti.html',
        {
            'obj_client_pt_editat': obj_client_pt_editat,
        }
    )

def addClient(request):
    if request.POST:
        CNP_Client=request.POST['CNP_Client']
        Nume=request.POST['Nume']
        Prenume=request.POST['Prenume']
        Telefon=request.POST['Telefon']
        Judet=request.POST['Judet']
        Oras=request.POST['Oras']
        Strada=request.POST['Strada']
        Numar_poarta=request.POST['Numar_poarta']

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO `Clienti` (`id_client`, `CNP_Client`, `nume`, `prenume`, `telefon`, `judet`, `oras`, `strada`, `numar_poarta`)"
                           " VALUES (NULL,'" + CNP_Client +  "', '" + Nume +  "', '" + Prenume +  "', '" + Telefon +  "', '" + Judet +  "', '" + Oras +  "', '" + Strada +  "', '" + Numar_poarta + "');")
        return redirect(clienti)

    return render(
        request,
        'addClient.html',
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

@csrf_exempt
def echipe(request):
    if request.POST:
        data = json.loads(request.POST.get("data", "{}"))
        for id in data['checklisturi_apasate']:
            Echipe.objects.filter(id_echipa=str(id)).delete()

    echipe = Echipe.objects.raw('SELECT * FROM Echipe')
    return render(
        request,
        'echipe.html',
        {
            'echipe': echipe,
        }
    )

@csrf_exempt
def addteam(request):
    if request.POST:
        Nume_echipa = request.POST['nume_echipa']
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO `Echipe` (`id_echipa`, `nume_echipa`) VALUES (NULL, '" + Nume_echipa + "');")
        return redirect(echipe)
    return render(
        request,
        'add_team.html',
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

@csrf_exempt
def specialisti(request):
    specialisti = Specialisti.objects.raw('SELECT * from Specialisti ORDER BY id_specialist DESC;')

    if request.POST:
        data = json.loads(request.POST.get("data", "{}"))
        for id in data['checklisturi_apasate']:
            Specialisti.objects.filter(id_specialist=str(id)).delete()

    return render(
        request,
        'specialisti.html',
        {
            'specialisti': specialisti,
        }
    )

def add_specialist(request):
    echipe = Echipe.objects.raw('SELECT * FROM Echipe')
    if request.POST:
        Nume = request.POST['Nume']
        Prenume = request.POST['Prenume']
        Specializare = request.POST['Specializare']
        ID_Echipa = request.POST['id_echipa']
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO `Specialisti` (`id_specialist`, `nume`, `prenume`, `specializare`, `id_echipa`) VALUES (NULL, '" + Nume +  "', '" + Prenume + "', '" + Specializare + "', '" + ID_Echipa + "');")
        return redirect(specialisti)

    return render(
        request,
        'addSpecialist.html',
        {
            'echipe': echipe,
        }
    )

def editareSpecialist(request, client_id_client):
    global id_echipa_pt_specialist
    if request.POST:
        Nume = request.POST['Nume']
        Prenume = request.POST['Prenume']
        Specializare = request.POST['Specializare']
        ID_Echipa = request.POST['id_echipa']
        with connection.cursor() as cursor:
            cursor.execute("UPDATE `Specialisti` SET `nume` = '" + Nume + "', `prenume` = '" + Prenume + "', `specializare` = '" + Specializare + "', `id_echipa` = '" + ID_Echipa + "' WHERE `Specialisti`.`id_specialist` = " + client_id_client + ";")
        return redirect(specialisti)

    obj_specialist_pt_editat = Specialisti.objects.get(pk=client_id_client)
    echipe = Echipe.objects.raw('SELECT * FROM Echipe')

    # get id from 'echipe', because if have only name from 'echipa'
    for i in echipe:
        if i.nume_echipa == str(obj_specialist_pt_editat.id_echipa):
            id_echipa_pt_specialist = i.id_echipa
    return render(
        request,
        'editSpecialist.html',
        {
            'obj_client_pt_editat': obj_specialist_pt_editat,
            'echipe': echipe,
            'id_echipa_pt_specialist': id_echipa_pt_specialist,
        }
    )


# - Selectie
def especialisti(request):
    Mecanici = Specialisti.objects.raw('SELECT id_specialist, nume, prenume, specializare, nume_echipa FROM Specialisti s INNER JOIN Echipe e WHERE s.id_echipa=e.id_echipa AND specializare="Mecanic"')
    Electromecanici = Specialisti.objects.raw('SELECT id_specialist, nume, prenume, specializare, nume_echipa FROM Specialisti s INNER JOIN Echipe e WHERE s.id_echipa=e.id_echipa AND specializare="Electromecanic"')
    Electricieni = Specialisti.objects.raw('SELECT id_specialist, nume, prenume, specializare, nume_echipa FROM Specialisti s INNER JOIN Echipe e WHERE s.id_echipa=e.id_echipa AND specializare="Electrician"')
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
                                                "ON c.id_client=com.id_client "
                                          "INNER JOIN Constatari const "
                                                "ON com.id_comanda = const.id_comanda")

    total_incasari = 0

    for i in Incasare:
        total_incasari = total_incasari + i.pret_lucrare
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

