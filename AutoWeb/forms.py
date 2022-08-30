from dataclasses import field, fields
from pyexpat import model
from .models import *
from django.forms import ModelForm
from django import forms


# desde este archivo .py voy a crear mis formularios

#formulario de personas
#class PersonaFormulario(forms.Form):
    
    #nombre= forms.CharField(max_length=30)
    #apellido = forms.CharField(max_length=30)
    #fecha_Nacimiento = forms.DateField()
    #sexo = forms.CharField(max_length=12)
    
    
#Investigando consegui esta forma de generar la clase, con los mismo atributos del models  
#fomulario persona
class PersonaFormulario(ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
        
 #formulario escuderia       
class AutosFormu(ModelForm):
    class Meta:
        model = Autos
        fields = "__all__"
        
        
#formulario circuito

class Circuitoform(ModelForm):
    class Meta:
        model = Circuito
        fields = "__all__"