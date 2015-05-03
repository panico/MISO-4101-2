from core_app.models import Proyecto, Activo, HistoryAlarmas, Inmueble, Elemento
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

    def test_Inmueble(self):

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

    