from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from competition import views


urlpatterns = patterns('',
	#original mth.uct.ac.za home
	url(r'^$', views.index, name='mths.uct.ac.za'),
	#original umc sidebar
	url(r'^content/', views.content, name='content'),
	#original umc home
	url(r'^main/', views.main, name='main'),

	#new form for student registration (start)
	url(r'^regStudent/', views.regStudent, name='regStudent'),

	#test search bars
	url(r'^search-form/$', views.search_form),
	url(r'^search/$', views.search),
	
	#url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),


)
