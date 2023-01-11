from django.conf.urls import url
from django.views.generic.base import TemplateView
from competition import views, compadmin_views

urlpatterns = [
	#registration views
    url(r'^register/school_select/', views.school_select, name='school_select'),
	url(r'^register/students/', views.newstudents, name='newstudents'),
	url(r'^register/submitted', views.submitted, name='submitted'),
	url(r'^register/entry_review', views.entry_review, name='entry_review'),	
	url(r'^register/printer_entry', views.printer_entry, name='printer_entry'),
	url(r'^register/school_report', views.printer_entry, name='school_report'),
	url(r'^accounts/profile/$',views.profile),
	url(r'^admin/upload_results',compadmin_views.upload_results, name='upload_results'),
	url(r'^admin/upload_declaration',compadmin_views.upload_declaration, name='upload_declaration'),
	url(r'^register/school_results',views.school_results, name='school_results'),
	url(r'^register/answer_sheets',views.answer_sheets, name="answer_sheets"),
	url(r'^register/school_certificates', views.school_certificates, name="school_certificates")
]
