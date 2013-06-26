from competition.models import *
from django.contrib import admin
from django.db import connection, transaction


#registers the models with admin
# admin.site.register(SiteUser)



def archive_table(modeladmin, request, queryset):
    
    # Data modifying operation - commit required
    # cursor.execute('CREATE TABLE student'+strftime("%Y-%m-%d %H:%M:%S", gmtime())+' AS SELECT * FROM competition_student')
    # transaction.commit_unless_managed()

    # print "herehre"
    # cursor = connection.cursor()

    # cursor.execute("RENAME TABLE competition_temp TO competition_schoolstudent")
    # cursor.execute ("CREATE TABLE table_name (column_name VARCHAR(100) NOT NULL)")
    cursor = connection.cursor()
    cursor.execute ("INSERT INTO `competition_invigilatorarchive`( `School`, `First_name`, `Surname`, `Grade`, `Venue`, `Inv_Reg`, `Phone (H)`, `Phone (W)`, `Fax (H)`, `Fax (W)`, `Email`, `Responsible`, `Registered_By`) select `School`, `First_name`, `Surname`, `Grade`, `Venue`, `Inv_Reg`, `Phone (H)`, `Phone (W)`, `Fax (H)`, `Fax (W)`, `Email`, `Responsible`, `Registered By` FROM competition_invigilator ")
    cursor.execute()

    print "hello"
    transaction.commit_unless_managed()
    
    row = cursor.fetchone()

    print "hello there"


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
	

class VenueAdmin(admin.ModelAdmin):
	list_display = ('building', 'code', 'seats', 'bums')

class InvigilatorAdmin(admin.ModelAdmin):
	list_display = ('school', 'firstname', 'surname', 'grade', 'venue', 'registered_by')

	
admin.site.add_action(archive_table)

admin.site.register(SchoolUser, SchoolUserAdmin)

admin.site.register(Venue, VenueAdmin)

admin.site.register(School, SchoolAdmin)

admin.site.register(SchoolStudent, SchoolStudentAdmin)
admin.site.register(SchoolStudentArchive)

admin.site.register(Invigilator, InvigilatorAdmin)
admin.site.register(InvigilatorArchive)
