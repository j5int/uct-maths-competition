from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from competition import views

admin.autodiscover()

urlpatterns = patterns('',
	#the sign in/up page at root
	url(r'^$', views.index, name='index'),
	
	#Aurelia is not quite sure what this does. It make the login work.
	# url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
	url(r'^accounts/profile/$', views.profile, name='profile'),

	#loads competitions/urls.py
    url(r'^competition/', include('competition.urls')),
    

    #admin and admin docs
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #load allauth/urls.py
    url(r'^accounts/', include('allauth.urls')),

)
