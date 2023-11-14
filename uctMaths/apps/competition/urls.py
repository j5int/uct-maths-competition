from django.urls import path

from apps.competition import compadmin_views, views

urlpatterns = [
	#registration views
    path('register/school_select/', views.school_select, name='school_select'),
	path('register/students/', views.newstudents, name='newstudents'),
	path('register/submitted/', views.submitted, name='submitted'),
	path('register/entry_review/', views.entry_review, name='entry_review'),
	path('register/printer_entry/', views.printer_entry, name='printer_entry'),
	path('register/school_report/', views.printer_entry, name='school_report'),
	path('accounts/profile/', views.profile),
	path('admin/upload_results/', compadmin_views.upload_results, name='upload_results'),
	path('admin/upload_declaration/', compadmin_views.upload_declaration, name='upload_declaration'),
	path('register/school_results/', views.school_results, name='school_results'),
	path('register/answer_sheets/', views.answer_sheets, name="answer_sheets"),
	path('register/school_certificates/', views.school_certificates, name="school_certificates")
]
