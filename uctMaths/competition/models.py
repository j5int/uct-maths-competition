# models.py
# defines django models (correspond to db tables)

from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
#Import_export models(https://django-import-export.readthedocs.org/en/latest/getting_started.html)
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
import tablib

class School(models.Model):
    # Contains school information. Duplicates should not be allowed, but will be removed by the admin.
    name        = models.CharField(max_length=255L, db_column='Name')
    key         = models.CharField(max_length=3L, db_column='Key') 
    language    = models.CharField(max_length=1L, choices=( 
    ('e', 'English'), 
    ('a', 'Afrikaans'), 
    ('b', 'Bilingual')
    ), db_column = 'Language')
    address     = models.CharField(max_length=255L, db_column='Address', blank=True)
    phone       = models.CharField(max_length=15L, db_column='Phone', blank=True) 
    fax         = models.CharField(max_length=15L, db_column='Fax', blank=True) 
    contact     = models.CharField(max_length=255L, db_column='Contact', blank=True)
    entered     = models.IntegerField(null=True, db_column='Entered', blank=True) 
    score       = models.IntegerField(null=True, db_column='Score', blank=True) 
    email       = models.CharField(max_length=50L, db_column='Email', blank=True) 
    assigned_to = models.ForeignKey(User, default=None, null=True, db_column='Assigned to', blank=True) #ForreignKey (gets assigned a single user)
    #registered_by = models.CharField(max_length=255L, db_column='Registered By') #Changed to CharField

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']     #defines the way the records are sorted.

class SchoolStudent(models.Model):
    # A single student. Not a User. Score and Rank will added/updated by the admin so they can be null.
    firstname   = models.CharField(max_length=255L, db_column='First_name')
    surname     = models.CharField(max_length=255L, db_column='Surname')
    language    = models.CharField(max_length=1L, choices=(
        ('e', 'English'), 
        ('a', 'Afrikaans'),
		('b', 'Bilingual')
    ), db_column = 'Language')
    reference   = models.CharField(max_length=7L, db_column='Reference') 
    school      = models.ForeignKey('School', db_column='School') 
    score       = models.IntegerField(null=True, db_column='Score', blank=True) 
    rank        = models.IntegerField(null=True, db_column='Rank', blank=True) 
    grade       = models.IntegerField(db_column='Grade', 
        validators = [
            MaxValueValidator(12),
            MinValueValidator(0)
        ])    
 #   sex         = models.CharField(max_length=1L, db_column='Sex', blank=True) 
    venue       = models.CharField(max_length=40L, db_column='Venue', blank=True) 
    #registered_by = models.ForeignKey(User, db_column='Registered By')
    paired = models.BooleanField(db_column='Paired')

    def __str__(self):
        return 'pair '+str(self.reference) if self.surname == '' else self.surname+', '+self.firstname
    class Meta:
        ordering = ['school', 'grade', 'surname', 'firstname','reference'] #defines the way the records are sorted.

#class SchoolUser(models.Model):
#    # The administrator for a single school. 
#    # A User can register/update/remove SchoolStudents and Invigilators.

#    school      = models.ForeignKey('School', db_column='School') 
#    count       = models.IntegerField()
#    address     = models.CharField(max_length=255L, db_column='Address')
#    town        = models.CharField(max_length=50L, db_column='Town')
#    postal_code = models.CharField(max_length=4L, db_column='Postal_Code') 
#    phone       = models.CharField(max_length=15L, db_column='Telephone') 
#    fax         = models.CharField(max_length=15L, db_column='Fax', blank=True) 
#    email       = models.CharField(max_length=50L, db_column='Email', blank=True)
#    correction  = models.IntegerField(db_column='Correction') 
#    entered     = models.IntegerField(db_column='Entered')  
#    language    = models.CharField(max_length=1L, db_column='Language', choices=(
#        ('e', 'English'), 
#        ('a', 'Afrikaans'),
#		('b', 'Bilingual')
#    )) 
#    counter     = models.IntegerField(db_column='Count')
#    last_login  = models.DateField(null=True, blank=True, db_column='Last Login')
#    non_uct     = models.IntegerField(db_column='Non UCT') 
#    user        = models.OneToOneField(User)

#    def __str__(self):
#        return self.user
#    class Meta:
#        ordering = ['school', 'user'] #defines the way the records are sorted.

class Venue(models.Model):
    '''Venues are locations for the event. Many SchoolStudents to one Venue.'''
    code        = models.CharField(max_length=40L, db_column='Code')
    building    = models.CharField(max_length=40L, db_column='Building') 
    seats       = models.IntegerField(db_column='Seats')
    grade       = models.IntegerField(db_column='Grade',null=True, blank=True)
    allocated_to_pairs = models.BooleanField(db_column='Allocated to PAIRS')
    occupied_seats = models.IntegerField(db_column='Occupied seats', blank=True)
    #individuals = models.IntegerField(db_column='Individuals')
    #registered_by = models.ForeignKey(User, db_column='Registered By')

    def __str__(self):
        return self.building+', '+self.code
    class Meta:
        ordering = ['building', 'code'] #defines the way the records are sorted.

class Invigilator(models.Model):
    # Invigilators registered by SchoolUsers. Many Invigilator to one School. 
    # Many Invigilators to one Venue.

    school      = models.ForeignKey('School', db_column='School') 
    firstname   = models.CharField(max_length=255L, db_column='First_name')
    surname     = models.CharField(max_length=255L, db_column='Surname')
    venue       = models.ForeignKey('Venue', db_column='Venue', null=True, blank=True) #Admin feature, implement later
    phone_primary = models.CharField(max_length=15L, db_column='Phone (Primary)', blank=True)
    phone_alt = models.CharField(max_length=15L, db_column='Phone (Alternative)', blank=True)
    email       = models.CharField(max_length=50L, db_column='Email', blank=False)


#REQUIREMENT: admin requests responsible teacher details when querying invigilators. 
#             The following methods cater for this. Performing the lookup based on assigned school.
    def rt_name(self):
        responsible_teacher = ResponsibleTeacher.objects.filter(school = self.school)
        if responsible_teacher:        
            return responsible_teacher[0].firstname + ' ' + responsible_teacher[0].surname
        else:
            return 'Not specified' #This should not happen!

    def rt_phone_primary(self):
        responsible_teacher = ResponsibleTeacher.objects.filter(school = self.school)
        if responsible_teacher:
            return responsible_teacher[0].phone_primary
        else:
            return 'Not specified' #This should not happen!

    def rt_email(self):
        responsible_teacher = ResponsibleTeacher.objects.filter(school = self.school)
        if responsible_teacher:
            return responsible_teacher[0].email
        else:
            return 'Not specified' #This should not happen!

    def school_name(self):
        #school_name = School.objects.filter(pk=self.school.id)
        #if school_name:
        return self.school.name
        #else:
#            return 'Not specified' #This should not happen!

    rt_name.short_description = 'Resp. teach. name'
    rt_phone_primary.short_description = 'Resp. teach. phone'
    rt_email.short_description = 'Resp. teach. email'

    def __str__(self):
        return self.surname+', '+self.firstname
    class Meta:
        ordering = ['school', 'surname', 'firstname'] #defines the way the records are sorted.


class ResponsibleTeacher(models.Model):
    # ResponsibleTeacher registered by SchoolUser
    # One ResponsibleTeacher to one school

    school      = models.ForeignKey('School', db_column='School') 
    firstname   = models.CharField(max_length=255L, db_column='First_name')
    surname     = models.CharField(max_length=255L, db_column='Surname')
    phone_primary = models.CharField(max_length=15L, db_column='Phone (Primary)', blank=True)
    phone_alt = models.CharField(max_length=15L, db_column='Phone (Alternative)', blank=True)
    email       = models.CharField(max_length=50L, db_column='Email', blank=False)
    #registered_by = models.ForeignKey(User, db_column='Registered By')
    def __str__(self):
        return self.surname+', '+self.firstname+', '+self.phone_primary
    class Meta:
        ordering = ['school', 'surname', 'firstname'] #defines the way the records are sorted.


class SchoolStudentArchive(models.Model):
    # Duplicate of the SchoolStudent model with extra date field - 'archived'. Used for saving old data. 
    # Generated from the admin page 
    archived    = models.DateField(null=True, blank=True, db_column='Date Archived')
    firstname   = models.CharField(max_length=255L, db_column='First_name')
    surname     = models.CharField(max_length=255L, db_column='Surname')
    language    = models.CharField(max_length=1L, choices=(
        ('e', 'English'), 
        ('a', 'Afrikaans'),
		('b', 'Bilingual')
    ), db_column = 'Language')
    reference   = models.CharField(max_length=7L, db_column='Reference') 
    school      = models.ForeignKey('School', db_column='School') 
    score       = models.IntegerField(null=True, db_column='Score', blank=True) 
    rank        = models.IntegerField(null=True, db_column='Rank', blank=True) 
    grade       = models.IntegerField(db_column='Grade', 
        validators = [
            MaxValueValidator(12),
            MinValueValidator(0)
        ])
   # sex         = models.CharField(max_length=1L, db_column='Sex', blank=True) 
    venue       = models.CharField(max_length=40L, db_column='Venue', blank=True) 
    #registered_by = models.ForeignKey(User, db_column='Registered By')
    paired = models.BooleanField(db_column='Paired')

    def __str__(self):
        return 'pair '+str(self.reference) if self.surname == '' else self.surname+', '+self.firstname+' ('+self.archived+')'
    class Meta:
        ordering = ['archived','grade', 'surname', 'firstname','reference'] #defines the way the records are sorted.



class InvigilatorArchive(models.Model):
    # duplicate of the Invigilator model with extra date field - 'archived'. Used for saving old data. 
    # Generated from the admin page     

    archived    = models.DateField(null=True, blank=True, db_column='Date_Archived')
    school      = models.ForeignKey('School', db_column='School') 
    firstname   = models.CharField(max_length=255L, db_column='First_name')
    surname     = models.CharField(max_length=255L, db_column='Surname')
    venue       = models.ForeignKey('Venue', db_column='Venue', null=True, blank=True) 
    phone_primary = models.CharField(max_length=15L, db_column='Phone (Primary)', blank=True)
    phone_alt   = models.CharField(max_length=15L, db_column='Phone (Alternative)', blank=True) 
    email       = models.CharField(max_length=50L, db_column='Email', blank=False)
    #registered_by = models.ForeignKey(User, db_column='Registered By')
    def __str__(self):
        return self.surname+', '+self.firstname+' ('+str(self.archived)+')'
    class Meta:
        ordering = ['archived', 'school', 'surname', 'firstname'] #defines the way the records are sorted.


#Import_Export class functionality
#ModelResource for exporting data
class SchoolStudentResource(resources.ModelResource):
    class Meta:
        model = SchoolStudent

class SchoolResource(resources.ModelResource):
    class Meta:
        model = School

class InvigilatorResource(resources.ModelResource):
    #Custom fields for export.
    rt_name = fields.Field(attribute = 'rt_name', column_name='resp. teach. name')
    rt_phone_primary = fields.Field(attribute = 'rt_phone_primary', column_name='resp. teach. phone')
    rt_email = fields.Field(attribute = 'rt_email', column_name='resp. teach. email')
    school_name = fields.Field(attribute = 'school_name', column_name='school name') #otherwise it just printed the school id (forreign key)

    class Meta:
        model = Invigilator
        export_order = ('school_name', 'firstname', 'surname', 'phone_primary', 'phone_alt', 'email', 'venue', 'rt_name','rt_phone_primary','rt_email') #Custom order with custom-fields as last few columns (otherwise they are added in the front)


class VenueResource(resources.ModelResource):
    class Meta:
        model = Venue


