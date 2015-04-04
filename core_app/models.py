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
#Clase que tiene los tipos de sensores
class TipoSensor(GenericModelWithName):
    descripcion = models.CharField(max_length=255)
#Clase que representa a un sensor físico (RFID, Gases, Incendio, etc) 
class Sensor(GenericModelWithName):
    #Objeto/Inmueble al que se asocia el sensor
    activo = models.ForeignKey(Elemento)
    tipo_sensor = models.ForeignKey(TipoSensor)

#Clase que representa los eventos generados por un sensor
class Evento(GenericModelWithName): #GenericModel
#    id = models.AutoField(primary_key=True)
    codigo  = models.CharField(max_length=10)
#    descripcion = models.CharField(max_length=1000)
    trama   = models.CharField(max_length=1000)
    fecha_hora_evento = models.DateTimeField()
    fecha_hora_sistema = models.DateTimeField()
    sensor   = models.ForeignKey(Sensor)
#    inmueble = models.ForeignKey(Inmueble)
# agregado 14/03/2015
#    inmueble = models.ForeignKey(Inmueble)
    

#Clase que representa las alarmas que pueden ser configuradas para un sensor/evento
class Alarma(GenericModelWithName):
    #Determina si la alarma se encuentra activada
    descripcion = models.CharField(max_length=512)
    usuario = models.ForeignKey(User)
    sensor = models.ForeignKey(Sensor)
    activa = models.BooleanField(default=True)
    notifica = models.BooleanField(default=True)
    eliminada = models.BooleanField(default=False)


#Clase que representa alarma de tipo Humo
class AlarmaHumo(Alarma):
    pass
#Clase que representa alarma de tipo Acceso
class AlarmaAcceso(Alarma):
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

#Clase que representa alarma de tipo Estado
class AlarmaEstado(Alarma):
    estado = models.BooleanField(default=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
#Alarmas reportadas
class AlarmaReportada(GenericModelWithName):
    descripcion = models.CharField(max_length=512)
    usuario = models.ForeignKey(User)
    alarma = models.ForeignKey(Alarma)
    fecha_hora = models.DateTimeField()
    nivel_alerta = models.IntegerField(default=2, validators=[MinValueValidator(0), MaxValueValidator(2)])



##Otras clases

class HistoryAlarmas(GenericModel):
    estado    = models.BooleanField(default=True)
    fecha     = models.DateTimeField()
    user      = models.ForeignKey(User)
    elemento  = models.ForeignKey(Elemento)
    inmueble  = models.ForeignKey(Inmueble)
    
    #parametro = models.ForeignKey(AlarmaParametro)

    sensor   = models.ForeignKey(Sensor)
    alarma   = models.ForeignKey(Alarma)