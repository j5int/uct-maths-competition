from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from competition import views


urlpatterns = patterns('',
<<<<<<< HEAD
	url(r'^$', views.index, name='mths.uct.ac.za'),
=======

	#url(r'^$', views.index, name='mths.uct.ac.za'),
>>>>>>> 15e2793510d8fd37350319c28874882a4fa0eb86
	#original umc sidebar
	url(r'^content/', views.content, name='content'),
	#original umc home
	url(r'^main/', views.main, name='main'),

	#new form for student registration (start)
	url(r'^regStudent/', views.regStudent, name='regStudent'),
	url(r'^regSchool/', views.regSchool, name='regStudent'),

	#test search bars
<<<<<<< HEAD
	url(r'^search-form/$', views.search_form),
	url(r'^search/$', views.search),	
=======
	#url(r'^search-form/$', views.search_form),
	#url(r'^search/$', views.search),
	

>>>>>>> 15e2793510d8fd37350319c28874882a4fa0eb86
	
	url(r'^accounts/profile/$',views.profile),

)
