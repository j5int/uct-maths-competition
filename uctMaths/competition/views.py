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

# def auth(request):
#   if not request.user.is_authenticated():
#     print "not logged in"
#     return HttpResponseRedirect('/accounts/login')

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
        pass

    closingdate_blurb='Please note that entries for this year\'s UCT Mathematics Competition strictly close on ' + compadmin.closingDate() + '.'
        #return HttpResponseRedirect('../register/school_select/school_select.html')
    return render_to_response('profile.html',{'school_blurb':school_blurb,'closingdate_blurb':closingdate_blurb})


# submitted thingszz
@login_required
def submitted(request, c):
  return render_to_response('submitted.html', c)

#********************************************
# View Students
#Can view a list of students registered by current user 
#User can also delete the entire list or can edit individual students
@login_required
def students(request):
    username = request.user #current user

    # CASE: When the admin reassigns a school, the new controller should
    #       be able to remove those students. ie. therefore filter by 
    #       school instead of registered_by
    try:
        #Attempt to find user's chosen school
        assigned_school = School.objects.get(assigned_to=request.user)
    except exceptions.ObjectDoesNotExist:
        # No school is associated with this user! Redirect to the select_schools page
        return HttpResponseRedirect('../register/school_select/school_select.html')

    students = SchoolStudent.objects.filter(school = assigned_school)
    #If the user decides to delete the list. Only deletes invigilators registered by the current user
    if request.method=='POST':# 
        form = (request.POST) # A form bound to the POST data

        for s in students: # Find the button that was pressed - (tied to invigilator ID)
            str_check = 'del_student'+str(s.id)

            if str_check in request.POST:
                if s.paired: #pair logic. Remove both entries
                    s_grade = s.grade
                    s.delete()
                    for student in students:
                        if student.paired and student.id != None and student.grade == s_grade:
                            student.delete()
                            break
                else:
                    s.delete() #Single user logic
                break

        return HttpResponseRedirect('students.html') ##Once the response has been completed, refresh the page

    c = {'students':students} #Sends back list of invigilators and grade options
    c.update(csrf(request))
    return render_to_response('students.html', c,context_instance=RequestContext(request))

#*******************************************
# View Schools
#View the list of schools registered by current user
#Can either delete the whole list or edit individual schools
@login_required
def schools(request):
    username = request.user #current user
    schoolOptions = School.objects.filter(registered_by = username)
    
    #If the user decides to delete all the schools. Deletes only schools registered by that user
    if request.method=='POST' and 'delete' in request.POST:
        form = (request.POST) # A form bound to the POST data
        for i in range (schoolOptions.count()): #RANGE!!!!!!!!
          schoolID = form.getlist ('schoolID',"")[i]
          
          #SQL to DELETE schools
          cursor = connection.cursor()
          cursor.execute("DELETE FROM competition_school WHERE id=%s", [schoolID])
          row = cursor.fetchone()

          #Code below didnt work, for some unknown reason, therefore we used the above SQL to DELETE
          # print "id ", schoolID
          # temp = School.objects.get(id = schoolID)
          # print temp
          # temp.delete()
          # School.objects.get(id = schoolID).delete()
          #   print 'iteration:',i,School.objects.get(id=i+1), type(form.getlist('schoolID','')[0])
          #   schoolID = form.getlist('schoolID','')[i]
          #   schoolUpdate = School.objects.get(id = schoolID)
          #   schoolUpdate.delete()

    #If the user decides to edit schools. Edits can only be made to certain fields
    elif request.method=='POST' and 'submit' in request.POST:
        form = (request.POST) # A form bound to the POST data
        for i in range (schoolOptions.count()):
          schoolID = form.getlist('schoolID','')[i]
          schoolUpdate = School.objects.get(id = schoolID)
          schoolUpdate.name = form.getlist('name','')[i]
          schoolUpdate.address = form.getlist('address','')[i]
          schoolUpdate.language = form.getlist('language','')[i]
          schoolUpdate.phone = form.getlist('phone','')[i]
          schoolUpdate.email = form.getlist('email','')[i]
          schoolUpdate.contact = form.getlist('contact','')[i]
          schoolUpdate.fax = form.getlist('fax','')[i]
          schoolUpdate.save()
          
    c = {'schools':schoolOptions} #Sends back list of schools registered by that person
    c.update(csrf(request))
    return render_to_response('schools.html', c, context_instance=RequestContext(request))

#***************************************************
# View Invigilators
#Can view a list of invigilators which the current user has registered
#Current user can also delete the list or edit the invigilators
@login_required
def invigilators(request):
    username = request.user #current user

    # CASE: When the admin reassigns a school, the new controller should
    #       be able to remove those students. ie. therefore filter by 
    #       school instead of registered_by
    try:
        #Attempt to find user's chosen school
        assigned_school = School.objects.get(assigned_to=request.user)
    except exceptions.ObjectDoesNotExist:
        # No school is associated with this user! Redirect to the select_schools page
        return HttpResponseRedirect('../register/school_select/school_select.html')

    invigilators = Invigilator.objects.filter(school = assigned_school)

    #If the user decides to delete the list. Only deletes invigilators registered by the current user
    if request.method=='POST':# 
        form = (request.POST) # A form bound to the POST data

        for i in invigilators: # Find the button that was pressed - (tied to invigilator ID)
            str_check = 'del_invig'+str(i.id)

            if str_check in request.POST:
                i.delete() #The invigilator is deleted from records

        return HttpResponseRedirect('invigilators.html') ##Once the response has been completed, refresh the page

    c = {'invigilators':invigilators} #Sends back list of invigilators and grade options
    c.update(csrf(request))
    return render_to_response('invigilators.html', c,context_instance=RequestContext(request))

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
    individual_list, pair_list = processGrade(student_list) #processGrade is defined below this method
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
    individual_list, pair_list = processGrade(student_list) #processGrade is defined below this method
    invigilator_list = Invigilator.objects.filter(school = assigned_school)
    responsible_teacher = ResponsibleTeacher.objects.filter(school = assigned_school)

    #if responsible_teacher:
     #   return HttpResponseRedirect('../entry_review/entry_review.html')

    entries_per_grade = {} #Dictionary with grade:range(...)
    pairs_per_grade = {}
    for grade in range(8,13):
        entries_per_grade[grade] = range(5-len(individual_list[grade]))
        #Place the "Previously Selected" number of pairs at the top of the list (So it appears as a default)
        pairs_per_grade[grade] = [pair_list[grade]/2]
        pairs_per_grade[grade].extend([i for i in range(0,6) if i != pair_list[grade]/2])

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
                    reference = '%3s%2s%2s'%(str(school.id).zfill(3),str(grade).zfill(2),str(10+p).zfill(2))
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
            for i in range (25):
                if form.getlist('firstname','')[i] == u'': continue
                firstname = form.getlist('firstname','')[i].capitalize()
                surname = form.getlist('surname','')[i].capitalize()
                language = form.getlist('language','')[0]
                school = assigned_school
                grade = form.getlist('grade','')[i]
                reference = '%3s%2s%2s'%(str(school.id).zfill(3),str(grade).zfill(2),str(i%5).zfill(2))
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


def processGrade(student_list): #FIXME: Should this be in view.py?
    """ Helper function for sorting students into grades """
    pair_list = { 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0}
    individual_list = { 8 : [] , 9 :  [] , 10 :  [] , 11 : [] , 12 : [] }

    try:
        for student in student_list:
            if student.paired: # Better pair condition logic for this!
                pair_list[student.grade]+=1
            else: 
                individual_list[student.grade].append(student)
    except IndexError:
        print 'Index Error'
    return individual_list, pair_list


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
            inv_req_message = 'This profile is already bound to ' + assigned_school.name + '. Please proceed with student registration for the UCT Mathematics Competition by selecting "Registration Form." If you have selected the incorrect school, please contact ' + compadmin.admin_emailaddress + '.'
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
                inv_req_message = 'This school has already been assigned to another user. If you believe this to be an error, please contact ' + compadmin.admin_emailaddress + '.'

    schoolOptions = School.objects.all()
    c = {'schools':schoolOptions, 'invalid_request' : invalid_request, 'inv_req_message' : inv_req_message, 'user':request.user,'error':error,'ierror':error} 
    c.update(csrf(request))
    return render_to_response('school_select.html', c, context_instance=RequestContext(request))

#*****************************************
#Register Schools
#Registers one school at a time
@login_required
def newschools (request):
  error = " "
  if request.method == 'POST': # If the form has been submitted...
        form = (request.POST) # A form bound to the POST data
        
        #Registers school, returns an error if information is entered incorrectly
        try:
          for i in range (1):
              if form.getlist('name','')[i] == u'': continue
              name = form.getlist('name','')[i]
              key = 123
              language = form.getlist('language','')[i]
              address = form.getlist('address','')[i]
              phone = form.getlist('phone','')[i]
              fax = form.getlist('fax','')[i]
              contact = form.getlist('contact','')[i]
              email = form.getlist('email','')[i]
              #registered_by =  User.objects.get(pk=int(form.getlist('registered_by','')[i]))

              query = School(name = name ,key = key ,  language = language  ,
                  address = address, phone = phone , fax = fax, contact = contact , email = email, registered_by= registered_by)
              query.save()
              query.key=query.id
              query.save()

          return render_to_response('submitted.html', {'type':'School'}) # Redirect after POST
        except Exception as e:
              error = "%s Incorrect information inserted into fields. Please insert correct information" % e
  else:
        form = SchoolForm() # An unbound form

  c = {'type':'Schools', 'range':range(1), 'error':error}
  c.update(csrf(request))

  return render_to_response('newschools.html', c,context_instance=RequestContext(request))


#******************************************
#Register Invigilators
#Register maximum of 4 invigilators at a time
@login_required
def newinvigilators (request):
  error = " "
  if request.method == 'POST': # If the form has been submitted...
        form = (request.POST) # A form bound to the POST data

        #Returns error if information entered incorrectly
        try:
          for i in range (4):
              if form.getlist('firstname','')[i] == u'': continue
              firstname = form.getlist('firstname','')[i].capitalize()
              surname = form.getlist('surname','')[i].capitalize()
              phone_primary = form.getlist('phone_primary','')[i]
              phone_alt = form.getlist('phone_alt','')[i]
              email = form.getlist('email','')[i]
              registered_by =  User.objects.get(pk=int(form.getlist('registered_by','')[i]))

              query = Invigilator(school = school , firstname = ifirstname,surname = isurname,
                                  phone_primary = iphone_primary , phone_alt = iphone_alt, email = iemail,
                                 registered_by= iregistered_by)

              query.save()

          return render_to_response('submitted.html', {'type':'Invigilator'}) # Redirect after POST
        except Exception as e:
              print e
              error = "%s: Incorrect information inserted into fields. Please insert correct information" 
  else:
        form = InvigilatorForm() # An unbound form
  schoolOptions = School.objects.all()

  c = {'schools':schoolOptions, 'range':range(10), 'grades':range(8,13), 'error':error} #******ADD RANGE

  c.update(csrf(request))
  return render_to_response('newinvigilators.html', c,context_instance=RequestContext(request))

