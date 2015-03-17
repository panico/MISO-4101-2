from enum import IntEnum

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class GenericModel(models.Model):
    #Representación como cadena del objeto
    def __str__(self):
        return 'Objeto {className} con Id[{modelId}]'.format(
            className=self.__class__.__name__, modelId=self.id)
    
    class Meta: 
        abstract = True
        
class GenericModelWithName(GenericModel):
    nombre = models.CharField(max_length=255, default='')
    
    class Meta: 
        abstract = True
        
    #Representación como cadena del objeto
    def __str__(self):
        return self.nombre


# Create your models here.
# Clase que representa cada una de las pertenencias de un usuario
class NivelAlerta(IntEnum):
    ROJO = 0
    AMARILLO = 1
    VERDE = 2
    
class Activo(GenericModelWithName):
    user = models.ForeignKey(User)
    #Contiene el estado actual notificado por un evento sobre el activo
    estado = models.IntegerField(default=2, validators=[MinValueValidator(0), MaxValueValidator(2)])
    
    class Meta:
        ordering = ['estado']
        
#Clase que agrupa los inmuebles
class Proyecto(GenericModelWithName):
    pass
    
#Clase que representa las propiedades del usuario fijas como Apto, Oficina, etc 
class Inmueble(Activo):
    proyecto = models.ForeignKey(Proyecto)
    #activos = models.ManyToManyField(Activo, related_name='inmuebles_activos_type', null=True)
    
#Clase que representa los electrodomésticos y demás elementos dentro de un inmueble
class Elemento(Activo):
    inmueble = models.ForeignKey(Inmueble)

#Clase que representa a un sensor físico (RFID, Gases, Incendio, etc) 
class Sensor(GenericModelWithName):
    #Objeto/Inmueble al que se asocia el sensor
    activo = models.ForeignKey(Activo)

#Clase que representa los eventos generados por un sensor
class Evento(GenericModel): #GenericModel
#    id = models.AutoField(primary_key=True)
    codigo  = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=1000)
    trama   = models.CharField(max_length=1000)
    fecha   = models.DateTimeField()
    prioridad = models.CharField(max_length=1)
    tipoEven    = models.CharField(max_length=2)
    sensor = models.ForeignKey(Sensor)
    elemento = models.ForeignKey(Elemento)
# agregado 14/03/2015
#    inmueble = models.ForeignKey(Inmueble)
    

#Clase que representa las alarmas que pueden ser configuradas para un sensor/evento
class Alarma(GenericModelWithName):
    #Determina si la alarma se encuentra activada
    estado = models.BooleanField(default=True)
    sensor = models.ForeignKey(Sensor)

#Clase que representa todos los parámetros configurables de una alarma (pe. MinTemperatura)
class AlarmaParametro(GenericModelWithName):
    valor = models.CharField(max_length=255)
    valorMin = models.IntegerField();
    valorMax = models.IntegerField();
    nivel = models.IntegerField(default=2, validators=[MinValueValidator(0), MaxValueValidator(2)])
    alarma = models.ForeignKey(Alarma)

class HistoryAlarmas(GenericModelWithName):
    estado    = models.BooleanField(default=True)
    fecha     = models.DateTimeField()
    user      = models.ForeignKey(User)
    inmueble  = models.ForeignKey(Inmueble)
    parametro = models.ForeignKey(AlarmaParametro)

#    sensor   = models.ForeignKey(Sensor)
#    alarma   = models.ForeignKey(Alarma)