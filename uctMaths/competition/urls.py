from django.conf.urls import patterns, url
from competition import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	#url(r'^$', views.current_datetime, name='current_datetime')   
)