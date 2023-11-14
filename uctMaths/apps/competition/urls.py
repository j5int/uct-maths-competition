from django.urls import path

from apps.competition import compadmin_views, views

urlpatterns = [
	#registration views
    path(r'^register/school_select/', views.school_select, name='school_select'),
	path(r'^register/students/', views.newstudents, name='newstudents'),
	path(r'^register/submitted', views.submitted, name='submitted'),
	path(r'^register/entry_review', views.entry_review, name='entry_review'),
	path(r'^register/printer_entry', views.printer_entry, name='printer_entry'),
	path(r'^register/school_report', views.printer_entry, name='school_report'),
	path(r'^accounts/profile/$', views.profile),
	path(r'^admin/upload_results', compadmin_views.upload_results, name='upload_results'),
	path(r'^admin/upload_declaration', compadmin_views.upload_declaration, name='upload_declaration'),
	path(r'^register/school_results', views.school_results, name='school_results'),
	path(r'^register/answer_sheets', views.answer_sheets, name="answer_sheets"),
	path(r'^register/school_certificates', views.school_certificates, name="school_certificates")
]
