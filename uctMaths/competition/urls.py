from django.conf.urls import patterns, url

from competition import views

urlpatterns = patterns('',
  url(r'^$', views.tester, name='tester'),
  #url(r'^$', views.current_datetime, name='current_datetime')
  
    
)