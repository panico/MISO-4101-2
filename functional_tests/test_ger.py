from django.test import TestCase, LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core import mail
from core_app import views
from core_app.models import Inmueble, Elemento, Proyecto
from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
      

class EstadoInmueble(FunctionalTest):#TestCase
    nombre = "Inmueble test"
    estado_inicial = 2
    estado_final = 1
    user = User.objects.create(username="test_user_last", password="pass", email="test@test.co")
    proyecto = Proyecto.objects.create(nombre="Proyecto_test")
    
    def setUp(self):
        c = Client()
        c.login(username="test_user_last", password='pass')

        #self.client.login(username="test_user", password="pass")
        self.inmueble = Inmueble.objects.create(nombre=self.nombre, estado=self.estado_inicial, user=self.user, proyecto=self.proyecto)
        self.inmueble.name = self.nombre
        self.inmueble.estado = self.estado_inicial
    #Método que verifica que el estado del inmueble cambie cuando se hace un set en el estado del inmueble
    def test_estado_inmueble(self):
        self.inmueble.set_estado(self.estado_final)
        self.assertTrue(self.estado_final==inmueble.estado)
    
        
#    def tearDown(self):
#        self.user.delete()
#        self.client.logout()
        
    

