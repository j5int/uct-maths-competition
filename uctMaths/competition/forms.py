# forms.py
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm, Textarea
from django.forms import ModelChoiceField
from competition.models import SchoolStudent, School, Invigilator, ResponsibleTeacher, Venue, Competition
from django.forms.models import modelformset_factory
from django.contrib.auth.models import User


#**********************************
#FORM FOR COMPETITION ADMINISTRATION
class CompetitionForm (ModelForm):
    class Meta:
        model=Competition
        fields = "__all__"
        
class CompetitionForm (forms.Form): #THERE MUST ONLY BE ONE OF THESE!
        fields = ['newentries_Opendate', 'newentries_Closedate']
        newentries_Opendate = forms.DateField()
        newentries_Closedate = forms.DateField()
        admin_emailaddress = forms.CharField()
        number_of_pairs = forms.IntegerField()
        number_of_individuals = forms.IntegerField()
        prizegiving_date = forms.DateField()

#**********************************
#FORM TO ENTER A NEW SCHOOL STUDENT
class StudentForm (ModelForm):
    class Meta:
        model=SchoolStudent
        fields = "__all__"
        
class StudentForm (forms.Form):
        fields = ['firstname', 'surname', 'language', 'school', 'grade', 'venue', 'location']
        firstname = forms.CharField()
        surname = forms.CharField()
        language = forms.CharField()
        school = forms.ModelChoiceField(required=True, widget = forms.Select(), queryset = School.objects.all()) #give all the school options
        grade = forms.IntegerField()
        pair = forms.BooleanField()
        award = forms.CharField()
        location = forms.CharField()

#**************************************
#FORM TO ENTER A NEW SCHOOL
class SchoolForm (ModelForm):
    class Meta:
        model=School
        fields = "__all__"

class SchoolForm (forms.Form):
        fields = ['name', 'language', 'address', 'phone', 'fax', 'contact', 'email', 'assigned_user', 'location']
        name = forms.CharField()
        language = forms.CharField()
        address = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
        phone = forms.CharField()
        fax = forms.CharField()
        contact = forms.CharField()
        email = forms.CharField()
        assigned_user = forms.ModelChoiceField(required=False, queryset = User.objects.all()) #user_name foreign key
        location = forms.CharField()

#**************************************
#SCHOOL SELECTION FORM
class SchoolSelectForm (ModelForm):
    class Meta:
        model=School
        fields = "__all__"

class SchoolSelectForm (forms.Form):
        fields = ['school_name']
        assign_to = forms.ModelChoiceField(required=True, queryset = User.objects.all())

#********************************  
#FORM TO ENTER NEW INVIGILATOR
class InvigilatorForm (ModelForm):
    class Meta:
        model=Invigilator
        fields = "__all__"

class InvigilatorForm (forms.Form):
        fields = ['school', 'firstname','surname', 'invig_reg','phone_primary','phone_alt', 'email', 'notes',
                  'rt_name', 'rt_phone_primary', 'location']
        school = forms.ModelChoiceField(required=False, widget = forms.Select(), queryset = School.objects.all()) #gives all school options
        firstname = forms.CharField()
        surname = forms.CharField()
        inv_reg = forms.CharField(required=False)
        phone_primary = forms.CharField()
        phone_alt = forms.CharField()
        email = forms.CharField()
        notes = forms.CharField()
        location = forms.CharField()

#*****************************************

#*****************************************
#FORM TO ENTER NEW RESPONSIBLE TEACHER
class ResponsibleTeacherForm (ModelForm):
    class Meta:
        model=ResponsibleTeacher
        fields = "__all__"

class ResponsibleTeacherForm(forms.Form):
        fields = ['school', 'firstname','surname', 'phone_primary','phone_alt', 'phone_cell', 'email_school', 'email_personal']
        school = forms.ModelChoiceField(required=False, widget = forms.Select(), queryset = School.objects.all()) #gives all school options
        firstname = forms.CharField()
        surname = forms.CharField()
        phone_primary = forms.CharField()
        phone_alt = forms.CharField()
        phone_cell = forms.CharField()
        email_school = forms.CharField()
        email_personal = forms.CharField()

#*****************************************

class UploadResultsForm(forms.Form):
        upload_file = forms.FileField(
                        label='Select a file'
                        #help_text = 'Hope this works!'
                        )
#*****************************************


