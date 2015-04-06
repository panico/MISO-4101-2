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
    # ex: /elemento/create/
    url(r'^create/$', login_required(views.ElemCreateView.as_view()), name='elem_create'),
    # ex: /agenda/5/
    url(r'^(?P<pk>\d+)/$', login_required(views.ElemDetailView.as_view()), name='elem_detail'),
    # ex: /agenda/1/update/
    url(r'^(?P<pk>\d+)/update/$', login_required(views.ElemUpdateView.as_view()), name='elem_update'),
#    url(r'^even_inm/$', login_required(views.EventosView.as_view(template_name='core_app/even_list.html')), name='even_inm_list'),
#    url(r'^even_elm/$', login_required(views.EventosView.as_view(template_name='core_app/even_list.html')), name='even_elm_list'),
    url(r'^correo/envio/$', login_required(views.CorreoView.as_view(template_name='core_app/correo_detail.html')), name='correo_envio'),
    #url(r'^$', login_required(views.HomeListView.as_view()), name='home_list'),                           

)