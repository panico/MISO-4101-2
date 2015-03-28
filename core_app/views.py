#from django.shortcuts import render
from django.views.generic import ListView
from core_app.correo import  correo
from core_app.sensores import  alarmas
from core_app.models import Inmueble, Elemento, Evento
from MySmartHome.settings import NAME_DB, USER_DB, HOST_DB, PWD_DB
import psycopg2
import datetime

class CorreoListView(ListView):
    context_object_name = 'app_list' 
    
    def get_queryset(self):
        #user = self.request.user;
        return [];

class CorreoView(ListView):
    context_object_name = 'correo_envio' 
    def get_queryset(self):        
        user = self.request.user
        resultado = {}

        inmuebles = Inmueble.objects.all().filter(user_id = user.id)

        if(inmuebles.__len__() > 0):
            resultado['inmuebles'] = inmuebles

            primer_inmueble = inmuebles[0]
            resultado['elementos'] = Elemento.objects.all().filter(
                 inmueble_id = primer_inmueble.id, user_id = user.id).order_by('-estado')

            if(resultado['elementos'].__len__() > 0):
                primer_elemento = resultado['elementos'][0]

                c = correo.myCorreo()
                c.enviarGmail(tipo_alarma=self.request.GET['alerta_id'],
                          destinatario=user.email,activo=primer_elemento.nombre)

                connection=psycopg2.connect("host=" + HOST_DB + " dbname=" + NAME_DB + " user=" + USER_DB + " password=" + PWD_DB )
                cursor=connection.cursor()

                cursor.execute("UPDATE core_app_activo SET estado =" + str(self.request.GET['alerta_id']) + " WHERE id =" + str(primer_elemento.id))
                connection.commit()

        else:
            c = correo.myCorreo()
            c.enviarGmail(tipo_alarma=self.request.GET['alerta_id'],
                          destinatario=user.email,activo="Activo Ejemplo")
        #return [];
    
#==========================================================
#Clase que gestiona los atributos requeridos por el home
#==========================================================
class HomeListView(ListView):
    context_object_name = 'info'
    template_name = 'core_app/home_list.html'
    
    def get_queryset(self):
        user = self.request.user
        inmuebles = Inmueble.objects.all().filter(user_id = user.id).order_by('-estado')
        resultado = {}
        
        if(inmuebles.__len__() > 0):
            resultado['inmuebles'] = inmuebles
            
            if 'inmueble_id' in self.request.GET:
                inmueble_param_id = self.request.GET['inmueble_id']
                resultado['elementos'] = Elemento.objects.all().filter(
                     inmueble_id = inmueble_param_id, user_id = user.id).order_by('-estado')
                resultado['inmueble_actual'] = Inmueble.objects.get(pk=inmueble_param_id)
            else:
                primer_inmueble = inmuebles[0]
                resultado['elementos'] = Elemento.objects.all().filter(
                     inmueble_id = primer_inmueble.id, user_id = user.id).order_by('-estado')
                resultado['inmueble_actual'] = Inmueble.objects.get(pk=primer_inmueble.id)
        
        return resultado

class EventosView(ListView):
    context_object_name = 'info'
    template_name = 'core_app/even_list.html'
    
    def get_queryset(self):
                    
        user = self.request.user
        inmuebles = Inmueble.objects.all().filter(user_id = user.id).order_by('-estado')
        fecha1  = None#'2015-01-19' #self.request.GET['fech_1']
        fecha2  = None#'2015-03-19'# '2015-02-18''2015-03-01'#self.request.GET['fech_1']
#        start_date = datetime.date(2005, 1, 1)
#        end_date = datetime.date(2005, 3, 31)     
        resultado = {}
        i = alarmas.Alarma()
        resultado['inmuebles'] = inmuebles  
        if 'inmueble_id' in self.request.GET and self.request.GET['inmueble_id'] != "":
            inmb_id = self.request.GET['inmueble_id']
            resultado['inmueble_actual'] = Inmueble.objects.get(pk=inmb_id)
            resultado['elementos'] = Elemento.objects.all().filter(inmueble_id = inmb_id, user_id = user.id).order_by('-estado')
            eventos = i.consul_events_inmb(inmueb_id = inmb_id, fecha1 = fecha1, fecha2 = fecha2)
        else:
            if 'elemento_id' in self.request.GET and self.request.GET['elemento_id'] != "":
                elm_id = self.request.GET['elemento_id']
                resultado['elemento_actual'] = Elemento.objects.get(pk=elm_id)
                resultado['inmueble_actual'] = resultado['elemento_actual'].inmueble
                resultado['elementos'] = Elemento.objects.all().filter(inmueble_id = resultado['inmueble_actual'].id, user_id = user.id).order_by('-estado')
                eventos = i.consul_events_elem(elem_id = elm_id, fech_1 = fecha1, fech_2 = fecha2)
            else:
                if (user.id != None):
                    eventos = i.consul_events(user_id = user.id, fech_1 = fecha1, fech_2 = fecha2)
                    resultado['elementos'] = Elemento.objects.all().filter(user_id = user.id).order_by('-estado')
        
        resultado['eventos'] = eventos    
        return resultado
        

#Este es un cambio de prueba para el Codeship
class CodeShipTest(ListView):
    context_object_name = 'info'
    template_name = 'core_app/home_list.html'

