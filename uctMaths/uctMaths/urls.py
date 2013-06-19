from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from competition import views

admin.autodiscover()

urlpatterns = patterns('',
	#actual site urls
	url(r'^$', views.allauthtest, name='allauthtest'),
    url(r'^competition/', include('competition.urls')),
    

    #admin and admin docs
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #allauth
    url(r'^accounts/', include('allauth.urls')),
    #endallauth
	
	#url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),


)
