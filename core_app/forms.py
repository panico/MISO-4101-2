from django import forms
from core_app.models import Alarma

class AlarmForm(forms.Form):

    nombre = forms.CharField()
    valor = forms.CharField(3)
    valorMin = forms.CharField(4)
    valorMax = forms.CharField(5)

    def __init__(self, nombre):
        self.nombre = nombre 
