from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class SiteUser(models.Model):
    username    = models.CharField(max_length=16L, db_column='Name')
    password    = models.CharField(max_length=16L, db_column='Password')
    language    = models.CharField(max_length=1L, db_column='Language', choices=(
        ('e', 'English'), 
        ('a', 'Afrikaans')
    )) 
    counter     = models.IntegerField(db_column='Count')
    last_login  = models.DateField(null=True, blank=True, db_column='Last Login')
    non_uct     = models.IntegerField(db_column='Non UCT') 
    def __str__(self):
        return self.username
    class Meta:
        ordering = ['username']

class School(models.Model):
    name        = models.CharField(max_length=40L, db_column='Name') 
    key         = models.CharField(max_length=3L, db_column='Key') 
    language    = models.CharField(max_length=1L, choices=(
        ('e', 'English'), 
        ('a', 'Afrikaans')
    ), db_column = 'Language')
    address     = models.CharField(max_length=30L, db_column='Address', blank=True) 
    phone       = models.CharField(max_length=15L, db_column='Phone', blank=True) 
    fax         = models.CharField(max_length=15L, db_column='Fax', blank=True) 
    contact     = models.CharField(max_length=30L, db_column='Contact', blank=True) 
    entered     = models.IntegerField(null=True, db_column='Entered', blank=True) 
    score       = models.IntegerField(null=True, db_column='Score', blank=True) 
    email       = models.CharField(max_length=30L, db_column='Email', blank=True) 
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class SchoolStudent(models.Model):
    firstname   = models.CharField(max_length=32L, db_column='First_name') 
    surname     = models.CharField(max_length=32L, db_column='Surname')
    language    = models.CharField(max_length=1L, choices=(
        ('e', 'English'), 
        ('a', 'Afrikaans')
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
    sex         = models.CharField(max_length=1L, db_column='Sex', blank=True) 
    venue       = models.CharField(max_length=40L, db_column='Venue', blank=True) 
    def __str__(self):
        return "pair "+str(self.reference) if self.surname == "" else self.surname+", "+self.firstname
    class Meta:
        ordering = ['surname', 'firstname','reference']

class SchoolUser(SiteUser):
    school      = models.ForeignKey('School', db_column='School') 
    count       = models.IntegerField()
    address     = models.CharField(max_length=40L, db_column='Address') 
    town        = models.CharField(max_length=20L, db_column='Town') 
    postal_code = models.CharField(max_length=4L, db_column='Postal_Code') 
    phone       = models.CharField(max_length=15L, db_column='Telephone') 
    fax         = models.CharField(max_length=15L, db_column='Fax', blank=True) 
    email       = models.CharField(max_length=40L, db_column='Email', blank=True) 
    correction  = models.IntegerField(db_column='Correction') 
    entered     =  models.IntegerField(db_column='Entered')  
    class Meta:
        ordering = ['school', 'username']

class Venue(models.Model):
    code        = models.IntegerField(db_column='Code')
    building    = models.CharField(max_length=40L, db_column='Building') 
    seats       = models.IntegerField(db_column='Seats')
    bums        = models.IntegerField(db_column='Bums')
    grade       = models.IntegerField(db_column='Grade')
    pairs       = models.IntegerField(db_column='Pairs')
    def __str__(self):
        return self.building+", "+self.code
    class Meta:
        ordering = ['building', 'code']

class Invigilator(models.Model):
    school      = models.ForeignKey('School', db_column='School') 
    firstname   = models.CharField(max_length=32L, db_column='First_name') 
    surname     = models.CharField(max_length=32L, db_column='Surname')
    grade       = models.IntegerField(db_column='Grade', null=True,
        validators = [
            MaxValueValidator(12),
            MinValueValidator(0)
        ])
    venue       = models.ForeignKey('Venue', db_column='Venue', blank=True) 
    inv_reg     = models.CharField(max_length=1L, choices=(
        ('i', 'Invigilator'), 
        ('r', 'Registrator')
    ), db_column='Inv/Reg')
    phone_h     = models.CharField(max_length=15L, db_column='Phone (H)', blank=True) 
    phone_w     = models.CharField(max_length=15L, db_column='Phone (W)', blank=True) 
    fax         = models.CharField(max_length=15L, db_column='Fax', blank=True) 
    fax_w       = models.CharField(max_length=15L, db_column='Fax (W)', blank=True) 
    email       = models.CharField(max_length=40L, db_column='Email', blank=True) 
    responsible = models.CharField(max_length=40L, db_column='Responsible')
    def __str__(self):
        return self.surname+", "+self.firstname
    class Meta:
        ordering = ['school', 'surname', 'firstname']
        

