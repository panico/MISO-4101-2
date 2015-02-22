from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    #url(r'^$', login_required(TemplateView.as_view(template_name='index.html'))),
    url(r'^$', RedirectView.as_view(url='/app/')),
    url(r'^app/', include('core_app.urls', namespace='app')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
)