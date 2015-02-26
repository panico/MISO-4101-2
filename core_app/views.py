#from django.shortcuts import render
from django.views.generic import ListView
from core_app.correo import  correo
#==========================================================
#Clase que gestiona los atributos requeridos por el home
#==========================================================
class HomeListView(ListView):
    context_object_name = 'app_list' 
    
    def get_queryset(self):
        #user = self.request.user;
        return [];

class CorreoView(ListView):
    context_object_name = 'correo_envio' 
    def get_queryset(self):        
        user = self.request.user
        c = correo.myCorreo()
        c.enviarGmail(tipo_alarma=self.request.GET['alerta_id'],
                      destinatario=user.email,activo="Televisor")
        #return [];
