from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from core_app import views
#from django.views.generic import TemplateView

urlpatterns = patterns('',
    # ex: /app/
    url(r'^$', login_required(views.HomeListView.as_view()), name='home_list'),
    # ex: /grupo/
    url(r'^correo/$', login_required(views.HomeListView.as_view(template_name='core_app/correo_index.html')), name='correo_index'),
    #url(r'^alarmas/$', login_required(views.EventosView.as_view(template_name='core_app/even_list.html')), name='even_list'),
    url(r'^alarmas/$', login_required(views.AlarmCreateView.as_view(template_name='core_app/alarma_lista.html')),name='alarma_creacion'),
    url(r'^correo/envio/$', login_required(views.CorreoView.as_view(template_name='core_app/correo_detail.html')), name='correo_envio'),
    #url(r'^$', login_required(views.HomeListView.as_view()), name='home_list'),                           

    url(r'^alarms/$', login_required(views.AlarmsListView.as_view(template_name='core_app/alarms_list.html')), name='alarms_list'),

)