# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    username = models.CharField(max_length=16L)
    password = models.CharField(max_length=16L)
    language = models.CharField(max_length=1L, db_column='Language', choices=(
        ('e', 'English'), 
        ('a', 'Afrikaans')
    )) 
    counter = models.IntegerField()
    last_login = models.DateField(null=True, blank=True)
    non_uct = models.IntegerField(db_column='Non_UCT') 
    def __unicode__(self):
        return self.username
    def Meta:
        ordering=['username']

class School(models.Model):
    name = models.CharField(max_length=40L, db_column='Name') 
    key = models.CharField(max_length=3L, db_column='Key') 
    language = models.CharField(max_length=1L, choices=(
        ('e', 'English'), 
        ('a', 'Afrikaans')
    ), db_column='Language')
    address = models.CharField(max_length=30L, db_column='Address', blank=True) 
    phone = models.CharField(max_length=15L, db_column='Phone', blank=True) 
    fax = models.CharField(max_length=15L, db_column='Fax', blank=True) 
    contact = models.CharField(max_length=30L, db_column='Contact', blank=True) 
    entered = models.IntegerField(null=True, db_column='Entered', blank=True) 
    score = models.IntegerField(null=True, db_column='Score', blank=True) 
    email = models.CharField(max_length=30L, db_column='Email', blank=True) 
    def __unicode__(self):
        return self.name
    def Meta:
        ordering=['name']

class SchoolStudent(models.Model):
    firstname = models.CharField(max_length=32L, db_column='First_name') 
    surname = models.CharField(max_length=32L, db_column='Surname')
    language = models.CharField(max_length=1L, choices=(
        ('e', 'English'), 
        ('a', 'Afrikaans')
    ), db_column='Language')
    reference = models.CharField(max_length=7L, db_column='Reference') 
    school = models.ForeignKey('School', db_column='School') 
    score = models.IntegerField(null=True, db_column='Score', blank=True) 
    rank = models.IntegerField(null=True, db_column='Rank', blank=True) 
    grade = models.IntegerField(db_column='Grade', 
        validators = [
            MaxValueValidator(12),
            MinValueValidator(0)
        ])    
    sex = models.CharField(max_length=1L, db_column='Sex', blank=True) 
    venue = models.CharField(max_length=40L, db_column='Venue', blank=True) 
    def __unicode__(self):
        return self.surname+", "+self.firstname
    def Meta:
        ordering=['surname', 'firstname']

class SchoolUser(User):
    school = models.ForeignKey('School', db_column='School') 
    count = models.IntegerField()
    address = models.CharField(max_length=40L, db_column='Address') 
    town = models.CharField(max_length=20L, db_column='Town') 
    postal_code = models.CharField(max_length=4L, db_column='Postal_Code') 
    telephone = models.CharField(max_length=15L, db_column='Telephone') 
    fax = models.CharField(max_length=15L, db_column='Fax', blank=True) 
    email = models.CharField(max_length=40L, db_column='Email', blank=True) 
    correction = models.IntegerField(db_column='Correction') 
    entered = models.IntegerField(db_column='Entered')  
    def Meta:
        ordering=['school']


