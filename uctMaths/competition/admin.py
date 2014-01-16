# admin.py
# registers models for the admin view.
# sets up how each model is displayed (list_display in each <Model>Admin class)
# methods for archiving student and invigilators
from __future__ import unicode_literals
from competition.models import *
from django.contrib import admin
from django.db import connection, transaction
from django import forms
import time, datetime
#Import_export models(https://django-import-export.readthedocs.org/en/latest/getting_started.html)
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import tablib
import compadmin

#Displays the address field as a text box
class SchoolModelForm( forms.ModelForm ):
	address = forms.CharField( widget=forms.Textarea )
	class Meta:
		model=School

#Displays different fields for SchoolUsers
#class SchoolUserAdmin(admin.ModelAdmin):
#	list_display = ('user', 'school', 'email')
#	search_fields = ['name']

#Displays different fields for School
class SchoolAdmin(ImportExportModelAdmin):
	form = SchoolModelForm
	list_display = ('key', 'name', 'language', 'address','phone','fax','contact','email','assigned_to', 'score', 'rank') ##Which columns should be kept here? 
	search_fields = ['name']
	resource_class = SchoolResource
	actions = ['remove_user_associations', 'output_schooltaglist', 'assign_school_ranks', 'school_summary','print_school_confirmations']
    #import school dataset
	#Expects csv (comma-separated) file with the first line being:
    #id,name,key,language,address,phone,fax,contact,entered,score,email,assigned_to(leave blank),registered_by
    #Entries are on separate rows (separated by line break)
	dataset = tablib.Dataset()
	dataset.headers = ['id', 'name', 'key', 'language', 'address','phone','fax','contact','email','assigned_to', 'score', 'rank']

	def remove_user_associations(self, request, queryset):
	    return compadmin.remove_user_assoc(queryset)

	def output_schooltaglist(self, request, queryset):
	    return compadmin.output_schooltaglists(queryset)

	def assign_school_ranks(self, request, queryset):
	    return compadmin.rank_schools(queryset)
	    
	def school_summary(self, request, queryset):
	    return compadmin.school_summary(request)
	    
	def print_school_confirmations(self, request, queryset):
	    return compadmin.print_school_confirmations(request, queryset)


	output_schooltaglist.short_description = 'Download school tags for schools (regardless of selection)'
	remove_user_associations.short_description = 'Remove associated users to selected school(s)' 
	assign_school_ranks.short_description = 'Assign rank based on score to schools (regardless of selection)' 
	school_summary.short_description = 'Schools with entries (xls summary) (regardless of selection)' 




class ResponsibleTeacherAdmin(ImportExportModelAdmin):
	list_display = ('school', 'firstname', 'surname', 'phone_primary', 'phone_alt', 'email')

#Displays different fields for SchoolStudent and archives SchoolStudent
class SchoolStudentAdmin(ImportExportModelAdmin):
	list_display = ('school', 'firstname', 'surname', 'grade', 'reference', 'venue', 'paired', 'score', 'rank')
	actions = ['archive_student','write_studentlist','write_studenttags', 'upload_results', 'output_assign_awards', 'output_PRN_files']
	search_fields = ['firstname', 'surname', 'reference', 'venue']

	#Adds all students in the SchoolStudent table to the Archived table, and adds the current date
	def archive_student(modeladmin, request, queryset):
	    cursor = connection.cursor()
	    cursor.execute ("INSERT INTO `competition_schoolstudentarchive`(`First_name`, `Surname`, `Language`, `Reference`, `School`, `Score`, `Rank`, `Grade`, `Venue`, `Registered By`) select `First_name`, `Surname`, `Language`, `Reference`, `School`, `Score`, `Rank`, `Grade`,  `Venue`, `Paired` FROM `competition_schoolstudent`")
	    cursor.execute("UPDATE `competition_schoolstudentarchive` SET `Date Archived` = CURDATE() WHERE `Date Archived` is NULL")
	    transaction.commit_unless_managed()

    # -------------- Import_Export functionality  ----------
	resource_class = SchoolStudentResource
	list_filter=('grade', 'paired', 'venue', 'language','school') #Field filters (shown as bar on right)

	dataset = tablib.Dataset()
	dataset.headers = ['school', 'firstname', 'surname', 'grade', 'reference', 'paired']

	def write_studentlist(self, request, queryset):
	    return compadmin.output_studentlists(queryset)
	write_studentlist.short_description = 'Export formatted XLS student registry for selected students'

	def write_studenttags(self, request, queryset):
	    return compadmin.output_studenttags(queryset)
	write_studenttags.short_description = 'Generate MailMerge student tags for all students (regardless of selection)'

	def upload_results(self, request, queryset):
	    return compadmin.upload_results(request, queryset)
	upload_results.short_description = 'Upload students\' results (.RES file required)'

	def rank_students(self, request, queryset):
	    return compadmin.rank_students(queryset)
	rank_students.short_description = 'Re-rank students. (regardless of selection)'

	def output_assign_awards(self, request, queryset):
	    return compadmin.assign_awards(request, queryset)
	output_assign_awards.short_description = 'Assign awards and export (xls) document (regardless of selection)'

	def output_PRN_files(self, request, queryset):
	    return compadmin.output_PRN_files(queryset)
	output_PRN_files.short_description = 'Generate PRN files for all students (regardless of selection)'


#Displays different fields for Venue
class VenueAdmin(ImportExportModelAdmin):
	resource_class = VenueResource
	list_display = ('building', 'code', 'seats', 'grade', 'allocated_to_pairs', 'occupied_seats')
	search_fields = ['building', 'code']
	list_filter = ('grade', 'allocated_to_pairs')
	actions = ['auto_allocate', 'deallocate', 'write_venue_register']
    # -------------- Import_Export functionality  ----------
	resource_class = VenueResource
	#Expects csv (comma-separated) file with the first line being:
    #id,name,key,language,address,phone,fax,contact,entered,score,email,assigned_to(leave blank),registered_by
    #Entries are on separate rows (separated by line break)
	dataset = tablib.Dataset()
	dataset.headers = ['building', 'code', 'seats','grade', 'allocated_to_pairs', 'occupied_seats']

	def auto_allocate(self, request, queryset):
	    compadmin.auto_allocate(queryset)

	def deallocate(self, request, queryset):
	    compadmin.venue_deallocate(queryset)

	def write_venue_register(self, request, queryset):
	    return compadmin.output_register(queryset)

	auto_allocate.short_description = 'Auto-allocate unallocated students to selected venue(s)' 
	deallocate.short_description = 'Deallocate students from selected venue(s)'
	write_venue_register.short_description = 'Export XLS student registry for selected venue(s)'

#Displays different fields for Invigilators and archives Invigilators
class InvigilatorAdmin(ImportExportModelAdmin):
    #list_display = ('school', 'firstname', 'surname', 'grade', 'venue', 'registered_by')
    list_display = ('school', 'firstname', 'surname', 'phone_primary', 'phone_alt', 'email', 'venue', 'rt_name','rt_phone_primary','rt_email')
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

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('newentries_Opendate', 'newentries_Closedate', 'admin_emailaddress')
    actions = ['export_competition']
    
    def export_competition(self, request, queryset):
        return compadmin.export_competition(request)

    export_competition.short_description = 'Export competition database (regardless of selection)'

#admin.site.register(SchoolUser, SchoolUserAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(ResponsibleTeacher, ResponsibleTeacherAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(SchoolStudent, SchoolStudentAdmin)
admin.site.register(Invigilator, InvigilatorAdmin)
