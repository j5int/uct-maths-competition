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
from django.db import connection
from django.core import exceptions 
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

import confirmation

# def auth(request):
#   if not request.user.is_authenticated():
#     print "not logged in"
#     return HttpResponseRedirect('/accounts/login')

def index(request):
	return render_to_response('index.html', {})


@login_required
def profile(request):
  # auth(request)
  return render_to_response('profile.html',{})


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
    invigilator_range = range(10-len(invigilator_list))

    entries_per_grade = {} #Dictionary with grade:range(...)
    for grade in range(8,13):
        entries_per_grade[grade] = range(5-len(individual_list[grade]))


    if request.method == 'POST':  # If the form has been submitted...

        form = (request.POST) # A form bound to the POST data

        #Register a single responsible teacher (assigned to that school)
        rtschool = assigned_school #School.objects.get(pk=int(form.getlist('school','')[0]))
        rtfirstname = form.getlist('rt_firstname','')[0]
        rtsurname = form.getlist('rt_surname','')[0]
        rtphone_primary = form.getlist('rt_phone_primary','')[0]
        rtphone_alt = form.getlist('rt_phone_alt','')[0]
        rtemail = form.getlist('rt_email','')[0]
        rtregistered_by =  User.objects.get(pk=int(form.getlist('rt_registered_by','')[0]))
        query = ResponsibleTeacher(firstname = rtfirstname , surname = rtsurname,
                                  school = rtschool, registered_by= rtregistered_by)
        query.save()
        query.reference=query.id
        query.save()

        #Registering per grade
        for grade in range (8,13):
              #Registering the different pairs
              #Information is set to null, only school name is given and reference
              #Reference if the ID of the first person in the pair
              for p in range(int(form.getlist("pairs",'')[grade-8])):
                    firstname = ''
                    surname = ''
                    language = form.getlist('language','')[0]
                    reference = 1234
                    school = assigned_school
                  # sex = ''
                    registered_by =  User.objects.get(pk=int(form.getlist('registered_by','')[p]))
                    paired = True 
                    query = SchoolStudent(firstname = firstname , surname = surname, language = language,reference = reference,
                            school = school, grade = grade , registered_by= registered_by, paired = paired)
                    query.save()
                    query.reference=query.id
                    query.save()
                    query1 = SchoolStudent(firstname = firstname , surname = surname, language = language,reference = query.id,
                            school = school, grade = grade , registered_by= registered_by, paired = paired)
                    query1.save()

        #Registering students, maximum number of students 25
        #Returns an error if information entered incorrectly         
        try:
            for i in range (25-len(student_list)):
                if form.getlist('firstname','')[i] == u'': continue
                firstname = form.getlist('firstname','')[i]
                surname = form.getlist('surname','')[i]
                language = form.getlist('language','')[0]
                reference = 1234
                school = assigned_school
                grade = form.getlist('grade','')[i]
             #   sex = form.getlist('sex','')[i]
                registered_by =  User.objects.get(pk=int(form.getlist('registered_by','')[i]))
                paired = False 
                query = SchoolStudent(firstname = firstname , surname = surname, language = language,reference = reference,
                        school = school, grade = grade , registered_by= registered_by, paired = paired)

                query.save()
                query.reference=query.id
                query.save()

            for j in range(10-len(invigilator_list)):
                if form.getlist('inv_firstname','')[j] == u'':
                    ierror = "Invigilator information incomplete"
                else:
                    school = assigned_school
                    ifirstname = form.getlist('inv_firstname','')[j]
                    isurname = form.getlist('inv_surname','')[j]
                    iphone_primary = form.getlist('inv_phone_primary','')[j]
                    iphone_alt = form.getlist('inv_phone_alt','')[j]
                    iemail = form.getlist('inv_email','')[j]
                    iregistered_by =  User.objects.get(pk=int(form.getlist('inv_registered_by','')[j]))
                    
                    query = Invigilator(school = school, firstname = ifirstname,surname = isurname,
                                       phone_primary = iphone_primary , phone_alt = iphone_alt, email = iemail, registered_by= iregistered_by)
                    query.save()

            #send_mail command generates Exception ('Connection refused') if used on local database (pgadmin3)
            #send_mail('Save successful', 'Here is the message.', 'support@sjsoft.com',['hayleym@sjsoft.com'], fail_silently=False)
            
            if 'save_form' in request.POST: #Just save the form and commit to database, refresh page with changes
                return HttpResponseRedirect('newstudents.html')
            elif 'submit_form' in request.POST: #Send confirmation email and continue
                confirmation.send_confirmation(request, assigned_school)
                return render_to_response('submitted.html', {'type':'Student'}) # Redirect after POST
            else:
                print 'This should not happen'

        except Exception as e:
              error = "%s: Incorrect information inserted into fields. Please insert correct information" % e
    else:
        form = StudentForm() # An unbound form

    c = {'type':'Students',
        'schooln':assigned_school,
        #'schools':schoolOptions,
        'student_list':individual_list,
        'entries_per_grade':entries_per_grade,
        'invigilator_list': invigilator_list,
        'pairs_per_grade':range(0,6), 
        'grades':range(8,13), 
        'error':error,
        'invigilator_range':invigilator_range, 
        'igrades':range(8,13),
        'ierror':error} # Modified ticked#11005

    c.update(csrf(request))
    return render_to_response('newstudents.html', c, context_instance=RequestContext(request))


def processGrade(student_list): #FIXME: Should this be in view.py?
    """ Helper function for sorting students into grades """
    pair_list = { 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0} ###Not used yet
    individual_list = { 8 : [] , 9 :  [] , 10 :  [] , 11 : [] , 12 : [] }

    try:
        for student in student_list:
            if student.paired: # Better pair condition logic for this!
                pair_list[student.grade]+=1
                pass
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
    already_assigned = False
    school_assignment = ''
    if request.method == 'POST':  # If the form has been submitted...

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
            already_assigned = True 

    schoolOptions = School.objects.all()
    c = {'schools':schoolOptions, 'already_assigned' : already_assigned, 'assigned_to':school_assignment,'user':request.user,'error':error,'ierror':error} 
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
              firstname = form.getlist('firstname','')[i]
              surname = form.getlist('surname','')[i]
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


#******************************************  
