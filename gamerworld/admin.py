from django.contrib import admin

from gamerworld.models import Biblioteca,Genero, ListaDeseos, SistemaPlataforma, Usuarios, Videojuego


# Register your models here.

admin.site.register(Biblioteca)
admin.site.register(Genero)
admin.site.register(SistemaPlataforma)
admin.site.register(Usuarios)
admin.site.register(Videojuego)
admin.site.register(ListaDeseos)

