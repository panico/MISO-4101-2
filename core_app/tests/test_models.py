from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core import mail
from core_app.models import Proyecto, Activo, HistoryAlarmas, AlarmaReportada, Inmueble, Elemento, Evento, Sensor, AlarmaEstado, AlarmaAcceso, AlarmaHumo
from django.core.urlresolvers import reverse
import datetime
from functional_tests.base import FunctionalTest

class HistoryAlarmasTest(FunctionalTest):#TestCase
    
    def test_historyAlarmas(self):
        histalm = HistoryAlarmas()
#        self.assertEqual(histalm.sensor, '0')
        histalm.fecha = datetime.datetime.now() #datetime.timedelta(days=1) # 1 day ago
        self.assertNotEqual(histalm.estado, False)
        self.assertTrue(histalm.is_over())

class InmuebleTest(FunctionalTest):
    nom_inm = "Inmueble test"
    estado_inicial_inmueble = 2
    estado_final_inmueble = 1
    
    nom_elm = "Elemento test"
    estado_inicial_elemento = 2
    estado_final_elemento = 1
#    def test_inmueble(self):
    def test_Inmueble(self):
#        self.client = Client()        
#        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.proyecto = Proyecto.objects.create(nombre="Proyecto_test")
        self.activo_to_inmueble = Activo.objects.create(user=self.user)
        self.activo_to_elemento = Activo.objects.create(user=self.user)
        self.inmueble = Inmueble(activo_ptr=self.activo_to_inmueble, proyecto = self.proyecto)
#        self.inmueble.name = self.nombre
        self.inmueble.name = self.nom_inm
        self.inmueble.estado = self.estado_inicial_inmueble
        
        self.assertNotEqual(self.inmueble.name, '')
        self.assertEqual(self.inmueble.estado, 2)
        
        self.elemento = Elemento(activo_ptr=self.activo_to_elemento, inmueble = self.inmueble)
        self.elemento.name = self.nom_elm
        self.elemento.estado = self.estado_inicial_elemento
        
        self.assertNotEqual(self.elemento.name, '')
        self.assertEqual(self.elemento.estado, 2)

    