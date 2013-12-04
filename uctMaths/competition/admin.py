# admin.py
# registers models for the admin view.
# sets up how each model is displayed (list_display in each <Model>Admin class)
# methods for archiving student and invigilators

from competition.models import *
from django.contrib import admin
from django.db import connection, transaction
import time, datetime

#Displays different fields for SchoolUsers
class SchoolUserAdmin(admin.ModelAdmin):
	list_display = ('user', 'school', 'email')

#Displays different fields for School
class SchoolAdmin(admin.ModelAdmin):
	list_display = ('name', 'registered_by')

#Displays different fields for SchoolStudent and archives SchoolStudent
class SchoolStudentAdmin(admin.ModelAdmin):
	list_display = ('school', 'firstname', 'surname', 'grade', 'registered_by')
	actions = ['archive_student']

	#Adds all students in the SchoolStudent table to the Archived table, and adds the current date
	def archive_student(modeladmin, request, queryset):
	    cursor = connection.cursor()
	    cursor.execute ("INSERT INTO `competition_schoolstudentarchive`(`First_name`, `Surname`, `Language`, `Reference`, `School`, `Score`, `Rank`, `Grade`, `Sex`, `Venue`, `Registered By`) select `First_name`, `Surname`, `Language`, `Reference`, `School`, `Score`, `Rank`, `Grade`, `Sex`,  `Venue`, `Registered By` FROM `competition_schoolstudent`")
	    cursor.execute("UPDATE `competition_schoolstudentarchive` SET `Date Archived` = CURDATE() WHERE `Date Archived` is NULL")
	    transaction.commit_unless_managed()
	
#Displays different fields for Venue
class VenueAdmin(admin.ModelAdmin):
	list_display = ('building', 'code', 'seats', 'bums')

#Displays different fields for Invigilators and archives Invigilators
class InvigilatorAdmin(admin.ModelAdmin):
	#list_display = ('school', 'firstname', 'surname', 'grade', 'venue', 'registered_by')
    list_display = ('school', 'firstname', 'surname', 'venue', 'registered_by')
    actions = ['archive_invigilator']

	#Adds all invigilators in the Invigilarors table, to the Archived table, and adds the current date
    def archive_invigilator(modeladmin, request, queryset):
        cursor = connection.cursor()
	    #cursor.execute ("INSERT INTO `competition_invigilatorarchive`( `School`, `First_name`, `Surname`, `Grade`, `Venue`, `Inv_Reg`, `Phone (H)`, `Phone (W)`, `Fax (H)`, `Fax (W)`, `Email`, `Responsible`, `Registered By`) select `School`, `First_name`, `Surname`, `Grade`, `Venue`, `Inv_Reg`, `Phone (H)`, `Phone (W)`, `Fax (H)`, `Fax (W)`, `Email`, `Responsible`, `Registered By` FROM competition_invigilator ")
        cursor.execute ("INSERT INTO `competition_invigilatorarchive`( `School`, `First_name`, `Surname`, `Venue`, `Inv_Reg`, `Phone (Primary)`, `Phone (Alternative)`, `Registered By`) select `School`, `First_name`, `Surname`, , `Venue`, `Inv_Reg`, `Phone (Primary)`, `Phone (Alternative)`, `Registered By` FROM competition_invigilator ")
	    
        cursor.execute("UPDATE `competition_invigilatorarchive` SET `Date_Archived` = CURDATE() WHERE `Date_Archived` is NULL")
        transaction.commit_unless_managed()

admin.site.register(SchoolUser, SchoolUserAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(SchoolStudent, SchoolStudentAdmin)
admin.site.register(Invigilator, InvigilatorAdmin)
