from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#actual site urls
    url(r'^competition/', include('competition.urls')),

    #admin and admin docs
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #allauth
    url(r'^accounts/', include('allauth.urls')),
    #endallauth
)
