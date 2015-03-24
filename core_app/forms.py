from django import forms
from core_app.models import Alarma,AlarmaHumo,AlarmaEstado

class AlarmForm(forms.Form):

    nombre = forms.CharField()
    valor = forms.CharField(3)
    valorMin = forms.CharField(4)
    valorMax = forms.CharField(5)


class AlarmaHumoForm(forms.ModelForm):
	class Meta:
		model = AlarmaHumo
		exclude = ('eliminada',)

class AlarmaEstadoForm(forms.ModelForm):
	class Meta:
		model = AlarmaEstado
		exclude = ('eliminada',)
		#exclude = ('fktodo',)

class AlarmaEstado2Form(forms.ModelForm):
	estado_sensor = forms.BooleanField(help_text='0=apagado 1=Encendido')
	class Meta:
		model = AlarmaEstado

		exclude = ('eliminada', 'estado_sensor',)
		
		#exclude = ('fktodo',)

