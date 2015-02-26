from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
#from core_app import views
from core_app import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # ex: /app/
    url(r'^$', login_required(TemplateView.as_view(template_name='index.html'))),
    # ex: /grupo/
    url(r'^correo/$', login_required(views.HomeListView.as_view(template_name='core_app/correo_index.html')), name='correo_index'),
    url(r'^correo/envio/$', login_required(views.CorreoView.as_view(template_name='core_app/correo_detail.html')), name='correo_envio'),
    #url(r'^$', login_required(views.HomeListView.as_view()), name='home_list'),                           
)