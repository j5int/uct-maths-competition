from competition.models import *
from django.contrib import admin
from django.db import connection, transaction
import time
import datetime


#registers the models with admin
# admin.site.register(SiteUser)



# def archive_invigilator(modeladmin, request, queryset):
#     year = datetime.date.today().strftime("%Y")
#     cursor = connection.cursor()
#     cursor.execute ("INSERT INTO `competition_invigilatorarchive`( `School`, `First_name`, `Surname`, `Grade`, `Venue`, `Inv_Reg`, `Phone (H)`, `Phone (W)`, `Fax (H)`, `Fax (W)`, `Email`, `Responsible`, `Registered By`) select `School`, `First_name`, `Surname`, `Grade`, `Venue`, `Inv_Reg`, `Phone (H)`, `Phone (W)`, `Fax (H)`, `Fax (W)`, `Email`, `Responsible`, `Registered By` FROM competition_invigilator ")
#     cursor.execute("UPDATE `competition_invigilatorarchive` SET `Date_Archived` = %s WHERE `Date_Archived` = NULL"[year])

#     print "hello"
#     transaction.commit_unless_managed()
    
#     row = cursor.fetchone()

#     print "hello there"


class SchoolUserAdmin(admin.ModelAdmin):
	list_display = ('user', 'school', 'email')

class SchoolAdmin(admin.ModelAdmin):
	list_display = ('name', 'registered_by')

	def drop_all():
		#something
		print
	def delete_by_school(table, school ):
		#delete by school?
		print

	def delete_by_user(table, user ):
		#delete registered by user?
		print

class SchoolStudentAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'surname', 'grade', 'school', 'registered_by')

	actions = ['archive_student']

	#Adds all students to the Archived table, and adds the current date
	def archive_student(modeladmin, request, queryset):
	    cursor = connection.cursor()
	    cursor.execute ("INSERT INTO `competition_schoolstudentarchive`(`First_name`, `Surname`, `Language`, `Reference`, `School`, `Score`, `Rank`, `Grade`, `Sex`, `Venue`, `Registered By`) select `First_name`, `Surname`, `Language`, `Reference`, `School`, `Score`, `Rank`, `Grade`, `Sex`,  `Venue`, `Registered By` FROM `competition_schoolstudent`")
	    cursor.execute("UPDATE `competition_schoolstudentarchive` SET `Date Archived` = CURDATE() WHERE `Date Archived` is NULL")
	    transaction.commit_unless_managed()
	

class VenueAdmin(admin.ModelAdmin):
	list_display = ('building', 'code', 'seats', 'bums')

class InvigilatorAdmin(admin.ModelAdmin):
	list_display = ('school', 'firstname', 'surname', 'grade', 'venue', 'registered_by')

	actions = ['archive_invigilator']

	#Adds all invigilators to the Archived table, and adds the current date
	def archive_invigilator(modeladmin, request, queryset):
	    cursor = connection.cursor()
	    cursor.execute ("INSERT INTO `competition_invigilatorarchive`( `School`, `First_name`, `Surname`, `Grade`, `Venue`, `Inv_Reg`, `Phone (H)`, `Phone (W)`, `Fax (H)`, `Fax (W)`, `Email`, `Responsible`, `Registered By`) select `School`, `First_name`, `Surname`, `Grade`, `Venue`, `Inv_Reg`, `Phone (H)`, `Phone (W)`, `Fax (H)`, `Fax (W)`, `Email`, `Responsible`, `Registered By` FROM competition_invigilator ")
	    cursor.execute("UPDATE `competition_invigilatorarchive` SET `Date_Archived` = CURDATE() WHERE `Date_Archived` is NULL")
	    transaction.commit_unless_managed()
	    
	 

	
# admin.site.add_action(archive_invigilator)

admin.site.register(SchoolUser, SchoolUserAdmin)

admin.site.register(Venue, VenueAdmin)

admin.site.register(School, SchoolAdmin)

admin.site.register(SchoolStudent, SchoolStudentAdmin)
admin.site.register(SchoolStudentArchive)

admin.site.register(Invigilator, InvigilatorAdmin)
admin.site.register(InvigilatorArchive)
