# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import loader, Context
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django import forms
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from competition.forms import StudentForm, SchoolForm, InvigilatorForm, VenueForm, testForm #, StudentFilter
from competition.models import SchoolStudent, School, Invigilator, Venue 
from django.contrib.auth.models import User

from django.contrib.auth.models import User, check_password


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


# submitted things
def submitted(request, c):
  return render_to_response('submitted.html', c)

# def regStudent (request, ):
#    return render_to_response('regStudent.html',{})

#def index(request):
 #   return render_to_response('onlinemaths.html', {})

#******************************************
# View Students
def students(request):
    return render_to_response('students.html',{})
# View Schools
def schools(request):
    return render_to_response('schools.html',{})
# View Invigilators
def invigilators(request):
    return render_to_response('invigilators.html',{})

# View Venues, Admin only
def venues(request):
    return render_to_response('venues.html',{})

# Register Students    
def newstudents(request):
    if request.method == 'POST': # If the form has been submitted...
        form = (request.POST) # A form bound to the POST data
        for i in range (2):
          firstname = form.getlist('firstname',"")[i]
          surname = form.getlist('surname',"")[i]
          language = form.getlist('language',"")[i]
          reference = 1234
          school = School.objects.get(pk=int(form.getlist('school',"")[i]))
          # print "here2 ", firstname
          # print "here3 ", school
          grade = form.getlist('grade',"")[i]
          sex = form.getlist('sex',"")[i]  
          registered_by =  User.objects.get(pk=int(form.getlist('registered_by',"")[i]))          
          query = SchoolStudent(firstname = firstname , surname = surname, language = language,reference = reference,
                  school = school, grade = grade , sex = sex, registered_by= registered_by)
          query.save()
        return render_to_response('submitted.html', {'type':'Student'}) # Redirect after POST
    else:
        form = StudentForm() # An unbound form

    schoolOptions = School.objects.all()
    c = {'type':'Students', 'schools':schoolOptions, 'range':range(2)}
    c.update(csrf(request))
    return render_to_response('newstudents.html', c, context_instance=RequestContext(request))


#*****************************************
#Register Schools
def newschools (request):
  if request.method == 'POST': # If the form has been submitted...
        form = (request.POST) # A form bound to the POST data
        for i in range (2):
            name = form.getlist('name',"")[i]
            key = "1234" #************FIX!!!!!!!!!!!!!!!!
            language = form.getlist('language',"")[i]
            address = form.getlist('address',"")[i]
            phone = form.getlist('phone',"")[i]
            fax = form.getlist('fax',"")[i]
            contact = form.getlist('contact',"")[i]
            email = form.getlist('email',"")[i]
            registered_by =  User.objects.get(pk=int(form.getlist('registered_by',"")[i]))
            
            query = School(name = name ,key = key ,  language = language  ,
                address = address, phone = phone , fax = fax, contact = contact , email = email, registered_by= registered_by)
            query.save()

        return render_to_response('submitted.html', {'type':'School'}) # Redirect after POST
  else:
        form = SchoolForm() # An unbound form
  

  c = {'type':'Schools', 'range':range(2)} #****** ADD RANGE
  c.update(csrf(request))
  return render_to_response('newschools.html', c, context_instance=RequestContext(request))

#******************************************
#Register Invigilators
def newinvigilators (request):
  if request.method == 'POST': # If the form has been submitted...
        form = (request.POST) # A form bound to the POST data
        for i in range (1):
            school = School.objects.get(pk=int(form.getlist('school',"")[i]))
            firstname = form.getlist('firstname',"")[i]
            surname = form.getlist('surname',"")[i]
            grade = form.getlist('grade',"")[i]
            venue = Venue.objects.get(pk=int(form.getlist('venue',"")[i]))
            inv_reg = form.getlist('inv_reg',"")[i]
            phone_h = form.getlist('phone_h',"")[i]
            phone_w = form.getlist('phone_w',"")[i]
            fax_h = form.getlist('fax_h',"")[i]
            fax_w = form.getlist('fax_w',"")[i]
            email = form.getlist('email',"")[i]
            responsible = form.getlist('responsible',"")[i]
            registered_by =  User.objects.get(pk=int(form.getlist('registered_by',"")[i]))
                        
            query = Invigilator(school = school , firstname = firstname,surname = surname, grade = grade ,
                venue = venue ,inv_reg = inv_reg,
                phone_h = phone_h , phone_w = phone_w, 
                fax_h = fax_h, fax_w = fax_w , email = email, responsible = responsible, registered_by= registered_by)
            query.save()

        return render_to_response('submitted.html', {'type':'Invigilator'}) # Redirect after POST
  else:
        form = InvigilatorForm() # An unbound form
  schoolOptions = School.objects.all()

  c = {'schools':schoolOptions, 'range':range(2)} #******ADD RANGE
  c.update(csrf(request))
  return render_to_response('newinvigilators.html', c, context_instance=RequestContext(request))

#***************************************
#Register Venues
def newvenues (request):
    if request.method == 'POST': # If the form has been submitted...
        form = (request.POST) # A form bound to the POST data
        for i in range (1):
            code = form.getlist('code',"")[i]
            building = form.getlist('building',"")[i]
            seats = form.getlist('seats',"")[i]
            bums = form.getlist('bums',"")[i]
            grade = form.getlist('grade',"")[i]
            pairs = form.getlist('pairs',"")[i]
            registered_by =  User.objects.get(pk=int(form.getlist('registered_by',"")[i]))
                        
            query = Venue(code = code , building = building  ,
                seats = seats, bums = bums , grade = grade, pairs = pairs,registered_by= registered_by)
            query.save()

        return render_to_response('submitted.html', {'type':'Venue'}) # Redirect after POST
    else:
        form = VenueForm() # An unbound form
   
    c = {'type':'Invigilators','range':range(1)}
    c.update(csrf(request))
    return render_to_response('newvenues.html', c, context_instance=RequestContext(request))

#******************************************  
def search_form (request):
  building = ""
  #code = ""
  if request.method == 'POST': # If the form has been submitted...
        form = testForm(request.POST) # A form bound to the POST data
        #print "FORM ", form
        print "here1", form
        print "here2", form.is_valid()
        if form.is_valid():
            building = form.cleaned_data['building']
            #code = form.cleaned_data['code']
            
            #return HttpResponseRedirect("IT'S BEEN SUBMITTED") # Redirect after POST
  else:
        form = testForm() # An unbound form
  venueOptions = Venue.objects.filter(building=building)
  #venueOptions1 = Venue.objects.filter(code=code)
  print venueOptions
  c = {'temp':venueOptions}#, 'temp1':venueOptions1}
  c.update(csrf(request))
  return render_to_response('search_form.html', c)
    
