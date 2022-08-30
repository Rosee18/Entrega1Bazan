from django.db import models

# Create your models here.

#clase para el registros de las personas
class Persona(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_Nacimiento= models.DateField()
    
   
   
    
 
#creo la clase circuento, para elegir el circueto favorito

class Circuito(models.Model):
    
    #creo la lista de circueto a elegir. NO se agrega el GP de Rusia. 
    
    circuitos= [
        
         ('GP de Bahrein','GP de Bahrein'),
         ('GP de Arabia Saudí','GP de Arabia Saudí'),
         ('GP de Australia','GP de Australia'),
         ('GP de Emilia-Romagna','GP de Emilia-Romagna'),
         ('GP de Miami','GP de Miami'),
         ('GP de España','GP de España'),
         ('GP de Mónaco','GP de Mónaco'),
         ('GP de Azerbaiyán','GP de Azerbaiyán'),
         ('GP de Canadá','GP de Canadá'),
         ('GP de Gran Bretaña','GP de Gran Bretaña'),
         ('GP de Austria','GP de Austria',),
         ('GP de Francia','GP de Francia'),
         ('GP de Hungría','GP de Hungría'),
         ('GP de Bélgica','GP de Bélgica'),
         ('GP de Países Bajos','GP de Países Bajos'),
         ('GP de Italia','GP de Italia'),
         ('GP de Singapur','GP de Singapur'),
         ('GP de Japón','GP de Japón'),
         ('GP de EE UU','GP de EE UU'),
         ('GP de Ciudad de México','GP de Ciudad de México'),
         ('GP de Sao Paulo','GP de Sao Paulo'),
         ('GP de Abu Dhabi','GP de Abu Dhabi')
    ]
    
    circuito= models.CharField(max_length=23, choices=circuitos, default='GP de Sao Paulo')
    
    
    

    

#creo la clase autos, ara las escuderias  
class Autos(models.Model):
    nombre = models.CharField(max_length=30)
    
    escuderias= [
        ('Ferrari','Ferrari'),
        ('Mercedes','Mercedes'),
        ('Alpine','Alpine'),
        ('Haas','Haas'),
        ('Alfa Romeo','Alfa Romeo'),
        ('Aston Martin','Aston Martin'),
        ('Alphatauri','Alphatauri'),
        ('Williams','Williams'),
        ('Red Bull','Red Bull'),
        ('Mclaren','Mclaren'),
        
    ]
    
    escuderias = models.CharField(max_length=30,choices=escuderias,default='Alfa Romeo')
    piloto = models.IntegerField()
        
    
    
    
    


