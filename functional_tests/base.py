from django.test import TestCase, LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core import mail
from core_app import views
from core_app.models import Inmueble, Elemento
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

# Create your tests here.
class FunctionalTest(StaticLiveServerTestCase):
    username = 'hernan'
    password = '000000'
    email = 'hernan@uniandes.com'
    
    @classmethod
    def setUpClass(cls):
        #cls.wd = WebDriver()
        super(FunctionalTest, cls).setUpClass()
        
    @classmethod
    def tearDownClass(cls):
        #cls.wd.quit()
        super(FunctionalTest, cls).tearDownClass()
        
    #Método que se ejecuta al inicio de cada uno de los métodos de prueba
    def setUp(self):
        # Cada uno de los test necesita ser ejecutado en un cliente
        self.client = Client()
        #Para verificar el login, se debe primero crea el usuario con el que se va a probar
        self.user = User.objects.create_user(self.username, self.email, self.password)
    
    #Método que se ejecuta al final de cada uno de los métodos de prueba    
    def tearDown(self):
        self.user.delete()
        self.client.logout()
