from django.conf.urls import patterns, url
from competition import views
from django.views.generic.base import TemplateView


urlpatterns = patterns('',
	url(r'^test/', views.tester, name='tester'),
	url(r'^$', views.index, name='index'),
	url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),


)
