from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lbj_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': './media/'}),
    url(r'^survey/', include('survey.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
