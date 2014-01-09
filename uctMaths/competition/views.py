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
from competition.forms import StudentForm, SchoolForm, InvigilatorForm, ResponsibleTeacherForm
from competition.models import SchoolStudent, School, Invigilator, Venue, ResponsibleTeacher
from django.contrib.auth.models import User
#from django.contrib.contenttypes import *
from django.db import connection
from django.core import exceptions 
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

import confirmation
import compadmin

def auth(request):
   if not request.user.is_authenticated():
     print "not logged in"
     return HttpResponseRedirect('/accounts/login')

def index(request):
    return render_to_response('index.html', {})


@login_required
def profile(request):
    # auth(request)
    school_blurb = 'This profile is currently '
    try:
        #Attempt to find user's chosen school
        assigned_school = School.objects.get(assigned_to=request.user)
        school_blurb += 'associated with ' + str(assigned_school.name) + ' and has sole access and responsibility for its UCT Mathematics competition entry forms. Navigate to \'Entry Form\' from the side-bar to review or edit your entry.'
    except exceptions.ObjectDoesNotExist:
        # No school is associated with this user! Redirect to the select_schools page
        school_blurb += 'not associated with any school. Navigate to \'Entry Form\' on the side-bar to continue.'
    
    admin_contact = compadmin.admin_emailaddress()
    closingdate_blurb='Please note that entries for this year\'s UCT Mathematics Competition strictly close on ' + compadmin.closingDate() + '.'
        #return HttpResponseRedirect('../register/school_select/school_select.html')
    return render_to_response('profile.html',{'school_blurb':school_blurb,'closingdate_blurb':closingdate_blurb, 'admin_contact':admin_contact})


# submitted thingszz
@login_required
def submitted(request, c):
  c.update(csrf(request))
  return render_to_response('submitted.html', c)


#*****************************************
# Entry Review
@login_required
def entry_review(request):
    error = " "
    try:
        #Attempt to find user's chosen school
        assigned_school = School.objects.get(assigned_to=request.user)
    except exceptions.ObjectDoesNotExist:
        # No school is associated with this user! Redirect to the select_schools page
        return HttpResponseRedirect('../school_select/school_select.html')

    #NOTE: School.objects.get(pk=int(form.getlist('school','')[0])) was previously used to get school from drop-down menu

    #Required that school form is pre-fetched to populate form
    student_list = SchoolStudent.objects.filter(school = assigned_school)
    individual_list, pair_list = compadmin.processGrade(student_list) #processGrade is defined below this method
    invigilator_list = Invigilator.objects.filter(school = assigned_school)
    responsible_teacher = ResponsibleTeacher.objects.filter(school = assigned_school)

    for p in range(8,13):
        pair_list[p] = pair_list[p]/2

    if not responsible_teacher:
        return HttpResponseRedirect('../students/newstudents.html')

    c = {'type':'Students',
        'schooln':assigned_school,
        'responsible_teacher':responsible_teacher[0],
        'student_list':individual_list,
        'pair_list':pair_list,
        'entries_open':compadmin.isOpen(),
        'invigilator_list': invigilator_list,
        'grades':range(8,13), 
        'error':error,
        'invigilator_range':range(10-len(invigilator_list)), 
        'igrades':range(8,13),
        'ierror':error}

    if request.method == 'POST' and 'edit_entry' in request.POST and compadmin.isOpen():  # If the form has been submitted.
        return HttpResponseRedirect('../students/newstudents.html')
    if request.method == 'POST' and 'resend_confirmation' in request.POST:  # If the form has been submitted.
        confirmation.send_confirmation(request, assigned_school, cc_admin=False) #Needs to only be bound to this user's email address
        return render_to_response('submitted.html')

    c.update(csrf(request))
    return render_to_response('entry_review.html', c, context_instance=RequestContext(request))


#*****************************************
# Register Students   
#User can register 5 students per grade and 5 pairs per grade 
@login_required
def newstudents(request):
    error = " "
    try:
        #Attempt to find user's chosen school
        assigned_school = School.objects.get(assigned_to=request.user)
    except exceptions.ObjectDoesNotExist:
        # No school is associated with this user! Redirect to the select_schools page
        return HttpResponseRedirect('../school_select/school_select.html')

    #NOTE: School.objects.get(pk=int(form.getlist('school','')[0])) was previously used to get school from drop-down menu

    #Required that school form is pre-fetched to populate form
    student_list = SchoolStudent.objects.filter(school = assigned_school)
    individual_list, pair_list = compadmin.processGrade(student_list) #processGrade is defined below this method
    invigilator_list = Invigilator.objects.filter(school = assigned_school)
    responsible_teacher = ResponsibleTeacher.objects.filter(school = assigned_school)

    #if responsible_teacher:
     #   return HttpResponseRedirect('../entry_review/entry_review.html')

    entries_per_grade = {} #Dictionary with grade:range(...)
    pairs_per_grade = {}
    for grade in range(8,13):
        entries_per_grade[grade] = range(compadmin.admin_number_of_individuals()-len(individual_list[grade]))
        #Place the "Previously Selected" number of pairs at the top of the list (So it appears as a default)
        pairs_per_grade[grade] = [pair_list[grade]/2]
        pairs_per_grade[grade].extend([i for i in range(0,compadmin.admin_number_of_pairs()+1) if i != pair_list[grade]/2])

    if request.method == 'POST':  # If the form has been submitted...

        form = (request.POST) # A form bound to the POST data

        #Delete all previously stored information
        for rt in responsible_teacher:
            rt.delete()
        for student in student_list:
            student.delete()
        for invigilator in invigilator_list:
            invigilator.delete()


        #Register a single responsible teacher (assigned to that school)
        rtschool = assigned_school #School.objects.get(pk=int(form.getlist('school','')[0]))
        rtfirstname = form.getlist('rt_firstname','')[0].capitalize()
        rtsurname = form.getlist('rt_surname','')[0].capitalize()
        rtphone_primary = form.getlist('rt_phone_primary','')[0]
        rtphone_alt = form.getlist('rt_phone_alt','')[0]
        rtemail = form.getlist('rt_email','')[0]
        #rtregistered_by =  User.objects.get(pk=int(form.getlist('rt_registered_by','')[0]))
        query = ResponsibleTeacher(firstname = rtfirstname , surname = rtsurname, phone_primary = rtphone_primary, 
                                  phone_alt = rtphone_alt, school = rtschool,
                                  email = rtemail)
        query.save()
        query.reference=query.id
        query.save()

        #Registering per grade
        for grade in range (8,13):
              #Registering the different pairs
              #Information is set to null, only school name is given and reference
              #Reference if the ID of the first person in the pair
              for p in range(int(form.getlist("pairs",'')[grade-8])):
                    firstname = 'Pair/Paar'
                    surname = str(grade)+chr(65+p)
                    language = form.getlist('language','')[0]
                    school = assigned_school
                    reference = '%3s%2s%2s'%(str(school.id).zfill(3),str(grade).zfill(2),str(11+p).zfill(2))
                    #registered_by =  User.objects.get(pk=int(form.getlist('registered_by','')[p]))
                    paired = True 
                    #Save first entry for pair
                    query = SchoolStudent(firstname = firstname , surname = surname, language = language,reference = reference,
                            school = school, grade = grade , paired = paired)
                    query.save()
                    #Save second entry for pair
                    query1 = SchoolStudent(firstname = firstname , surname = surname, language = language, reference = reference, 
                            school = school, grade=grade,
                            paired = paired)
                    query1.save()

        #Registering students, maximum number of students 25
        #Returns an error if information entered incorrectly         
        try:
            for i in range (5*compadmin.admin_number_of_individuals()):
                if form.getlist('firstname','')[i] == u'': continue
                firstname = form.getlist('firstname','')[i].capitalize()
                surname = form.getlist('surname','')[i].capitalize()
                language = form.getlist('language','')[0]
                school = assigned_school
                grade = form.getlist('grade','')[i]
                reference = '%3s%2s%2s'%(str(school.id).zfill(3),str(grade).zfill(2),str(i%5+1).zfill(2))
                #registered_by =  User.objects.get(pk=int(form.getlist('registered_by','')[i]))
                paired = False 

                query = SchoolStudent(firstname = firstname , surname = surname, language = language,reference = reference,
                        school = school, grade = grade , paired = paired)

                query.save()

            for j in range(10):
                if form.getlist('inv_firstname','')[j] == u'':
                    ierror = "Invigilator information incomplete"
                else:
                    school = assigned_school
                    ifirstname = form.getlist('inv_firstname','')[j].capitalize()
                    isurname = form.getlist('inv_surname','')[j].capitalize()
                    iphone_primary = form.getlist('inv_phone_primary','')[j]
                    iphone_alt = form.getlist('inv_phone_alt','')[j]
                    iemail = form.getlist('inv_email','')[j]
                    #iregistered_by =  User.objects.get(pk=int(form.getlist('inv_registered_by','')[j]))

                    query = Invigilator(school = school, firstname = ifirstname,surname = isurname,
                                       phone_primary = iphone_primary , phone_alt = iphone_alt, email = iemail)
                    query.save()

            if 'submit_form' in request.POST: #Send confirmation email and continue
                confirmation.send_confirmation(request, assigned_school,cc_admin=True)
                return render_to_response('submitted.html')
            else:
                print 'This should not happen'

        except Exception as e:
              error = "%s: Incorrect information inserted into fields. Please insert correct information" % e
    else:
        form = StudentForm() # An unbound form

    if responsible_teacher:
        responsible_teacher = responsible_teacher[0]
    else:
        #If not null, then the form has been filled out.
        #Therefore - redirect to entry_review page
        pass #HttpResponseRedirect('../entry_review.html')

    c = {'type':'Students',
        'schooln':assigned_school,
        #'schools':schoolOptions,
        'responsible_teacher':responsible_teacher,
        'student_list':individual_list,
        'pairs_per_grade':pairs_per_grade,
        'pair_range':pairs_per_grade,
        'entries_per_grade':entries_per_grade,
        'invigilator_list': invigilator_list,
        'entries_open':compadmin.isOpen(),
        'grades':range(8,13), 
        'error':error,
        'invigilator_range':range(10-len(invigilator_list)), 
        'igrades':range(8,13),
        'ierror':error}

    c.update(csrf(request))
    return render_to_response('newstudents.html', c, context_instance=RequestContext(request))

#*****************************************
# School select.
# Should be redirected here (from newstudents) if there is no school associated with the particular user name
@login_required
def school_select(request):
    error = " "
    invalid_request = False
    inv_req_message = ''
    school_assignment = ''
    if request.method == 'POST':  # If the form has been submitted...

        try:
        #Attempt to find user's chosen school
            assigned_school = School.objects.get(assigned_to=request.user)
            inv_req_message = 'This profile is already bound to ' + assigned_school.name + '. Please proceed with student registration for the UCT Mathematics Competition by selecting "Entry form." If you have selected the incorrect school, please contact ' + compadmin.admin_emailaddress() + '.'
            invalid_request=True
        except exceptions.ObjectDoesNotExist:
        # No school is associated with this user! Continue
            form = (request.POST) # A form bound to the POST data
            school_selected = School.objects.get(pk=int(form.getlist('school','')[0]))
            school_assignment = School.objects.get(name=school_selected).assigned_to
            
            if school_assignment == None: #An unassigned school is assigned to user.
                #TODO: Add a "Please be sure" message just telling them what they're doing.
                #schoolAssmtUpdate = School.objects.get(id = school_assignment)
                school_selected.assigned_to = request.user
                school_selected.save()
                #School.objects.set(name=school_selected).assign_to(request.user)
                return HttpResponseRedirect('../students/newstudents.html')

            elif school_assignment == request.user: #This should not happen
                return HttpResponseRedirect('../students/newstudents.html')
            else:
                invalid_request = True 
                inv_req_message = 'This school has already been assigned to another user. If you believe this to be an error, please contact ' + compadmin.admin_emailaddress() + '.'

    schoolOptions = School.objects.all()
    c = {'schools':schoolOptions, 'invalid_request' : invalid_request, 'inv_req_message' : inv_req_message, 'user':request.user,'error':error,'ierror':error, 'admin_emailaddress':compadmin.admin_emailaddress()} 
    c.update(csrf(request))
    return render_to_response('school_select.html', c, context_instance=RequestContext(request))
