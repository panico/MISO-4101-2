#from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from core_app.correo import  correo
from core_app.models import Inmueble, Elemento, Alarma
from MySmartHome.settings import NAME_DB, USER_DB, HOST_DB, PWD_DB
import psycopg2
from core_app.forms import AlarmForm

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

#Este es un cambio de prueba para el Codeship
class CodeShipTest(ListView):
    context_object_name = 'info'
    template_name = 'core_app/home_list.html'


#vista de alarmas
class AlarmsListView(ListView):
    context_object_name = 'result'
    template_name = 'core_app/alarms_list.html'

    def get_queryset(self):        
        user = self.request.user
        alarmas = Alarma.objects.all()
        resultado = {}

        if(alarmas.__len__() > 0):
            resultado['alarmas'] = alarmas
            primer_alarma = alarmas[0]




        
        return resultado

#creacion de alarmas
class AlarmCreateView(CreateView):
    model = Alarma
    fields = ['nombre', 'estado', 'sensor']
    success_url = '/app/alarms'

    def form_valid(self, form):
        #form.instance.grupo.queryset = Grupo.objects.filter(users__id = user.id)
        
        return super(AlarmCreateView, self).form_valid(form)


#creacion de alarmas
class AlarmFormView(FormView):
    template_name = 'core_app/myform.html'
    form_class = AlarmForm
    success_url = '/app/alarms'

    
    def form_valid(self, form):

        connection=psycopg2.connect("host=" + HOST_DB + " dbname=" + NAME_DB + " user=" + USER_DB + " password=" + PWD_DB )
        cursor=connection.cursor()

        cursor.execute("UPDATE core_app_alarma SET name = " + str(self.nombre) + " WHERE id = " + "0")
        print(str(self))
        connection.commit()
        #form.instance.grupo.queryset = Grupo.objects.filter(users__id = user.id)
        return super(AlarmFormView, self).form_valid(form)
