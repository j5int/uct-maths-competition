# admin.py
# registers models for the admin view.
# sets up how each model is displayed (list_display in each <Model>Admin class)
# methods for archiving student and invigilators
from __future__ import unicode_literals
from competition.models import *
from django.contrib import admin
from django.contrib.admin import SimpleListFilter

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
		fields = "__all__"

#Displays different fields for SchoolUsers
#class SchoolUserAdmin(admin.ModelAdmin):
#	list_display = ('user', 'school', 'email')
#	search_fields = ['name']

#Displays different fields for School
class SchoolAdmin(ImportExportModelAdmin):
	form = SchoolModelForm
	list_display = ('key', 'name', 'language', 'address','phone','fax','contact','email','assigned_to', 'score', 'rank', 'entered', 'location', 'answer_sheets_emailed') ##Which columns should be kept here?
	search_fields = ['name']
	resource_class = SchoolResource

	actions = ['remove_user_associations', 'output_schooltaglist', 'assign_school_ranks', 'school_summary','print_school_confirmations', 'update_school_entry_status','generate_school_reports','generate_multi_school_reports','email_school_reports','school_certificate_list','generate_school_answer_sheets','email_school_answer_sheets']

    #import school dataset
	#Expects csv (comma-separated) file with the first line being:
    #id,name,key,language,address,phone,fax,contact,entered,score,email,assigned_to(leave blank),registered_by
    #Entries are on separate rows (separated by line break)
	dataset = tablib.Dataset()
	dataset.headers = ['id', 'name', 'key', 'language', 'address','phone','fax','contact','email','assigned_to', 'score', 'rank', 'location']

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

	def update_school_entry_status(self, request, queryset):
	    return compadmin.update_school_entry_status()

	def generate_school_reports(self, request, queryset):
	    return compadmin.print_school_reports(request, queryset)

	def email_school_reports(self, request, queryset):
	    return compadmin.email_school_reports(request, queryset)

	def generate_multi_school_reports(self, request, queryset):
	    return compadmin.multi_reportgen(request, queryset)

	def school_certificate_list(self, request, queryset):
	    return compadmin.certificate_list(request, queryset)
	
	def generate_school_answer_sheets(self, request, queryset):
		return compadmin.generate_school_answer_sheets(request, queryset)
	
	def email_school_answer_sheets(self, request, queryset):
		return compadmin.email_school_answer_sheets(request, queryset)

	output_schooltaglist.short_description = 'Download school tags for selected school(s)'
	remove_user_associations.short_description = 'Remove associated users to selected school(s)'
	assign_school_ranks.short_description = 'Assign rank based on score to schools (regardless of selection)'
	school_summary.short_description = 'Schools summary (.xls) (only schools with entries, regardless of selection)'
	update_school_entry_status.short_description = 'Update/Refresh schools\' entry status (regardless of selection)'
	print_school_confirmations.short_description = 'Print selected school(s) confirmation (single .pdf)'
	generate_school_reports.short_description = 'Print selected school(s) reports (single .pdf)'
	generate_multi_school_reports.short_description = 'Download selected school(s) (separate) reports (.zip/.pdf)'
	school_certificate_list.short_description = 'Download school certificate list'

	email_school_reports.short_description = 'Email selected school(s) reports (single .pdf) to school(s)'

	generate_school_answer_sheets.short_description = 'Download answer sheets for selected school(s)'

	class AnswerSheetEmailSentFilter(SimpleListFilter):
		title = "Answer sheets emailed"
		parameter_name = "answer_sheets_emailed"
		
		def lookups(self, request, model_admin):
			return (
				('sent', 'sent'),
				('unsent', 'entered and unsent'),
			)
		def queryset(self, request, queryset):
			if self.value() == 'sent':
				return queryset.filter(models.Q(answer_sheets_emailed__gte=datetime.datetime(datetime.date.today().year, 1, 1, 0, 0, 0))
					& models.Q(entered__gt=0) )
			if self.value() == 'unsent':
				print(datetime.date.today().year)
				return queryset.filter((models.Q(answer_sheets_emailed__isnull=True)
					| models.Q(answer_sheets_emailed__lt=datetime.datetime(datetime.date.today().year, 1, 1, 0, 0, 0)) )
					& models.Q(entered__gt=0) )

	list_filter=('entered','language',AnswerSheetEmailSentFilter) #Field filters (shown as bar on right)




class ResponsibleTeacherAdmin(ImportExportModelAdmin):
	list_display = ('school', 'firstname', 'surname', 'phone_primary', 'phone_alt', 'email', 'report_downloaded', 'answer_sheet_downloaded')

#Displays different fields for SchoolStudent and archives SchoolStudent
class SchoolStudentAdmin(ImportExportModelAdmin):
	list_display = ('school', 'firstname', 'surname', 'grade', 'reference', 'venue', 'paired', 'score', 'rank', 'award', 'location')
	actions = ['write_studentlist','write_studenttags', 'upload_results', 'output_assign_awards', 'output_PRN_files','rank_students', 'assign_student_awards']
	search_fields = ['firstname', 'surname', 'reference', 'venue']

	#Adds all students in the SchoolStudent table to the Archived table, and adds the current date
	def archive_student(modeladmin, request, queryset):
	    cursor = connection.cursor()
	    cursor.execute ("INSERT INTO `competition_schoolstudentarchive`("
						"`First_name`, `Surname`, `Language`, `Reference`, `School`, `Score`, `Rank`, `Grade`, `Venue`, `Paired`, 'Location') "
						"select "
						"`First_name`, `Surname`, `Language`, `Reference`, `School`, `Score`, `Rank`, `Grade`,  `Venue`, `Paired`, 'Location' "
						"FROM `competition_schoolstudent`")
	    cursor.execute("UPDATE `competition_schoolstudentarchive` SET `Date Archived` = CURDATE() WHERE `Date Archived` is NULL")
	    transaction.commit_unless_managed()

    # -------------- Import_Export functionality  ----------
	resource_class = SchoolStudentResource
	list_filter=('grade', 'paired', 'venue', 'language','school', 'award') #Field filters (shown as bar on right)

	dataset = tablib.Dataset()
	dataset.headers = ['school', 'firstname', 'surname', 'grade', 'reference', 'paired']

	def write_studentlist(self, request, queryset):
	    return compadmin.output_studentlists(queryset)
	write_studentlist.short_description = 'Export (.xls) student registry for selected student(s)'

	def write_studenttags(self, request, queryset):
	    return compadmin.output_studenttags(queryset)
	write_studenttags.short_description = 'Generate MailMerge student tags for selected student(s)'

	def upload_results(self, request, queryset):
	    return compadmin.upload_results(request, queryset)
	upload_results.short_description = 'Upload students\' results (.RES file required)'

	def rank_students(self, request, queryset):
	    return compadmin.rank_students(queryset)
	rank_students.short_description = 'Re-rank students. (regardless of selection)'

	def output_assign_awards(self, request, queryset):
	    return compadmin.export_awards(request, queryset)
	output_assign_awards.short_description = 'Export (.xls) document (regardless of selection)'

	def output_PRN_files(self, request, queryset):
	    return compadmin.output_PRN_files(queryset)
	output_PRN_files.short_description = 'Generate PRN files for all students (regardless of selection)'

	def assign_student_awards(self, request, queryset):
	    return compadmin.assign_student_awards()
	assign_student_awards.short_description = 'Assign student awards (regardless of selection)'

#Displays different fields for Venue
class VenueAdmin(ImportExportModelAdmin):
	resource_class = VenueResource
	list_display = ('building', 'code', 'seats', 'grade', 'allocated_to_pairs', 'occupied_seats', 'location')
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
    list_display = ('school', 'firstname', 'surname', 'phone_primary', 'phone_alt', 'email', 'venue', 'rt_name','rt_phone_primary','rt_email', 'location')
    #actions = ['archive_invigilator']
    search_fields = ['firstname', 'surname']

    # -------------- Import_Export functionality  ----------
    resource_class = InvigilatorResource
    list_filter=('school', 'venue') #Field filters (shown as bar on right)

    #Adds all invigilators in the Invigilators table, to the Archived table, and adds the current date
    def archive_invigilator(modeladmin, request, queryset):
        cursor = connection.cursor()
        
        cursor.execute ("INSERT INTO `competition_invigilatorarchive`( "
						"`School`, `First_name`, `Surname`, `Venue`, `Inv_Reg`, `Phone (Primary)`, `Phone (Alternative)`, 'Email', `Registered By`, `Notes`, 'Location') "
						"select "
						"`School`, `First_name`, `Surname`, `Venue`, `Inv_Reg`, `Phone (Primary)`, `Phone (Alternative)`, 'Email', `Registered By`, `Notes`, 'Location' "
						"FROM competition_invigilator ")

        cursor.execute("UPDATE `competition_invigilatorarchive` SET `Date_Archived` = CURDATE() WHERE `Date_Archived` is NULL")
        transaction.commit_unless_managed()

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('newentries_Opendate', 'newentries_Closedate', 'admin_emailaddress', 'prizegiving_date')
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
