#from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView, TemplateView
from core_app.correo import  correo
from core_app.sensores import  alarmas
from core_app.models import Inmueble, Elemento, Evento, Alarma, Sensor, TipoSensor
from MySmartHome.settings import NAME_DB, USER_DB, HOST_DB, PWD_DB
import psycopg2
import datetime
from core_app.forms import AlarmForm,AlarmaHumoForm,AlarmaEstadoForm, AlarmaEstado2Form
from django.forms.formsets import formset_factory, BaseFormSet
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from core_app.models import Alarma,AlarmaHumo,AlarmaEstado
from django.http import HttpResponseRedirect


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
    context_object_name = 'even_list'
    template_name = 'core_app/even_list.html'
    
    def get_queryset(self):
        user = self.request.user
        fecha1  = None# '2015-01-01'#'2015-01-19' #self.request.GET['fech_1']
        fecha2  = None#'2015-03-19'# '2015-02-18''2015-03-01'#self.request.GET['fech_1']
#        start_date = datetime.date(2005, 1, 1)
#        end_date = datetime.date(2005, 3, 31)       
        result = {}
        if (user.id != None):
            i = alarmas.Alarma()
            eventos = i.consul_events(user_id = user.id, fech_1 = fecha1, fech_2 = fecha2)
            result['eventos'] = eventos
            
        return result
        

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
class AlarmsView(TemplateView):

    def post(self,request):

        class RequiredFormSet(BaseFormSet):
            def __init__(self, *args, **kwargs):
                super(RequiredFormSet, self).__init__(*args, **kwargs)
                for form in self.forms:
                    form.empty_permitted = False

        alarma_id = self.request.POST['alarma_id']

        if alarma_id=='0' :
            AlarmFormSet = formset_factory(AlarmaHumoForm, extra=1, max_num=10, formset=RequiredFormSet)
        elif alarma_id=='1':
            AlarmFormSet = formset_factory(AlarmaEstadoForm, extra=1, max_num=10, formset=RequiredFormSet)
        elif alarma_id=='2':
            AlarmFormSet = formset_factory(AlarmaEstado2Form, extra=1, max_num=10, formset=RequiredFormSet)
        elif alarma_id=='3':
            AlarmFormSet = formset_factory(AlarmaAccesoForm, extra=1, max_num=10, formset=RequiredFormSet)    
        
        alarma_formset = AlarmFormSet(request.POST, request.FILES)
        
        if alarma_formset.is_valid():
            for form in alarma_formset.forms:
                alarma = form.save(commit=False)
                if alarma_id=='2':
                    alarma.estado_sensor=form.estado_sensor
                alarma.save()
        
        return HttpResponseRedirect('../')

    def get(self,request):
        
        class RequiredFormSet(BaseFormSet):
            def __init__(self, *args, **kwargs):
                super(RequiredFormSet, self).__init__(*args, **kwargs)
                for form in self.forms:
                    form.empty_permitted = False

    #extra 1 para que me pinte 1 formulario al mismo tiempo
        alarma_id = self.request.GET['alarma_id']

        if alarma_id=='0' :
            tipo_sensores = TipoSensor.objects.all().filter(id=alarma_id)
            primer_tipo_sensor = tipo_sensores[0]
            sensores = Sensor.objects.all().filter(tipo_sensor_id=primer_tipo_sensor.id)
            alarmas = Alarma.objects.all().filter( sensor_id= sensores.id)#.order_by('id') #Select * from Todo ;
        elif alarma_id=='1':
            tipo_sensores = TipoSensor.objects.all().filter(id=alarma_id)
            primer_tipo_sensor = tipo_sensores[0]
            sensores = Sensor.objects.all().filter(tipo_sensor_id=primer_tipo_sensor.id)
            alarmas = Alarma.objects.all().filter( sensor_id= sensores.id)#.order_by('id') #Select * from Todo ;
        elif alarma_id=='2':
            alarmas = Alarma.objects.all().filter(id = alarma_id)#.order_by('id') #Select * from Todo ;
        elif alarma_id=='3':
            alarmas = Alarma.objects.all().filter(id = alarma_id)#.order_by('id') #Select * from Todo ;
        else:
            alarmas = Alarma.objects.all()#.order_by('id') #Select * from Todo ;
    
        AlarmFormSet = formset_factory(AlarmaEstado2Form, extra=1, max_num=10, formset=RequiredFormSet)
        alarma_formset = AlarmFormSet()

        return  render_to_response('core_app/myform.html', locals(),
                                RequestContext(request))

