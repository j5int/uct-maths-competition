# admin.py
# registers models for the admin view.
# sets up how each model is displayed (list_display in each <Model>Admin class)
# methods for archiving student and invigilators

from competition.models import *
from django.contrib import admin
from django.db import connection, transaction
from django import forms
import time, datetime
#Import_export models(https://django-import-export.readthedocs.org/en/latest/getting_started.html)
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#Displays the address field as a text box
class SchoolModelForm( forms.ModelForm ):
	address = forms.CharField( widget=forms.Textarea )
	class Meta:
		model=School

#Displays different fields for SchoolUsers
class SchoolUserAdmin(admin.ModelAdmin):
	list_display = ('user', 'school', 'email')
	search_fields = ['name']

#Displays different fields for School
class SchoolAdmin(admin.ModelAdmin):
	form = SchoolModelForm
	list_display = ('name','phone','email','assigned_to') ##Which columns should be kept here? 
	search_fields = ['name']


class ResponsibleTeacherAdmin(ImportExportModelAdmin):
	list_display = ('firstname', 'surname', 'phone_primary', 'email', 'registered_by')

#Displays different fields for SchoolStudent and archives SchoolStudent
class SchoolStudentAdmin(ImportExportModelAdmin):
	list_display = ('school', 'firstname', 'surname', 'grade', 'reference', 'paired')
	actions = ['archive_student']
	search_fields = ['firstname', 'surname', 'reference', 'venue']

	#Adds all students in the SchoolStudent table to the Archived table, and adds the current date
	def archive_student(modeladmin, request, queryset):
	    cursor = connection.cursor()
	    cursor.execute ("INSERT INTO `competition_schoolstudentarchive`(`First_name`, `Surname`, `Language`, `Reference`, `School`, `Score`, `Rank`, `Grade`, `Venue`, `Registered By`) select `First_name`, `Surname`, `Language`, `Reference`, `School`, `Score`, `Rank`, `Grade`,  `Venue`, `Registered By`, `Paired` FROM `competition_schoolstudent`")
	    cursor.execute("UPDATE `competition_schoolstudentarchive` SET `Date Archived` = CURDATE() WHERE `Date Archived` is NULL")
	    transaction.commit_unless_managed()

    # -------------- Import_Export functionality  ----------
	resource_class = SchoolStudentResource
	list_filter=('school', 'grade', 'paired', 'venue', 'language') #Field filters (shown as bar on right)

#Displays different fields for Venue
class VenueAdmin(admin.ModelAdmin):
	list_display = ('building', 'code', 'seats', 'bums')
	#search_fields = ['building', 'code', 'seats']


#Displays different fields for Invigilators and archives Invigilators
class InvigilatorAdmin(ImportExportModelAdmin):
    #list_display = ('school', 'firstname', 'surname', 'grade', 'venue', 'registered_by')
    list_display = ('school', 'firstname', 'surname', 'venue', 'registered_by')
    actions = ['archive_invigilator']
    search_fields = ['firstname', 'surname']

    # -------------- Import_Export functionality  ----------
    resource_class = InvigilatorResource
    list_filter=('school', 'venue') #Field filters (shown as bar on right)

    #Adds all invigilators in the Invigilarors table, to the Archived table, and adds the current date
    def archive_invigilator(modeladmin, request, queryset):
        cursor = connection.cursor()
        
        cursor.execute ("INSERT INTO `competition_invigilatorarchive`( `School`, `First_name`, `Surname`, `Venue`, `Inv_Reg`, `Phone (Primary)`, `Phone (Alternative)`,  'Email', `Registered By`) select `School`, `First_name`, `Surname`, , `Venue`, `Inv_Reg`, `Phone (Primary)`, `Phone (Alternative)`, 'Email', `Registered By` FROM competition_invigilator ")

        cursor.execute("UPDATE `competition_invigilatorarchive` SET `Date_Archived` = CURDATE() WHERE `Date_Archived` is NULL")
        transaction.commit_unless_managed()



admin.site.register(SchoolUser, SchoolUserAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(ResponsibleTeacher, ResponsibleTeacherAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(SchoolStudent, SchoolStudentAdmin)
admin.site.register(Invigilator, InvigilatorAdmin)
