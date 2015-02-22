from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
#from core_app import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # ex: /app/
    url(r'^$', login_required(TemplateView.as_view(template_name='index.html'))),
    #url(r'^$', login_required(views.HomeListView.as_view()), name='home_list'),                           
)