# Entrega1Bazan
#http://127.0.0.1:8000/RoseCoder/inicio
Proyecto:
El proyecto fue realizado para cumplir ciertas funcionalidades 
el mismo cumple con el patron MVT.

Tenemos tres models.py 
#class Persona(models.Model):
#class Circuito(models.Model):
#class Autos
con la cuales creamos el modelo de la base de datos

En caso de agregar otros modelos, modificar tanto el form.py como el views.py como corresponda. 
agregar el campo ID de la base de datos ejem: id = info1.get("id") en la views. para asi evitar malos ratos. al momento de validar si el form es valido.


Tenemos los html. en el path: RoseCoder\AutoWeb\template trabajrlos desde alli en caso de aregar algun otro. 

en form.py tenemos los formularios correspondiente a cada modelo. 
#Investigando consegui esta forma de generar la clase, con los mismo atributos del models-

Desde la URL #http://127.0.0.1:8000/RoseCoder/inicio podra verificar las funcinalidades, 
en la parte superio tenemos cada boton que nos indica que accion podemos realizar


#http://127.0.0.1:8000/RoseCoder/Personas << aca tenemos un formulario con campo nombre apellido y fecha de nacimiento. este ultimo siendo un cado date,
en caso de que no sea una fecha la incluida indicara error. 

#http://127.0.0.1:8000/RoseCoder/escuderia << aca poseemos tres campos nombre escuderias y piloto. el campo escuderia posee una lista la cual se despliega con las opciones 
validadas. 

#http://127.0.0.1:8000/RoseCoder/circuitos <<< aca tenemos un campo el cual es una lista con los datos validos en funcion al proyecto. al elegir la opcion
nos indica con un mensaje que fue correcto y nos redirije a la pagina de inicio.

#http://127.0.0.1:8000/RoseCoder/Busqueda << aca podemos realizar la busqueda por medio del nombre, hacia la BD en caso de que no exista el dato en la BD,
nos indicque que debemos registranos en el link formulario. 

BD SQLLIT3

tables principales: 

select * from  AutoWeb_circuito  
select* from AutoWeb_Escuderias
select * from  AutoWeb_persona


