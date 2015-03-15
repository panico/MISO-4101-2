#from django.shortcuts import render
from django.views.generic import ListView
from core_app.correo import  correo
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
        inmuebles = Inmueble.objects.all().filter(user_id = user.id)
        resultado = {}
        
        if(inmuebles.__len__() > 0):
            resultado['inmuebles'] = inmuebles
            
            if 'inmueble_id' in self.request.GET:
                inmueble_param_id = self.request.GET['inmueble_id']
                resultado['elementos'] = Elemento.objects.all().filter(
                     inmueble_id = inmueble_param_id, user_id = user.id)
            else:
                primer_inmueble = inmuebles[0]
                resultado['elementos'] = Elemento.objects.all().filter(
                     inmueble_id = primer_inmueble.id, user_id = user.id).order_by('-estado')
        
        return resultado
    
class EventosView(ListView):
    context_object_name = 'even_list'
    template_name = 'core_app/even_list.html'
    
    def get_queryset(self):
        user = self.request.user
        fecha1      = self.request.GET['fech_1']
        fecha2      = self.request.GET['fech_2']
#        start_date = datetime.date(2005, 1, 1)
#        end_date = datetime.date(2005, 3, 31)       
        result = {}
        inmbs = Inmueble.objects.filter(user = user.id)

        for im in inmbs.__len__():                
            elems = Elemento.objects.filter(inmueble = inmbs[im])
            if (elems.__len__() > 0):
                for e in elems.__len__():
                    if (fecha1 != None and fecha2 == None):
                        eventos = Evento.objects.all().filter(inmueble = inmbs[im], elemento = elems[e], 
                                                              fecha = fecha1).order_by('inmueble')
                        result['eventos'] = eventos
                    else:
                        if (fecha2 != None):
                            eventos = Evento.objects.filter(inmueble = inmbs[im], elemento = elems[e], 
                                                            pub_date__range=(fecha1, fecha2)).order_by('inmueble')
                            result['eventos'] = eventos
                        else:
                            result = "Debe registrar la fecha inicial"
            else:
                result = "Inmueble sin elementos"

        return result
        