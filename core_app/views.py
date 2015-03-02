#from django.shortcuts import render
from django.views.generic import ListView
from core_app.correo import  correo
from core_app.models import Inmueble, Elemento

class CorreoListView(ListView):
    context_object_name = 'app_list' 
    
    def get_queryset(self):
        c = correo.myCorreo()
        c.enviarGmail()
        #user = self.request.user;
        return [];
    
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
                     inmueble_id = primer_inmueble.id, user_id = user.id)
#        print (resultado.keys())  
        return resultado