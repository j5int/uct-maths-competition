# forms.py
from django import forms
from django.forms import ModelForm
from django.forms import ModelChoiceField
from competition.models import SchoolStudent, School

class StudentForm (ModelForm):
    class Meta:
        model=SchoolStudent

class StudentForm (forms.Form):
        fields = ['firstname', 'surname', 'language', 'reference', 'school','grade','sex','venue']
        firstname = forms.CharField()
        surname = forms.CharField()
        language = forms.CharField()
        reference = forms.IntegerField ()
        school = forms.ModelChoiceField(required=False, widget = forms.Select(), queryset = School.objects.all())
        grade = forms.IntegerField()
        sex = forms.CharField ()
       

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)