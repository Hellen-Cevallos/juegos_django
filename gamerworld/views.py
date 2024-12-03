from contextlib import redirect_stderr
from email import message
from multiprocessing import context
from django.http import HttpResponse
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from .models import Biblioteca, ListaDeseos, Videojuego
from gamerworld.models import Biblioteca,ListaDeseos, Videojuego
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError



# Create your views here.
def inicio(request): # Recibe un objeto de tipo request
    return render(request,"principal.html")  # Lo que va a recibir como 2DO parametro es el códigoo de html(en este caso es la plantilla )lo que le va a mandar el usuario
def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
    }) 
    else:
        if request.POST['password1'] == request.POST['password1']:
            #registrar usuario
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('tasks')
            except IntegrityError:    

                return render(request, 'signup.html',{
                    'form':UserCreationForm,
                    "error":'El usuario ya existe'
                })
        return render(request, 'signup.html',{
                'form': UserCreationForm,
                "error": 'Contraseña incorrecta'
    })            

@login_required    
def tasks(request):
    taks = taks.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'principal.html', {
        "tasks": tasks})
    
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('tasks')


def consultargames(request):
    biblio = Videojuego.objects.all() #una variable con el modelo y el objects con  todo
    return render(request, "juegos.html",{  # luego se envia un tercr parametro que en este caso es un diccionario un diccionario tiene la clave y el valor 
        'biblio': biblio
    })


def listadeseos(request):
    listads= ListaDeseos.objects.all()
    return render(request, "colecciones.html",{
        "listads" : listads
    })

def carrito(request):
    carritoComp=Biblioteca.objects.all()
    return render(request, "carritoVideojuego.html",{
        "carritoComp" : carritoComp
    })
    

def guardarjuego(request):
    codVideojuego=request.POST["codVideojuego"]
    codUsuario=request.POST["codUsuario"]
    cantidadvdj=request.POST["cantidadvdj"]
    j=Biblioteca(codVideojuego=codVideojuego, codUsuario=codUsuario,cantidadvdj=cantidadvdj)
    j.save()
    messages.success(request, 'Videojuego Agregado')
    return redirect('consultargames')


def eliminar(request, codVideojuego):
    biblioteca=Biblioteca.objects.filter(pk=codVideojuego)
    biblioteca.delete()
    messages.success(request,'Videojuego eliminado')
    return redirect('consultargames')
    

def descripcion(request,codVideojuego):
    biblioteca = Biblioteca.objects.get(pk=codVideojuego)
    return render(request, "juegos.html")