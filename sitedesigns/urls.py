from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from sitedesignsbase.views import index, contact, systaseis, works

urlpatterns = patterns('',
    url(r'^$',index,{'template_name': 'index.html'}),
    url(r'^contact/', contact, {'template_name': 'contact.html'}),
    url(r'^who_we_are/', systaseis, {'template_name': 'systaseis.html'}),
    url(r'^works/', works, {'template_name': 'works.html'}),
    url(r'^admin/', include(admin.site.urls))
)
