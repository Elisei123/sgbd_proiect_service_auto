from django.db import models

# Create your models here.

class Clienti(models.Model):
    id_client = models.AutoField(primary_key=True)
    CNP_Client = models.CharField(max_length=14)
    nume = models.CharField(max_length=35)
    prenume = models.CharField(max_length=35)
    judet = models.CharField(max_length=40)
    oras = models.CharField(max_length=40)
    strada = models.CharField(max_length=40)
    numar_poarta = models.CharField(max_length=40)
    telefon = models.CharField(max_length=11)

    class Meta:
        db_table = 'Clienti'

    def __str__(self):
        return '{}'.format(self.id_client)


class Comenzi(models.Model):
    id_comanda = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Clienti, models.DO_NOTHING, db_column='id_client')
    data_comanda = models.DateField()
    stare_comanda = models.CharField(max_length=35)
    descriere = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Comenzi'

    def __str__(self):
        return '{}'.format(self.id_comanda)

class Echipe(models.Model):
    id_echipa = models.AutoField(primary_key=True)
    nume_echipa = models.CharField(db_column='nume_echipa', max_length=25)

    class Meta:
        db_table = 'Echipe'

    def __str__(self):
        return '{}'.format(self.nume_echipa)

class Specialisti(models.Model):
    id_specialist = models.AutoField(primary_key=True)
    id_echipa = models.ForeignKey(Echipe, models.DO_NOTHING, db_column='id_echipa')
    nume = models.CharField(max_length=35)
    prenume = models.CharField(max_length=35)
    specializare = models.CharField(max_length=25)

    class Meta:
        db_table = 'Specialisti'

    def __str__(self):
        return '{}'.format(self.id_specialist) # Before '{}' if you want to add text.

class Constatari(models.Model):
    id_constatare = models.AutoField(primary_key=True)
    id_comanda = models.OneToOneField(Comenzi, models.DO_NOTHING, db_column='id_comanda')
    id_echipa = models.ForeignKey(Echipe, models.DO_NOTHING, db_column='id_echipa')
    pret_lucrare = models.IntegerField()

    class Meta:
        db_table = 'Constatari'

    def __str__(self):
        return '{}'.format(self.id_constatare)


class Piese(models.Model):
    id_piesa = models.AutoField(primary_key=True)
    id_constatare = models.ForeignKey(Constatari, models.DO_NOTHING, db_column='id_constatare')
    pret = models.IntegerField()
    cantitate = models.IntegerField()
    nume_piesa = models.CharField(max_length=55)

    class Meta:
        db_table = 'Piese'

    def __str__(self):
        return '{}'.format(self.id_piesa)


class Sarcini(models.Model):
    id_sarcina = models.AutoField(primary_key=True)
    id_constatare = models.ForeignKey(Constatari, models.DO_NOTHING, db_column='id_constatare')
    task = models.TextField(db_column='Task')  # Field name made lowercase.

    class Meta:
        db_table = 'Sarcini'

    def __str__(self):
        return '{}'.format(self.id_sarcina)
