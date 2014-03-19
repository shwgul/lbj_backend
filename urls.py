from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lbj_server.views.home', name='home'),
    # url(r'^lbj_server/', include('lbj_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': './media/'}),
    url(r'^survey/makemember', 'survey.views.makesun'),
    url(r'^survey/$', 'survey.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
