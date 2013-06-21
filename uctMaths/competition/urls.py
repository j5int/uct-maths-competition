from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from competition import views


urlpatterns = patterns('',

	#url(r'^$', views.index, name='mths.uct.ac.za'),
	#original umc sidebar
	url(r'^content/', views.content, name='content'),
	#original umc home
	url(r'^main/', views.main, name='main'),

	#table views
	url(r'^students/', views.students, name='students'),
	url(r'^schools/', views.schools, name='schools'),
	url(r'^invigilators/', views.invigilators, name='invigilators'),
	url(r'^venues/', views.venues, name='venues'),

	#registration views
	url(r'^register/students/', views.newstudents, name='newstudents'),
	url(r'^register/schools/', views.newschools, name='newschools'),
	url(r'^register/invigilators/', views.newinvigilators, name='newinvigilators'),
	url(r'^register/venues/', views.newvenues, name='newvenues'),
	#test search bars

	url(r'^search-form/$', views.search_form),
	#url(r'^search/$', views.search),
	
	url(r'^accounts/profile/$',views.profile),

)
