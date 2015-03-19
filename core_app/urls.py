from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from core_app import views
#from django.views.generic import TemplateView

urlpatterns = patterns('',
    # ex: /app/
    url(r'^$', login_required(views.HomeListView.as_view()), name='home_list'),
    # ex: /grupo/
    url(r'^correo/$', login_required(views.HomeListView.as_view(template_name='core_app/correo_index.html')), name='correo_index'),
    url(r'^correo/envio/$', login_required(views.CorreoView.as_view(template_name='core_app/correo_detail.html')), name='correo_envio'),
    #url(r'^$', login_required(views.HomeListView.as_view()), name='home_list'),                           

    url(r'^alarms/$', login_required(views.AlarmsListView.as_view(template_name='core_app/alarms_list.html')), name='alarms_list'),
    url(r'^alarms/create/$', login_required(views.AlarmCreateView.as_view()), name='alarma_create'),

    url(r'^alarms/form/$', login_required(views.AlarmFormView.as_view()), name='alarma_form'),

)