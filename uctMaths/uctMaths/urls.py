from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from competition import views

admin.autodiscover()

urlpatterns = [
	#the sign in/up page at root
	url(r'^$', views.index, name='index'),
	
	#password reset
	url(r'^resetpassword/$', password_reset),
	url(r'^resetpassword/passwordsent/$', password_reset_done),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete),
	url(r'^account/', include('django.contrib.auth.urls')),
	
	#Aurelia is not quite sure what this does. It make the login work.
	# url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
	url(r'^accounts/profile/$', views.profile, name='profile'),

	#loads competitions/urls.py
    url(r'^competition/', include('competition.urls')),


    #admin and admin docs
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #load allauth/urls.py
    url(r'^accounts/', include('allauth.urls'))
]
