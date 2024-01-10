# models.py
# defines django models (correspond to db tables)
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
#Import_export models(https://django-import-export.readthedocs.org/en/latest/getting_started.html)

LOCATIONS = (
    ('C', 'Cape Town'),
    ('G', 'George')
)

class Competition(models.Model):
    newentries_Opendate = models.DateField(db_column='newentries_Opendate', verbose_name="Opening date for entries")
    newentries_Closedate = models.DateField(db_column='newentries_Closedate', verbose_name="Closing date for entries")
    admin_emailaddress = models.CharField(max_length=30, verbose_name="Admin email address")
    num_schoolcandidate_scores = models.IntegerField(db_column='num_schoolcandidate_scores', null=True, verbose_name="Number of school candidate scores")
    number_of_individuals = models.IntegerField(db_column='num_individuals', verbose_name="Maximum individual entries per grade per school")
    number_of_pairs = models.IntegerField(db_column='num_pairs', verbose_name="Maximum pair entries per grade per school")
    prizegiving_date = models.DateField(db_column='prizegiving_date', verbose_name="Prize-giving date")
    invigilators = models.BooleanField(db_column='invigilators', default=False,
                                        verbose_name="Require schools to provide invigilators")
    answer_sheet_download_enabled = models.BooleanField(db_column='answer_sheet_download_enabled', default=False,
                                                        verbose_name="Allow teachers to download answer sheets")


def _on_delete(school, *args, **kwargs):
    pass

class School(models.Model):
    # Contains school information. Duplicates should not be allowed, but will be removed by the admin.
    name        = models.CharField(max_length=255, db_column='Name', verbose_name="School name")
    key         = models.CharField(max_length=3, db_column='Key', unique=True)
    language    = models.CharField(max_length=1, choices=(
    ('e', 'English'), 
    ('a', 'Afrikaans'), 
    ('b', 'Bilingual')
    ), db_column = 'Language')
    address     = models.CharField(max_length=255, db_column='Address', blank=True)
    phone       = models.CharField(max_length=15, db_column='Phone', blank=True) 
    fax         = models.CharField(max_length=15, db_column='Fax', blank=True) 
    contact     = models.CharField(max_length=255, db_column='Contact', blank=True)
    entered     = models.IntegerField(null=True, db_column='Entered') 
    score       = models.IntegerField(null=True, db_column='Score', blank=True) 
    email       = models.CharField(max_length=50, db_column='Email', blank=True) 
    assigned_to = models.ForeignKey(User, default=None, null=True, db_column='Assigned to', blank=True, on_delete=_on_delete) #ForeignKey (gets assigned a single user)
    rank = models.IntegerField(null=True, db_column='Rank', blank=True)
    location = models.CharField(max_length=3, choices=LOCATIONS, db_column='Location')
    answer_sheets_emailed = models.DateTimeField(db_column="answer_sheets_emailed", blank=True, verbose_name="Answer sheets emailed to teacher")
    report_emailed = models.DateTimeField(db_column="report_emailed", blank=True, verbose_name="Results report emailed to teacher")

    def __str__(self):
        return self.name
    def getFormatName(self):
        return u'%s'%(self.name)
    class Meta:
        ordering = ['name']     #defines the way the records are sorted.


class SchoolStudent(models.Model):
    # A single student. Not a User. Score and Rank will added/updated by the admin so they can be null.
    firstname   = models.CharField(max_length=255, db_column='First_name', verbose_name="First name")
    surname     = models.CharField(max_length=255, db_column='Surname')
    language    = models.CharField(max_length=1, choices=(
        ('e', 'English'), 
        ('a', 'Afrikaans'),
		('b', 'Bilingual')
    ), db_column = 'Language')
    reference   = models.CharField(max_length=7, db_column='Reference') 
    school      = models.ForeignKey('School', db_column='School', on_delete=lambda x:x)
    score       = models.IntegerField(null=True, db_column='Score', blank=True) 
    rank        = models.IntegerField(null=True, db_column='Rank', blank=True) 
    grade       = models.IntegerField(db_column='Grade', 
        validators = [
            MaxValueValidator(12),
            MinValueValidator(8)
        ])
    venue       = models.CharField(max_length=40, db_column='Venue', blank=True)
    paired = models.BooleanField(db_column='Paired', default=False)
    award = models.CharField(max_length=3, db_column='Award', null=True, blank=True)
    location = models.CharField(max_length=3, choices=LOCATIONS, db_column='Location')

    def __str__(self):
        return self.surname+', '+self.firstname

    def __unicode__(self):
        return u'%s, %s'%(self.surname,self.firstname)
    class Meta:
        ordering = ['school', 'grade', 'surname', 'firstname','reference'] #defines the way the records are sorted.

class Venue(models.Model):
    '''Venues are the rooms where individuals or pairs from the same grade write the competition.
    Many SchoolStudents to one Venue.'''
    # code is used as an Excel worksheet name which can be no longer than 31 characters
    code        = models.CharField(max_length=31, db_column='Code', unique=True)
    building    = models.CharField(max_length=40, db_column='Building') 
    seats       = models.IntegerField(db_column='Seats')
    grade       = models.IntegerField(db_column='Grade', null=True, blank=True, choices = zip(range(8,13), range(8,13)))
    allocated_to_pairs = models.BooleanField(db_column='Allocated to PAIRS', default=False)
    occupied_seats = models.IntegerField(db_column='Occupied seats', blank=True, null=True)
    location = models.CharField(max_length=3, choices=LOCATIONS, db_column='Location')

    def __str__(self):
        return self.building+' '+self.code
    def __unicode__(self):
        return u'%s, %s'%(self.building,self.code)
    class Meta:
        ordering = ['building', 'code'] #defines the way the records are sorted.
        

class Invigilator(models.Model):
    # Invigilators registered by SchoolUsers. Many Invigilators to one School.
    # Many Invigilators to one Venue.

    school      = models.ForeignKey('School', db_column='School', on_delete=lambda x:x)
    firstname   = models.CharField(max_length=255, db_column='First_name', verbose_name="First name")
    surname     = models.CharField(max_length=255, db_column='Surname')
    venue       = models.ForeignKey('Venue', db_column='Venue', null=True, blank=True, on_delete=lambda x:x) #Admin feature, implement later
    phone_primary = models.CharField(max_length=15, db_column='Phone (Primary)', blank=True)
    phone_alt = models.CharField(max_length=15, db_column='Phone (Alternative)', blank=True)
    email       = models.CharField(max_length=50, db_column='Email', blank=False)
    notes       = models.CharField(max_length=500, db_column='Notes', blank=True)
    location    = models.CharField(max_length=3, choices=LOCATIONS, db_column='Location')

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
            return responsible_teacher[0].email_personal
        else:
            return 'Not specified' #This should not happen!

    def school_name(self):
        return self.school.name

    rt_name.short_description = 'Resp. teach. name'
    rt_phone_primary.short_description = 'Resp. teach. phone'
    rt_email.short_description = 'Resp. teach. email'

    def __str__(self):
        return self.surname+', '+self.firstname
    def __unicode__(self):
        return u'%s, %s'%(self.surname,self.firstname)
    class Meta:
        ordering = ['school', 'surname', 'firstname'] #defines the way the records are sorted.


class ResponsibleTeacher(models.Model):
    # ResponsibleTeacher registered by SchoolUser
    # One Primary ResponsibleTeacher and one Alternate ResponsibleTeacher to one school

    school      = models.ForeignKey('School', db_column='School', on_delete=lambda x:x)
    firstname   = models.CharField(max_length=255, db_column='First_name', verbose_name="First name")
    surname     = models.CharField(max_length=255, db_column='Surname')
    phone_primary = models.CharField(max_length=15, db_column='Phone (Primary)', blank=True)
    phone_alt   = models.CharField(max_length=15, db_column='Phone (Alternative)', blank=True)
    phone_cell  = models.CharField(max_length=15, db_column='Cellphone', blank=True)
    email_school   = models.CharField(max_length=50, db_column='Email (School)', blank=False)
    email_personal = models.CharField(max_length=50, db_column='Email (Personal)', blank=True) 
    is_primary  = models.BooleanField(db_column='Is_primary', default="true")
    report_downloaded = models.DateTimeField(db_column='Report_downloaded', blank=True, null=True, verbose_name="Results report downloaded manually by teacher")
    answer_sheet_downloaded = models.DateTimeField(db_column='Answer_sheet_downloaded', blank=True, null=True, verbose_name="Answer sheets downloaded manually by teacher")
    def __str__(self):
        return self.surname+', '+self.firstname+', '+self.phone_primary
    def __unicode__(self):
        return u'%s, %s'%(self.surname,self.firstname)
        
    class Meta:
        ordering = ['school', 'surname', 'firstname'] #defines the way the records are sorted.


class SchoolStudentArchive(models.Model):
    # Duplicate of the SchoolStudent model with extra date field - 'archived'. Used for saving old data. 
    # Generated from the admin page 
    archived    = models.DateField(null=True, blank=True, db_column='Date Archived')
    firstname   = models.CharField(max_length=255, db_column='First_name', verbose_name="First name")
    surname     = models.CharField(max_length=255, db_column='Surname')
    language    = models.CharField(max_length=1, choices=(
        ('e', 'English'), 
        ('a', 'Afrikaans'),
		('b', 'Bilingual')
    ), db_column = 'Language')
    reference   = models.CharField(max_length=7, db_column='Reference') 
    school      = models.ForeignKey('School', db_column='School', on_delete=lambda x:x)
    score       = models.IntegerField(null=True, db_column='Score', blank=True) 
    rank        = models.IntegerField(null=True, db_column='Rank', blank=True) 
    grade       = models.IntegerField(db_column='Grade', 
        validators = [
            MaxValueValidator(12),
            MinValueValidator(8)
        ])
    venue       = models.CharField(max_length=40, db_column='Venue', blank=True)
    paired = models.BooleanField(db_column='Paired', default=False)
    location = models.CharField(max_length=3, choices=LOCATIONS, db_column='Location')

    def __str__(self):
        return 'pair '+str(self.reference) if self.surname == '' else self.surname+', '+self.firstname+' ('+self.archived+')'
    def __unicode__(self):
        return u'%s, %s (%s)'%(self.surname,self.firstname,self.archived)
    class Meta:
        ordering = ['archived','grade', 'surname', 'firstname','reference'] #defines the way the records are sorted.



class InvigilatorArchive(models.Model):
    # duplicate of the Invigilator model with extra date field - 'archived'. Used for saving old data. 
    # Generated from the admin page     

    archived    = models.DateField(null=True, blank=True, db_column='Date_Archived', verbose_name="Date Archived")
    school      = models.ForeignKey('School', db_column='School', on_delete=lambda x:x)
    firstname   = models.CharField(max_length=255, db_column='First_name', verbose_name="First name")
    surname     = models.CharField(max_length=255, db_column='Surname')
    venue       = models.ForeignKey('Venue', db_column='Venue', null=True, blank=True, on_delete=lambda x:x)
    phone_primary = models.CharField(max_length=15, db_column='Phone (Primary)', blank=True)
    phone_alt   = models.CharField(max_length=15, db_column='Phone (Alternative)', blank=True) 
    email       = models.CharField(max_length=50, db_column='Email', blank=False)
    notes       = models.CharField(max_length=500, db_column='Notes', blank=False)
    location    = models.CharField(max_length=3, choices=LOCATIONS, db_column='Location')
    def __str__(self):
        return self.surname+', '+self.firstname+' ('+str(self.archived)+')'
    def __unicode__(self):
        return u'%s, %s (%s)'%(self.surname,self.firstname,self.archived)
    class Meta:
        ordering = ['archived', 'school', 'surname', 'firstname'] #defines the way the records are sorted.
