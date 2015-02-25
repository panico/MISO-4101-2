from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# Clase que representa cada una de las pertenencias de un usuario 
class Activo(models.Model):
    user = models.ForeignKey(User)
    
    class Meta:
        ordering = ['id']
        
    #Representación como cadena del objeto
    def __str__(self):
        return self.id


class Proyecto(models.Model):
    pass

#Clase que representa las propiedades del usuario fijas como Apto, Oficina, etc 
class Inmueble(Activo):
    proyecto = models.ForeignKey(Proyecto)
    activos = [];
    
    def append_element(self, element):
        self.activos.append(element)

    def remove_element(self, element):
        self.activos.remove(element)
    

#Clase que representa los electrodomésticos y demás elementos dentro de un inmueble
class Elemento(Activo):
    pass

#Clase que representa a un sensor físico (RFID, Gases, Incendio, etc) 
class Sensor(models.Model):
    activo = models.ForeignKey(Activo)

#Clase que representa los eventos generados por un sensor
class Evento(models.Model):
    sensor = models.ForeignKey(Sensor)

#Clase que representa las alarmas que pueden ser configuradas para un sensor/evento
class Alarma(models.Model):
    sensor = models.ForeignKey(Sensor)

#Clase que representa todos los parámetros configurables de una alarma (pe. MinTemperatura)
class AlarmaParametro(models.Model):
    pass
