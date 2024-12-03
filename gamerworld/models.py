from pyexpat import model

from django.db import models


#from gamerworld.views import listadeseos

# Create your models here.

class Biblioteca(models.Model):

    codVideojuego=  models.IntegerField(default=4)
    codUsuario= models.IntegerField(default=4)
    cantidadvdj= models.IntegerField(default=4)

class Genero(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion= models.CharField(max_length=150)
    publicoobjetivo=models.CharField(max_length=150)
    edadrecomendada=models.CharField(max_length=5)

class SistemaPlataforma(models.Model):
    nombre=models.CharField(max_length=30)
    fabricante=models.CharField(max_length=40)

class Usuarios(models.Model):
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=80)
    email=models.CharField(max_length=100)
    nickname=models.CharField(max_length=25)

class Videojuego(models.Model):
    codVideojuego=  models.IntegerField(default=4)
    codempresa=models.IntegerField(default=5)
    sistemaPlataforma=models.IntegerField(default=5)
    codgenero=models.IntegerField(default=5)
    sipnosis=models.TextField(max_length=150)
    fechaSalida=models.DateField()
    valoracion=models.IntegerField(default=10)
    comentarios=models.CharField(max_length=100)
    nombre=models.CharField(max_length=50)
    precio=models.FloatField()

class ListaDeseos(models.Model):
    codVideojuego=  models.IntegerField(default=4)
    nombreJuego=models.CharField(max_length=50)
    codUsuario= models.IntegerField(default=4)
    cantidadvdj= models.IntegerField(default=4)
    listadeseos= models.CharField(max_length=50)
    estado=models.CharField(max_length=20) # publico o privado


