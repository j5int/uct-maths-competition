from competition.models import *
from django.contrib import admin

#registers the models with admin
# admin.site.register(SiteUser)

class archive_table(admin.ModelAdmin):
	#archive table. 
	#copy to new table with date in the name. 
	#drop original table to be recreated with syncdb.
	db.rename_table("venues", "hello")

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
admin.site.register(School, SchoolAdmin)
admin.site.register(SchoolStudent, SchoolStudentAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Invigilator, InvigilatorAdmin)