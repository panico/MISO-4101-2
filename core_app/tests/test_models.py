from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core import mail
from core_app.models import HistoryAlarmas, AlarmaReportada, Inmueble, Elemento, Evento, Sensor, AlarmaEstado, AlarmaAcceso, AlarmaHumo
from django.core.urlresolvers import reverse
import datetime
#from .base import FunctionalTest

class HistoryAlarmasTest(TestCase):

    def test_historyAlarmas(self):
        histalm = HistoryAlarmas()
#        self.assertEqual(histalm.sensor, '0')
        histalm.fecha = datetime.datetime.now() #datetime.timedelta(days=1) # 1 day ago
        self.assertNotEqual(histalm.estado, False)
        self.assertTrue(histalm.is_over())
    
#    def test_inmueble(self):
