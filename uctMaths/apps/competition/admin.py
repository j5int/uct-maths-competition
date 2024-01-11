# admin.py
# registers models for the admin view.
# sets up how each model is displayed (list_display in each <Model>Admin class)
# methods for archiving student and invigilators
from __future__ import unicode_literals

from django.urls import path

from .models import *
from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from django.http import HttpResponseRedirect
from django.db import connection, transaction
from django import forms
import datetime

#Import_export models(https://django-import-export.readthedocs.org/en/latest/getting_started.html)
from import_export.admin import ImportExportModelAdmin
import tablib
from . import compadmin
from .resources import SchoolResource, SchoolStudentResource, VenueResource, InvigilatorResource


#Displays the address field as a text box
class SchoolModelForm( forms.ModelForm ):
    address = forms.CharField( widget=forms.Textarea )
    class Meta:
        model=School
        fields = "__all__"

#Displays different fields for SchoolUsers
#class SchoolUserAdmin(admin.ModelAdmin):
#    list_display = ('user', 'school', 'email')
#    search_fields = ['name']

#Displays different fields for School
class SchoolAdmin(ImportExportModelAdmin):
    change_form_template = "admin/rt_changeform.html"
    form = SchoolModelForm
    list_display = ('key', 'name', 'language', 'address','phone','fax','contact','email','assigned_to', 'score', 'rank', 'entered', 'location', 'answer_sheets_emailed', 'report_emailed') ##Which columns should be kept here?
    search_fields = ['name']
    resource_class = SchoolResource

    # Single action button functions (don't require selection)
    change_list_template = "admin/school_changelist.html"
    def get_urls(self):
        urls = super(SchoolAdmin, self).get_urls()
        my_urls = [
            path("assign_school_ranks/", self.assign_school_ranks),
            path("school_summary/", self.school_summary),
            path("update_school_entry_status/", self.update_school_entry_status),
            path("school_certificate_list/", self.school_certificate_list),
            path("generate_grade_answer_sheets/", self.generate_grade_answer_sheets)
        ]
        return my_urls + urls

    def assign_school_ranks(self, request):
        compadmin.rank_schools()
        return HttpResponseRedirect("../")
        
    def school_summary(self, request):
        return compadmin.school_summary(request)

    def update_school_entry_status(self, request):
        compadmin.update_school_entry_status()
        return HttpResponseRedirect("../")

    def school_certificate_list(self, request):
        return compadmin.certificate_list(request)
    
    def generate_grade_answer_sheets(self, request):
        return compadmin.generate_grade_answer_sheets(request)

    # Action items (require selections)
    actions = [    
                'remove_user_associations', 'output_schooltaglist','print_school_confirmations','generate_school_reports',
                'generate_multi_school_reports','email_school_reports','generate_school_answer_sheets',
                'email_school_answer_sheets','export_courier_address'
            ]

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

    def print_school_confirmations(self, request, queryset):
        return compadmin.print_school_confirmations(request, queryset)

    def generate_school_reports(self, request, queryset):
        return compadmin.print_school_reports(request, queryset)

    def email_school_reports(self, request, queryset):
        return compadmin.email_school_reports(request, queryset)

    def generate_multi_school_reports(self, request, queryset):
        return compadmin.multi_reportgen(request, queryset)
    
    def generate_school_answer_sheets(self, request, queryset):
        return compadmin.generate_school_answer_sheets(request, queryset)
    
    def email_school_answer_sheets(self, request, queryset):
        return compadmin.email_school_answer_sheets(request, queryset)

    def export_courier_address(self, request, queryset):
        return compadmin.export_courier_address(request, queryset)

    output_schooltaglist.short_description = 'Download school tags for selected school(s)'
    remove_user_associations.short_description = 'Remove associated users to selected school(s)'
    print_school_confirmations.short_description = 'Print selected school(s) confirmation (single .pdf)'
    generate_school_reports.short_description = 'Print selected school(s) reports (single .pdf)'
    generate_multi_school_reports.short_description = 'Download selected school(s) (separate) reports (.zip/.pdf)'
    email_school_reports.short_description = 'Email selected school(s) reports (single .pdf) to school(s)'
    email_school_answer_sheets.short_description = "Email selected school(s) answer sheets"
    generate_school_answer_sheets.short_description = 'Download answer sheets for selected school(s)'
    export_courier_address.short_description = 'Export courier addresses (.xls) for selected school(s)'
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
                return queryset.filter((models.Q(answer_sheets_emailed__isnull=True)
                    | models.Q(answer_sheets_emailed__lt=datetime.datetime(datetime.date.today().year, 1, 1, 0, 0, 0)) )
                    & models.Q(entered__gt=0) )
    class ReportEmailSentFilter(SimpleListFilter):
        title = "Report emailed"
        parameter_name = "report_emailed"
        
        def lookups(self, request, model_admin):
            return (
                ('sent', 'sent'),
                ('unsent', 'entered and unsent'),
            )
        def queryset(self, request, queryset):
            if self.value() == 'sent':
                return queryset.filter(models.Q(report_emailed__gte=datetime.datetime(datetime.date.today().year, 1, 1, 0, 0, 0))
                    & models.Q(entered__gt=0) )
            if self.value() == 'unsent':
                return queryset.filter((models.Q(report_emailed__isnull=True)
                    | models.Q(report_emailed__lt=datetime.datetime(datetime.date.today().year, 1, 1, 0, 0, 0)) )
                    & models.Q(entered__gt=0) )
    
    class EnteredFilter(SimpleListFilter):
        title = "school entered"
        parameter_name = "entered"

        def lookups(self, request, model_admin):
            return (
                ("entered", "entered"),
                ("not-entered", "not entered")
            )
        
        def queryset(self, request, queryset):
            if self.value() == "entered":
                return queryset.filter(models.Q(entered__gte=1))
            if self.value() == "not-entered":
                return queryset.filter(models.Q(entered__lte=0))

    list_filter=(EnteredFilter,'language',AnswerSheetEmailSentFilter,ReportEmailSentFilter) #Field filters (shown as bar on right)






class ResponsibleTeacherAdmin(ImportExportModelAdmin):
    change_form_template = "admin/rt_changeform.html"
    list_display = ('school', 'firstname', 'surname', 'phone_primary', 'phone_alt', 'phone_cell', 'email_school', 'email_personal', 'report_downloaded', 'answer_sheet_downloaded')
    search_fields = ['school__name', 'firstname']
#Displays different fields for SchoolStudent and archives SchoolStudent
class SchoolStudentAdmin(ImportExportModelAdmin):
    list_display = ('school', 'firstname', 'surname', 'grade', 'reference', 'venue', 'paired', 'score', 'rank', 'award', 'location')
    actions = ['write_studentlist','write_studenttags']
    search_fields = ['firstname', 'surname', 'reference', 'venue']
    # Single action button functions (don't require selection)
    change_list_template = "admin/student_changelist.html"
    def get_urls(self):
        urls = super(SchoolStudentAdmin, self).get_urls()
        my_urls = [
            path("upload_results/", self.upload_results),
            path("rank_students/", self.rank_students),
            path("output_assign_awards/", self.output_assign_awards),
            path("output_PRN_files/", self.output_PRN_files),
            path("assign_student_awards/", self.assign_student_awards),
        ]
        return my_urls + urls
    def upload_results(self, request):
        return compadmin.upload_results()

    def rank_students(self, request):
        compadmin.rank_students()
        return HttpResponseRedirect("../")

    def output_assign_awards(self, request):
        return compadmin.export_awards(request)

    def output_PRN_files(self, request):
        return compadmin.output_PRN_files()
        
    def assign_student_awards(self, request):
        compadmin.assign_student_awards()
        return HttpResponseRedirect("../")
    #Adds all students in the SchoolStudent table to the Archived table, and adds the current date
    def archive_student(modeladmin, request, queryset):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO `competition_schoolstudentarchive`("
                       "`First_name`, `Surname`, `Language`, `Reference`, `School`, `Score`, `Rank`, `Grade`, `Venue`, `Paired`, 'Location') "
                       "select "
                       "`First_name`, `Surname`, `Language`, `Reference`, `School`, `Score`, `Rank`, `Grade`,  `Venue`, `Paired`, 'Location' "
                       "FROM `competition_schoolstudent`")
        cursor.execute(
            "UPDATE `competition_schoolstudentarchive` SET `Date Archived` = CURDATE() WHERE `Date Archived` is NULL")
        transaction.commit_unless_managed() #TODO: replace deprecated

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

    def response_change(self, request, obj):
        """
        This overides method in parent class that is in the Django files.
        Deallocates students from the venue before figuring out where to redirect after the 'Save' button has been pressed
        when editing an existing object.
        """
        queryset = [obj]
        self.deallocate(request, queryset)
        test = super()
        return test.response_change(request, obj) 

    auto_allocate.short_description = 'Auto-allocate unallocated students to selected venue(s)' 
    deallocate.short_description = 'Deallocate students from selected venue(s)'
    write_venue_register.short_description = 'Export XLS student registry for selected venue(s)'


# Displays different fields for Invigilators and archives Invigilators
class InvigilatorAdmin(ImportExportModelAdmin):
    # list_display = ('school', 'firstname', 'surname', 'grade', 'venue', 'registered_by')
    list_display = (
    'school', 'firstname', 'surname', 'phone_primary', 'phone_alt', 'email', 'venue', 'rt_name', 'rt_phone_primary',
    'rt_email', 'location')
    # actions = ['archive_invigilator']
    search_fields = ['firstname', 'surname']

    # -------------- Import_Export functionality  ----------
    resource_class = InvigilatorResource
    list_filter = ('school', 'venue')  # Field filters (shown as bar on right)

    # Adds all invigilators in the Invigilators table, to the Archived table, and adds the current date
    def archive_invigilator(modeladmin, request, queryset):
        cursor = connection.cursor()

        cursor.execute("INSERT INTO `competition_invigilatorarchive`( "
                       "`School`, `First_name`, `Surname`, `Venue`, `Inv_Reg`, `Phone (Primary)`, `Phone (Alternative)`, 'Email', `Registered By`, `Notes`, 'Location') "
                       "select "
                       "`School`, `First_name`, `Surname`, `Venue`, `Inv_Reg`, `Phone (Primary)`, `Phone (Alternative)`, 'Email', `Registered By`, `Notes`, 'Location' "
                       "FROM competition_invigilator ")

        cursor.execute(
            "UPDATE `competition_invigilatorarchive` SET `Date_Archived` = CURDATE() WHERE `Date_Archived` is NULL")
        transaction.commit_unless_managed() #TODO: replace deprecated

class CompetitionAdmin(admin.ModelAdmin):
    
    list_display = ('newentries_Opendate', 'newentries_Closedate', 'admin_emailaddress', 'prizegiving_date', 'invigilators', 'answer_sheet_download_enabled')
    actions = ['export_competition']
    # Single action button functions (don't require selection)
    change_list_template = "admin/competition_changelist.html"
    def get_urls(self):
        urls = super(CompetitionAdmin, self).get_urls()
        my_urls = [
            path("upload_declaration/", self.upload_declaration),
        ]
        return my_urls + urls

    def upload_declaration(self, request):
        return compadmin.upload_declaration()

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
