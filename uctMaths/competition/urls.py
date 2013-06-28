from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from competition import views


urlpatterns = patterns('',

	#table views
	url(r'^students/', views.students, name='students'),
	url(r'^schools/', views.schools, name='schools'),
	url(r'^invigilators/', views.invigilators, name='invigilators'),
	# url(r'^venues/', views.venues, name='venues'),

	#registration views
	url(r'^register/students/', views.newstudents, name='newstudents'),
	url(r'^register/schools/', views.newschools, name='newschools'),
	url(r'^register/invigilators/', views.newinvigilators, name='newinvigilators'),
	# url(r'^register/venues/', views.newvenues, name='newvenues'),

	url(r'^register/submitted', views.submitted, name='submitted'),

		
	url(r'^accounts/profile/$',views.profile),

)
