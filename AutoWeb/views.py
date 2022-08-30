from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader
from AutoWeb.forms import *

# Create your views here.


def inicio(request):

    return render(request, "RoseCoder/inicio.html")

#escuderia/autos


def escuderia(request):
    if request.method == "POST":
        miFormue = AutosFormu(request.POST)
        print(miFormue)
        if miFormue.is_valid():
            info1 = miFormue.cleaned_data
            print(info1)
            id = info1.get("id")
            nombre = info1["nombre"]
            escuderias = info1["escuderias"]
            piloto = info1["piloto"]
            auto = Autos(id, nombre, escuderias, piloto)
            auto.save()
            return render(request, "RoseCoder/inicio.html", {"mensaje": "Exelecente has elegido unas de las mejores!!"})
        else:
            return render(request, "RoseCoder/inicio.html", {"mensaje": "Error"})

    else:
        miFormue = AutosFormu()
        return render(request, "RoseCoder/escuderia.html", {"formulario": miFormue})

#circuito


def circuitos(request):

    if request.method == "POST":

        formuc = Circuitoform(request.POST)
        print(formuc)
        if formuc.is_valid():

            info2 = formuc.cleaned_data
            print(info2)
            circuito = info2.get("circuito")
            id = info2.get("id")
            circu = Circuito(id, circuito)
            circu.save()
            return render(request, "RoseCoder/inicio.html", {"mensaje": "Gracias por elegir tu circuito favorito"})

        else:

           return render(request, "RoseCoder/inicio.html", {"mensaje": "Error"})
    else:
        formuc = Circuitoform()
        return render(request, "RoseCoder/circu.html", {"formulari": formuc})


# formulario de persona
def Personas(resquest):
    if resquest.method == "POST":
        miFormu = PersonaFormulario(resquest.POST)
        print(miFormu)
        if miFormu.is_valid():
            info = miFormu.cleaned_data
            print(info)
            nombre = info["nombre"]
            apellido = info["apellido"]
            fecha_Nacimiento = info["fecha_Nacimiento"]
            personas = Persona(
                nombre=nombre, apellido=apellido, fecha_Nacimiento=fecha_Nacimiento)
            personas.save()
            return render(resquest, "RoseCoder/inicio.html", {"mensaje": "GRACIAS por ser parte de nuestro grupo amante a la F1"})
        else:
            return render(resquest, "RoseCoder/inicio.html", {"mensaje": "Error verifica que los datos sean correctos"})
    else:
        miFormu = PersonaFormulario()
        return render(resquest, "RoseCoder/persona.html", {"formula": miFormu})
    
    
    
#render a la busqueda

def Busqueda(request):
    return render(request,"RoseCoder/buscar.html")



#Buscar info en las tablas.
def Buscar(request):
    persona= request.GET["nombre"]
    personas=Persona.objects.filter(nombre=persona)
    if len(personas) !=0:
        return render(request,"RoseCoder/busqueda.html",{"personas":personas})
    else:
        return render (request,"RoseCoder/inicio.html", {"mensaje": "No figurar como fanatico, Vamos!! registrate en formulario!!"})
    




