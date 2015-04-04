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
#    url(r'^even_inm/$', login_required(views.EventosView.as_view(template_name='core_app/even_list.html')), name='even_inm_list'),
#    url(r'^even_elm/$', login_required(views.EventosView.as_view(template_name='core_app/even_list.html')), name='even_elm_list'),
    url(r'^correo/envio/$', login_required(views.CorreoView.as_view(template_name='core_app/correo_detail.html')), name='correo_envio'),
    #url(r'^$', login_required(views.HomeListView.as_view()), name='home_list'),                           
    url(r'^elementos/$', login_required(views.EventosView.as_view(template_name='core_app/elementos_form.html')), name='elementos_form'),
    url(r'^elementos/notificacion/$', login_required(views.EventosView.as_view(template_name='core_app/elementos_notif.html')), name='elementos_notif')
)