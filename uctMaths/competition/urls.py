from django.conf.urls import patterns, url
from competition import views


urlpatterns = patterns('',
	url(r'^test/', views.tester, name='tester'),
	url(r'^$', views.index, name='index'),


)
