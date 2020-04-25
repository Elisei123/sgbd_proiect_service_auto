from django.contrib import admin

# Register your models here.
from web_interface.models import Clienti, Comenzi, Constatari, Echipe, Piese, Sarcini, Specialisti


@admin.register(Clienti)
class ClientiAdmin(admin.ModelAdmin):
    pass

@admin.register(Comenzi)
class ComenziAdmin(admin.ModelAdmin):
    pass

@admin.register(Constatari)
class ConstatariAdmin(admin.ModelAdmin):
    pass

@admin.register(Echipe)
class EchipeAdmin(admin.ModelAdmin):
    pass

@admin.register(Piese)
class PieseAdmin(admin.ModelAdmin):
    pass

@admin.register(Sarcini)
class SarciniAdmin(admin.ModelAdmin):
    pass

@admin.register(Specialisti)
class SpecialistiAdmin(admin.ModelAdmin):
    pass