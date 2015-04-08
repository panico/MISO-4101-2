from django import forms
from django.forms.widgets import Widget, Select, MultiWidget
from core_app.models import Alarma,AlarmaHumo,AlarmaEstado,AlarmaAcceso, Elemento
from core_app.snipe import SelectTimeWidget


#BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
#favorite_colors = forms.MultipleChoiceField(required=False,
#     widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)



# Force minutes and seconds to be displayed in increments of 10
#t = forms.TimeField(widget=SelectTimeWidget(minute_step=10, second_step=10))

# Use a 12-hr time format, which will display a 4th select 
# element containing a.m. and p.m. options)
#t = forms.TimeField(widget=SelectTimeWidget(twelve_hr=True))
class AlarmForm(forms.Form):

	class Meta:
		model = Alarma
		exclude = ('eliminada',)

class AlarmaHumoForm(forms.ModelForm):

	sensor = forms.ChoiceField(required=False)
	nivel = forms.ChoiceField(required=False)
	class Meta:
		model = AlarmaHumo
		exclude = ('eliminada','sensor','nivel_alarma')

class AlarmaEstadoForm(forms.ModelForm):
	
	sensor = forms.ChoiceField(required=False)
	#hora_inicial = forms.TimeField(widget=SelectTimeWidget(twelve_hr=True))
	#hora_final = forms.TimeField(widget=SelectTimeWidget(twelve_hr=True))
	#hora_inicial = forms.TimeField()
	#hora_final = forms.TimeField()
	estado = forms.BooleanField(required=False,help_text='Cerrado=[] Abierto=[X]')
	nivel = forms.ChoiceField(required=False)
	
	class Meta:
		model = AlarmaEstado
		exclude = ('eliminada', 'estado_sensor','nivel_alarma','sensor')

class AlarmaEstado2Form(forms.ModelForm):
	sensor = forms.ChoiceField(required=False)
	#hora_inicial = forms.TimeField()
	#hora_final = forms.TimeField()
	#hora_inicial = forms.TimeField(widget=SelectTimeWidget(twelve_hr=True))
	#hora_final = forms.TimeField(widget=SelectTimeWidget(twelve_hr=True))
	estado = forms.BooleanField(required=False, help_text='apagado=[] Encendido=[X]')
	nivel = forms.ChoiceField(required=False)
	
	class Meta:
		model = AlarmaEstado
		exclude = ('eliminada', 'estado_sensor','nivel_alarma','sensor')

class AlarmaAccesoForm(forms.ModelForm):
	sensor = forms.ChoiceField(required=False)
	nivel = forms.ChoiceField(required=False)
	#hora_inicial = forms.TimeField()
	#hora_final = forms.TimeField()
	#hora_inicial = forms.TimeField(widget=SelectTimeWidget(twelve_hr=True))
	#hora_final = forms.TimeField(widget=SelectTimeWidget(twelve_hr=True))
	class Meta:
		model = AlarmaAcceso
		exclude = ('eliminada', 'estado_sensor','nivel_alarma','sensor')

class ElementoForm(forms.ModelForm):
	#sensor = forms.CharField(max_length=50, min_length=1)
	class Meta:
		model = Elemento
		exclude = ('inmueble', 'user','estado')