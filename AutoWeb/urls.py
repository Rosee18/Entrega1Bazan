import imp
from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('inicio',inicio, name= "inicio" ),
    path ('escuderia', escuderia,name="escuderia"),
    path ('circuitos', circuitos,name="circuitos"),
    path ('Personas', Personas,name="personas"),
    path('Buscar',Buscar,name="Buscar"),
    path('Busqueda',Busqueda,name="Busqueda"),
]