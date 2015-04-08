from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from core_app import views
#from django.views.generic import TemplateView

urlpatterns = patterns('',
    # ex: /app/
    url(r'^$', login_required(views.HomeListView.as_view()), name='home_list'),
    # ex: /grupo/
    url(r'^correo/$', login_required(views.HomeListView.as_view(template_name='core_app/correo_index.html')), name='correo_index'),

    url(r'^eventos/$', login_required(views.EventosView.as_view(template_name='core_app/even_list.html')), name='even_list'),

    url(r'^history/$', login_required(views.AlarmReportsView.as_view(template_name='core_app/alarmas_history.html')), name='alarmas_history'),
    
    url(r'^tipo_alarmas/$', login_required(views.TipoAlarmsView.as_view(template_name='core_app/tipo_alarmas.html')),name='tipo_alarmas'),
    url(r'^alarmas/$', login_required(views.AlarmsListView.as_view(template_name='core_app/alarmas_lista.html')), name='alarmas_lista'),
    url(r'^alarmas/editar_alarmas/$', login_required(views.AlarmsEditView.as_view(template_name='core_app/alarmas_detalle.html')), name='alarmas_detalle'),
    url(r'^alarmas/crear_alarmas/$', login_required(views.AlarmsView.as_view(template_name='core_app/crear_alarma.html')), name='alarmas_lista'),
    #url(r'^alarmas/$', login_required(views.AlarmCreateView.as_view(template_name='core_app/alarma_lista.html')),name='alarma_creacion'),

    # ex: /elemento/create/
    #url(r'^create/$', login_required(views.ElemCreateView.as_view()), name='elem_create'),
     url(r'^create/$', login_required(views.CrearElementoView.as_view(template_name='core_app/crear_elemento.html')), name='crear_elemento'),
    
    # ex: /agenda/5/
    url(r'^(?P<pk>\d+)/$', login_required(views.ElemDetailView.as_view()), name='elem_detail'),
    # ex: /agenda/1/update/
    url(r'^(?P<pk>\d+)/update/$', login_required(views.ElemUpdateView.as_view()), name='elem_update'),

#    url(r'^even_inm/$', login_required(views.EventosView.as_view(template_name='core_app/even_list.html')), name='even_inm_list'),
#    url(r'^even_elm/$', login_required(views.EventosView.as_view(template_name='core_app/even_list.html')), name='even_elm_list'),

    url(r'^correo/envio/$', login_required(views.CorreoView.as_view(template_name='core_app/correo_detail.html')), name='correo_envio'),
    #url(r'^$', login_required(views.HomeListView.as_view()), name='home_list'),                           

    url(r'^alarms/$', login_required(views.AlarmsListView.as_view(template_name='core_app/alarms_list.html')), name='alarms_list'),

)