#from django.shortcuts import render
from django.views.generic import ListView
from core_app.correo import  correo
#==========================================================
#Clase que gestiona los atributos requeridos por el home
#==========================================================
class HomeListView(ListView):
    context_object_name = 'app_list' 
    
    def get_queryset(self):
        c = correo.myCorreo()
        c.enviarGmail()
        #user = self.request.user;
        return [];