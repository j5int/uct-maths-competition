# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import loader, Context
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django import forms
from competition.forms import StudentForm, SchoolForm
from competition.models import SchoolStudent, School 


def index(request):
	return render_to_response('base.html', {})

def content (request):
   #t = loader.get_template('base.html')
   return render_to_response('contents.html',{})
   #return HttpResponse(t.render(base.html))

def profile(request):
    return render_to_response('profile.html',{})

def main (request):
   return render_to_response('main.html',{})


# def regStudent (request, ):
#    return render_to_response('regStudent.html',{})

#def index(request):
 #   return render_to_response('onlinemaths.html', {})

#******************************************
#ADDING STUDENT TO DB    
def regStudent(request):
   if request.method == 'POST': # If the form has been submitted...
        form = StudentForm(request.POST) # A form bound to the POST data
        #print "FORM ", form
        print "here1", form
        print "here2", form.is_valid()
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            firstname = form.cleaned_data['firstname']
            surname = form.cleaned_data['surname']
            language = form.cleaned_data['language']
            school = form.cleaned_data['school']
            grade = form.cleaned_data['grade']
            sex = form.cleaned_data['sex']
            
            query = SchoolStudent(firstname = firstname , surname = surname, language = language  ,
                school = school, grade = grade , sex = sex)
            query.save()

            return HttpResponseRedirect('/thanks/') # Redirect after POST
   else:
        form = StudentForm() # An unbound form
   schoolOptions = School.objects.all()
   c = {'schools':schoolOptions}
   c.update(csrf(request))
   return render_to_response('regStudent.html', c)

#*****************************************
#ADDING SCHOOL TO DB
def regSchool (request):
  if request.method == 'POST': # If the form has been submitted...
        form = SchoolForm(request.POST) # A form bound to the POST data
        #print "FORM ", form
        print "here1", form
        print "here2", form.is_valid()
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            name = form.cleaned_data['name']
            language = form.cleaned_data['language']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            fax = form.cleaned_data['fax']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            
            query = School(name = name , language = language  ,
                address = address, phone = phone , fax = fax, contact = contact , email = email)
            query.save()

            return HttpResponseRedirect('/thanks/') # Redirect after POST
  else:
        form = SchoolForm() # An unbound form
   
  c = {}
  c.update(csrf(request))
  return render_to_response('regSchool.html', c)

    
    
