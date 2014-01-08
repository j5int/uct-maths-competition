# forms.py
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
        
class CompetitionForm (forms.Form): #THERE MUST ONLY BE ONE OF THESE!
        fields = ['newentries_Opendate', 'newentries_Closedate']
        newentries_Opendate = forms.DateField()
        newentries_Closedate = forms.DateField()
        admin_emailaddress = forms.CharField()
        #prizegiving_date = forms.DateField()

#**********************************
#FORM TO ENTER A NEW SCHOOL STUDENT
class StudentForm (ModelForm):
    class Meta:
        model=SchoolStudent
        
class StudentForm (forms.Form):
        fields = ['firstname', 'surname', 'language', 'school','grade','venue', 'registered_by']
        firstname = forms.CharField()
        surname = forms.CharField()
        language = forms.CharField()
        school = forms.ModelChoiceField(required=True, widget = forms.Select(), queryset = School.objects.all()) #give all the school options
        grade = forms.IntegerField()
     #   sex = forms.CharField()
        pair = forms.BooleanField()
        #registered_by = forms.ModelChoiceField(required=True, queryset = User.objects.all()) #for foreign key

#**************************************
#FORM TO ENTER A NEW SCHOOL
class SchoolForm (ModelForm):
    class Meta:
        model=School

class SchoolForm (forms.Form):
        fields = ['name', 'language', 'address','phone','fax','contact','email','assigned_user']
        name = forms.CharField()
        language = forms.CharField()
        address = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
        phone = forms.CharField()
        fax = forms.CharField()
        contact = forms.CharField()
        email = forms.CharField()
        #registered_by = forms.ModelChoiceField(required=False, queryset = User.objects.all())  #for foreign key
        assigned_user = forms.ModelChoiceField(required=False, queryset = User.objects.all()) #user_name forreign key

#**************************************
#SCHOOL SELECTION FORM
class SchoolSelectForm (ModelForm):
    class Meta:
        model=School

class SchoolSelectForm (forms.Form):
        fields = ['school_name']
        assign_to = forms.ModelChoiceField(required=True, queryset = User.objects.all())

#********************************  
#FORM TO ENTER NEW INVIGILATOR
class InvigilatorForm (ModelForm):
    class Meta:
        model=Invigilator

class InvigilatorForm (forms.Form):
        #fields = ['school','firstname','surname', 'grade', 'invig_reg','phone_h','phone_w','fax','fax_w','email','responsible']
        fields = ['school', 'firstname','surname', 'invig_reg','phone_primary','phone_alt', 'email', 'rt_name', 'rt_phone_primary']
        school = forms.ModelChoiceField(required=False, widget = forms.Select(), queryset = School.objects.all()) #gives all school options
        firstname = forms.CharField()
        surname = forms.CharField()
        inv_reg = forms.CharField(required=False)
        phone_primary = forms.CharField()
        phone_alt = forms.CharField()
        email = forms.CharField()
        #registered_by = forms.ModelChoiceField(required=False, queryset = User.objects.all()) #for foreign key

#*****************************************

#*****************************************
#FORM TO ENTER NEW RESPONSIBLE TEACHER
class ResponsibleTeacherForm (ModelForm):
    class Meta:
        model=ResponsibleTeacher

class ResponsibleTeacherForm(forms.Form):
        fields = ['school', 'firstname','surname', 'phone_primary','phone_alt', 'email']
        school = forms.ModelChoiceField(required=False, widget = forms.Select(), queryset = School.objects.all()) #gives all school options
        firstname = forms.CharField()
        surname = forms.CharField()
        phone_primary = forms.CharField()
        phone_alt = forms.CharField()
        email = forms.CharField()
        #registered_by = forms.ModelChoiceField(required=False, queryset = User.objects.all()) #for foreign key

#*****************************************

class UploadResultsForm(forms.Form):
        upload_file = forms.FileField(
                        label='Select a file'
                        #help_text = 'Hope this works!'
                        )
#*****************************************


