"""
URL configuration for project_name project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gamerworld import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('',views.inicio, name='inicio'), #para crear nuestras vistas , se les agrega un nombre para llamar a cada una de las rutas
    path('juegos', views.consultargames, name='consultargames'),
    path('colecciones',views.listadeseos, name='listadeseos'),
    path('carritoVideojuego', views.carrito, name='carrito'),
    path('juegos/guardar/', views.guardarjuego, name='guardarjuego'),
    path('juegos/eliminar/<int:codVideojuego>/', views.eliminar, name='eliminar'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


