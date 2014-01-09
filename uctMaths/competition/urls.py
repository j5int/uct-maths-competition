from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from competition import views, compadmin_views


urlpatterns = patterns('',

	#registration views
    url(r'^register/school_select/', views.school_select, name='school_select'),
	url(r'^register/students/', views.newstudents, name='newstudents'),
	url(r'^register/submitted', views.submitted, name='submitted'),
	url(r'^register/entry_review', views.entry_review, name='entry_review'),
	url(r'^accounts/profile/$',views.profile),
	url(r'^admin/upload_results',compadmin_views.upload_results, name='upload_results'),
)
