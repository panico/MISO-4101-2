from django.test import TestCase, LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core import mail
from core_app import views
from core_app.models import Inmueble, Elemento
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import FunctionalTest

# Create your tests here.
class NotifyTest(FunctionalTest):    
    @classmethod
    def test_new_notify(self, a):
        if a:
            return self.assertEqual(a, 1)
        else:
            return self.assertEqual(a, 0)
    
    
    def test_changeNotify(self):
        data = HistoryAlarmas()
        
        if (data.estado == False):
            estado = True
            self.assertNotEqual(data.estado, estado)

  