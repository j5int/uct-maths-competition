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


def index(request):
	return render_to_response('index.html', {})

def profile(request):
    return render_to_response('profile.html',{})


# submitted thingszz
def submitted(request, c):
  return render_to_response('submitted.html', c)

# View Students
def students(request):
    username = request.user
    studentOptions = SchoolStudent.objects.filter(registered_by = username)
    if request.method=='POST' and 'delete' in request.POST:
        form = (request.POST) # A form bound to the POST data
        for i in range (studentOptions.count()): #RANGE!!!!!!!!
          studentUpdate = SchoolStudent.objects.get(id= form.getlist('studentID',"")[i])
          studentUpdate.delete()
          
    elif request.method=='POST' and 'submit' in request.POST:
        form = (request.POST) # A form bound to the POST data
        for i in range (studentOptions.count()): #RANGE!!!!!!!!
          studentID = form.getlist('studentID',"")[i]
          studentUpdate = SchoolStudent.objects.get(id= studentID)
          studentUpdate.firstname = form.getlist('firstname',"")[i]
          studentUpdate.surname = form.getlist('surname',"")[i]
          studentUpdate.sex = form.getlist('sex',"")[i]
          studentUpdate.save()
         
    c = {'students':studentOptions}
    c.update(csrf(request))
    return render_to_response('students.html', c,context_instance=RequestContext(request))

# View Schools
def schools(request):
    username = request.user
    schoolOptions = School.objects.filter(registered_by = username)
    
    if request.method=='POST' and 'delete' in request.POST:
        form = (request.POST) # A form bound to the POST data
        for i in range (schoolOptions.count()): #RANGE!!!!!!!!
          schoolUpdate = School.objects.get(id= form.getlist('schoolID',"")[i])
          schoolUpdate.delete()

    elif request.method=='POST' and 'submit' in request.POST:
        form = (request.POST) # A form bound to the POST data
        for i in range (schoolOptions.count()): #RANGE!!!!!!!!
          schoolID = form.getlist('schoolID',"")[i]
          schoolUpdate = SchoolStudent.objects.get(id= schoolID)
          schoolUpdate.name = form.getlist('name',"")[i]
          schoolUpdate.address = form.getlist('address',"")[i]
          schoolUpdate.language = form.getlist('language',"")[i]
          schoolUpdate.phone = form.getlist('phone',"")[i]
          schoolUpdate.email = form.getlist('email',"")[i]
          schoolUpdate.contact = form.getlist('contact',"")[i]
          schoolUpdate.fax = form.getlist('fax',"")[i]
          schoolUpdate.save()
          
    c = {'schools':schoolOptions}
    c.update(csrf(request))
    return render_to_response('schools.html', c,context_instance=RequestContext(request))

# View Invigilators
def invigilators(request):
    username = request.user
    invigilators = Invigilator.objects.filter(registered_by = username)
    
    if request.method=='POST' and 'delete' in request.POST:
        form = (request.POST) # A form bound to the POST data
        for i in range (invigilators.count()): #RANGE!!!!!!!!
          invigilatorUpdate = Invigilator.objects.get(id= form.getlist('schoolID',"")[i])
          invigilatorUpdate.delete()

    elif request.method=='POST' and 'submit' in request.POST:
        form = (request.POST) # A form bound to the POST data
        for i in range (invigilators.count()): #RANGE!!!!!!!!
          invigilatorID = form.getlist('invigilatorID',"")[i]
          invigilatorUpdate = SchoolStudent.objects.get(id= invigilatorID)
          invigilatorUpdate.firstname = form.getlist('firstname',"")[i]
          invigilatorUpdate.surname = form.getlist('surname',"")[i]
          invigilatorUpdate.school = form.getlist('school',"")[i]
          invigilatorUpdate.grade = form.getlist('grade',"")[i]
          invigilatorUpdate.venue = form.getlist('venue',"")[i]
          invigilatorUpdate.inv_reg = form.getlist('inv_reg',"")[i]
          invigilatorUpdate.phone_h = form.getlist('phone_h',"")[i]
          invigilatorUpdate.phone_w = form.getlist('phone_w',"")[i]
          invigilatorUpdate.fax_h = form.getlist('fax_h',"")[i]
          invigilatorUpdate.fax_w = form.getlist('fax_w',"")[i]
          invigilatorUpdate.email = form.getlist('email',"")[i]
          invigilatorUpdate.responsible = form.getlist('responsible',"")[i]
          invigilatorUpdate.save()
       
    c = {'invigilators':invigilators}
    c.update(csrf(request))
    return render_to_response('invigilators.html', c,context_instance=RequestContext(request))

# View Venues, Admin only
# def venues(request):
#     username = request.user
#     userType = request.user.is_superuser
#     venues = Venue.objects.filter(registered_by = username)
#     # print venues
#     if userType:
#       if request.method == 'POST': # If the form has been submitted...
#           form = (request.POST) # A form bound to the POST data
#           for i in range (venues.count()): #RANGE!!!!!!!!
#             venueID = form.getlist('venueID',"")[i]
#             venueUpdate = SchoolStudent.objects.get(id= venueID)
#             venueUpdate.building = form.getlist('building',"")[i]
#             venueUpdate.code = form.getlist('code',"")[i]
#             venueUpdate.seats = form.getlist('seats',"")[i]
#             venueUpdate.bums = form.getlist('bums',"")[i]
#             venueUpdate.grade = form.getlist('grade',"")[i]
#             venueUpdate.pairs = form.getlist('pairs',"")[i]
#             venueUpdate.save()
#           # print "here!! ", venueUpdate
#     c = {'venues':venues, 'userType':userType}
#     c.update(csrf(request))
#     return render_to_response('venues.html', c,context_instance=RequestContext(request))

# Register Students    
def newstudents(request):
    error = " "
    if request.method == 'POST':  # If the form has been submitted...
       # print "here gg"
        form = (request.POST) # A form bound to the POST data
        for grade in range (8,13):
          # print "here1!!!! " , int(form.getlist("pairs","")[grade-8])
          for p in range(int(form.getlist("pairs","")[grade-8])):
            firstname = ""
            surname = ""
            language = form.getlist('language',"")[0]
            reference = 1234
            school = School.objects.get(pk=int(form.getlist('school',"")[0]))
            # print "here2 ", firstname
            # print "here3 ", school
            # grade = form.getlist('grade',"")[i]
            sex = "" 
            registered_by =  User.objects.get(pk=int(form.getlist('registered_by',"")[p]))          
            query = SchoolStudent(firstname = firstname , surname = surname, language = language,reference = reference,
                    school = school, grade = grade , sex = sex, registered_by= registered_by)
            query.save()
            query.reference=query.id
            query.save()
            query1 = SchoolStudent(firstname = firstname , surname = surname, language = language,reference = query.id,
                    school = school, grade = grade , sex = sex, registered_by= registered_by)
            query1.save()            
        try:
          for i in range (25):
            if form.getlist('firstname',"")[i] == u'': continue
            firstname = form.getlist('firstname',"")[i]
            surname = form.getlist('surname',"")[i]
            language = form.getlist('language',"")[0]
            reference = 1234
            school = School.objects.get(pk=int(form.getlist('school',"")[0]))
            grade = form.getlist('grade',"")[i]
            sex = form.getlist('sex',"")[i]  
            registered_by =  User.objects.get(pk=int(form.getlist('registered_by',"")[i]))          
            query = SchoolStudent(firstname = firstname , surname = surname, language = language,reference = reference,
                    school = school, grade = grade , sex = sex, registered_by= registered_by)
            query.save()

          return render_to_response('submitted.html', {'type':'Student'}) # Redirect after POST
        except Exception as e:
              error = "Incorrect information inserted into fields. Please insert correct information"
    else:
        form = StudentForm() # An unbound form
        

    schoolOptions = School.objects.all()
    c = {'type':'Students', 'schools':schoolOptions, 'entries_per_grade':range(5), 'pairs_per_grade':range(6), 'grades':range(8,13), 'error':error}
    c.update(csrf(request))
    return render_to_response('newstudents.html', c, context_instance=RequestContext(request))


#*****************************************
#Register Schools
def newschools (request):
  error = " "
  if request.method == 'POST': # If the form has been submitted...
        form = (request.POST) # A form bound to the POST data
        # print form
        try:
          for i in range (2):
              if form.getlist('name',"")[i] == u'': continue
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
        except Exception as e:
              error = "Incorrect information inserted into fields. Please insert correct information"
  else:
        form = SchoolForm() # An unbound form
  

  c = {'type':'Schools', 'range':range(2), 'error':error} #****** ADD RANGE
  c.update(csrf(request))

  return render_to_response('newschools.html', c,context_instance=RequestContext(request))


#******************************************
#Register Invigilators
def newinvigilators (request):
  error = " "
  if request.method == 'POST': # If the form has been submitted...
        form = (request.POST) # A form bound to the POST data
        try:
          for i in range (1):
              if form.getlist('firstname',"")[i] == u'': continue
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
        except Exception as e:
              error = "Incorrect information inserted into fields. Please insert correct information"
  else:
        form = InvigilatorForm() # An unbound form
  schoolOptions = School.objects.all()

  c = {'schools':schoolOptions, 'range':range(2), 'grades':range(8,13), 'error':error} #******ADD RANGE

  c.update(csrf(request))
  return render_to_response('newinvigilators.html', c,context_instance=RequestContext(request))


#***************************************
# Register Venues
# def newvenues (request):
#     # print "here1", request.method
#     error = " "
#     if request.method == 'POST': # If the form has been submitted...
#         form = (request.POST) # A form bound to the POST data
#         try: 
#           for i in range (1):
#               if form.getlist('building',"")[i] == u'': continue
#               code = form.getlist('code',"")[i]
#               building = form.getlist('building',"")[i]
#               seats = form.getlist('seats',"")[i]
#               bums = form.getlist('bums',"")[i]
#               grade = form.getlist('grade',"")[i]
#               pairs = form.getlist('pairs',"")[i]
#               registered_by =  User.objects.get(pk=int(form.getlist('registered_by',"")[i]))
                          
#               query = Venue(code = code , building = building  ,
#                   seats = seats, bums = bums , grade = grade, pairs = pairs,registered_by= registered_by)
#               query.save()

#           return render_to_response('submitted.html', {'type':'Venue'}) # Redirect after POST
#         except Exception as e:
#               error = "Error in input"
              
#     else:
#         form = VenueForm() # An unbound form
   
#     c = {'type':'Invigilators','range':range(1), 'grades':range(8,13), 'error':error}

#     c.update(csrf(request))
#     return render_to_response('newvenues.html', c, context_instance=RequestContext(request))


#******************************************  
def search_form (request):
    username = request.user
    print "user: ", request.user.is_superuser # DETERMINES TYPE OF STAFF
    studentOptions = SchoolStudent.objects.filter(registered_by = username)
    print studentOptions
    if request.method == 'POST': # If the form has been submitted...
        form = (request.POST) # A form bound to the POST data
        for i in range (2):
          studentID = form.getlist('studentID',"")[i]
          studentUpdate = SchoolStudent.objects.get(id= studentID)
          studentUpdate.firstname = form.getlist('firstname',"")[i]
          studentUpdate.surname = form.getlist('surname',"")[i]
          studentUpdate.save()
    # studentTemp.surname = "ww"

    # # studentTemp.delete()
    # print "student! ", studentTemp
    c = {'students':studentOptions}#, 'temp1':venueOptions1}
    c.update(csrf(request))
    return render_to_response('search_form.html', c,context_instance=RequestContext(request))
    
