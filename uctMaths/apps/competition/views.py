from __future__ import unicode_literals

import pytz
from django.http import HttpResponse
from django.shortcuts import render as render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators import csrf
from django.template.context_processors import csrf
from .forms import StudentForm
from .models import SchoolStudent, School, Invigilator, ResponsibleTeacher
from django.core import exceptions
from django.contrib.auth.decorators import login_required

from . import confirmation
from . import compadmin

from datetime import datetime,time

def auth(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login')



@login_required
def printer_entry_result(request, school_list=None):
    """ Generate the printer entry template for each school (in the optional queryset or the one bound to the user issuing the request)."""
    #had to easy_install html5lib pisa
    #Create the HttpResponse object with the appropriate PDF headers.
    temp_school_list = []
    if not school_list: #If not called by the admin
        try:
            #Attempt to find user's chosen school
            temp_school_list.append(School.objects.get(assigned_to=request.user))
        except exceptions.ObjectDoesNotExist:
            # No school is associated with this user! Redirect to the select_schools page
            return HttpResponseRedirect('../school_select/')
    else:
        temp_school_list = [school for school in school_list]

    html = '' #Will hold rendered templates
    return compadmin.generate_school_confirmation(request, temp_school_list)

#Method bound to printer_entry.html request
@login_required
def printer_entry(request, queryset=None):
    """ Method bound to printer_entry.html """
    result = printer_entry_result(request, queryset)
    response = HttpResponse(result.getvalue())
    response["Content-Type"] = "application/pdf"
    return response

@login_required
def profile(request):
    # auth(request)
    assigned_school=None
    school_blurb = 'Welcome. This profile is currently '
    try:
        #Attempt to find user's chosen school
        assigned_school = School.objects.get(assigned_to=request.user)
        school_blurb += 'associated with ' + str(assigned_school.name) + ' and has sole access and responsibility for its UCT Mathematics Competition entry forms. Please navigate to \'Entry Form\' on the side-bar to review or edit your entry.'
    except exceptions.ObjectDoesNotExist:
        # No school is associated with this user! Redirect to the select_schools page
        school_blurb += 'not associated with any school. Navigate to \'Entry Form\' to select your school.'
    admin_contact = compadmin.admin_emailaddress()

    if compadmin.isOpen():
        closingdate_blurb='Please note that online entries for this year\'s UCT Mathematics Competition strictly close on ' + compadmin.closingDate() + '.'
    elif not request.user.is_staff:

        closingdate_blurb=(f'School submissions for this year\'s UCT Mathematics Competition are closed. '
                           'If you have previously submitted an entry, please navigate to \'Entry form\' if you '
                           f'wish to view your entry. The competition registration window is set for {compadmin.openingDate()} -> {compadmin.closingDate()}')
    else:
        closingdate_blurb='Online entries are closed but you may still create and modify entries because you have admin rights.'
    show_results_download = False
    if assigned_school:
        show_results_download = has_results(request, assigned_school) and after_pg(request)
    show_answer_sheets_download = False

    if assigned_school and ResponsibleTeacher.objects.filter(
            school=assigned_school.id).count() > 0 and compadmin.can_download_answer_sheets():
        show_answer_sheets_download = compadmin.school_students_venue_assigned(assigned_school)

    return render_to_response(request, 'profile.html',
                              {'school_blurb': school_blurb,
                               'closingdate_blurb': closingdate_blurb,
                               'admin_contact': admin_contact,
                               'show_results_download': show_results_download,
                               'show_answer_sheets_download': show_answer_sheets_download,
                               'admin': True if request.user.is_staff else False})


# submitted thingszz
@login_required
def submitted(request):

    school_summary_blurb = 'Thank you for using the UCT Mathematics Competition online Registration Portal. You have successfully registered:'
    
    try: #Try get the student list for the school assigned to the requesting user
        school_asmt = School.objects.get(assigned_to=request.user)
        student_list = SchoolStudent.objects.all().filter(school=school_asmt)
    except exceptions.ObjectDoesNotExist:
        return HttpResponseRedirect('../school_select/')
    except Exception:
        school_summary_blurb = 'An error has occured.' #This could occur if a user has become associated with > 1 school.
    
    grade_summary = compadmin.gradeBucket(student_list) #Bin into categories (Pairing, grade)
    school_summary_info = [] #Entry for each grade
    count_individuals = 0
    count_pairs = 0
    
    for i in range(8,13):
        grade_summary_text = 'Grade %d: %d individuals' % (i, len(grade_summary[i,False,'ALL']))
        if compadmin.admin_number_of_pairs() > 0:
            grade_summary_text += " and %d pairs" % (len(grade_summary[i,True,'ALL']))
        school_summary_info.append(grade_summary_text)
        count_pairs = count_pairs + len(grade_summary[i,True,'ALL'])
        count_individuals = count_individuals + len(grade_summary[i,False,'ALL'])
        
    school_summary_statistics = 'You have successfully registered %d students' % (count_pairs*2+count_individuals)
    
    if compadmin.admin_number_of_pairs() > 0:
        school_summary_statistics += ' (%d individuals and %d pairs).' % (count_individuals, count_pairs)

    c = {
        'school_summary_blurb':school_summary_blurb,
        'school_summary_info':school_summary_info,
        'school_summary_statistics':school_summary_statistics,
        }

    c.update(csrf(request))
    return render_to_response(request, 'submitted.html', c)


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
        return HttpResponseRedirect('../school_select/')

    #NOTE: School.objects.get(pk=int(form.getlist('school','')[0])) was previously used to get school from drop-down menu

    #Required that school form is pre-fetched to populate form
    student_list = SchoolStudent.objects.filter(school = assigned_school)
    individual_list, pair_list = compadmin.processGrade(student_list) #processGrade is defined below this method
    invigilator_list = Invigilator.objects.filter(school = assigned_school)
    responsible_teacher = ResponsibleTeacher.objects.filter(school = assigned_school).filter(is_primary = True)
    alt_responsible_teacher = ResponsibleTeacher.objects.filter(school = assigned_school).filter(is_primary = False)

    for p in range(8,13):
        pair_list[p] = pair_list[p]

    if not (responsible_teacher or alt_responsible_teacher):
        return HttpResponseRedirect('../students/')
    else:
        assigned_school.entered=1 #The school has made an entry
        assigned_school.save()
    
    if responsible_teacher:
        responsible_teacher = responsible_teacher[0]
    else:
        responsible_teacher = None

    if alt_responsible_teacher:
        alt_responsible_teacher = alt_responsible_teacher[0]
    else:
        alt_responsible_teacher = None
        
    c = {'type':'Students',
        'schooln':assigned_school,
        'responsible_teacher':responsible_teacher,
        'alt_responsible_teacher':alt_responsible_teacher,
        'student_list':individual_list,
        'pair_list':pair_list,
        'max_num_pairs': compadmin.admin_number_of_pairs(),
        'entries_open': compadmin.isOpen() or request.user.is_staff,
        'invigilator_list': invigilator_list,
        'grades':range(8,13), 
        'error':error,
        'invigilator_range':range(10-len(invigilator_list)), 
        'igrades':range(8,13),
        'ierror':error,
        "only_back":True,
        'invigilators': compadmin.competition_has_invigilator(),
        'address':assigned_school.address.replace(', ','\n'),
        'maxEntries': compadmin.get_max_entries()}

    if request.method == 'POST' and 'edit_entry' in request.POST and (compadmin.isOpen() or request.user.is_staff):  # If the form has been submitted.
        return HttpResponseRedirect('../students/')
    if request.method == 'POST' and 'resend_confirmation' in request.POST:  # If the form has been submitted.
        confirmation.send_confirmation(request, assigned_school, cc_admin=False) #Needs to only be bound to this user's email address
        return HttpResponseRedirect('../')

    c.update(csrf(request))
    return render_to_response(request, 'entry_review.html', c)


#*****************************************
# Register Students   
# Up to <competition.number_of_individuals> individuals and <competition.number_of_pairs> pairs per grade 
@login_required
def newstudents(request):
    error = " "
    try:
        #Attempt to find user's chosen school
        assigned_school = School.objects.get(assigned_to=request.user)
    except exceptions.ObjectDoesNotExist:
        # No school is associated with this user! Redirect to the select_schools page
        return HttpResponseRedirect('../school_select/')

    #NOTE: School.objects.get(pk=int(form.getlist('school','')[0])) was previously used to get school from drop-down menu

    #Required that school form is pre-fetched to populate form
    student_list = SchoolStudent.objects.filter(school = assigned_school)
    individual_list, pair_list = compadmin.processGrade(student_list) #processGrade is defined below this method
    invigilator_list = Invigilator.objects.filter(school = assigned_school)
    responsible_teacher = ResponsibleTeacher.objects.filter(school = assigned_school).filter(is_primary = True)
    alt_responsible_teacher = ResponsibleTeacher.objects.filter(school = assigned_school).filter(is_primary = False)

    editEntry = False
    language_selection_options = ['e', 'a', 'b']

    if (responsible_teacher or alt_responsible_teacher):
        editEntry = True
    
    if assigned_school and (responsible_teacher or alt_responsible_teacher):
        language_temp = assigned_school.language
        language_selection = [language_temp]
        language_selection.extend([c for c in language_selection_options if c != language_temp])
    else:
        language_selection = ['e', 'a', 'b']


    entries_per_grade = {} #Dictionary with grade:range(...)
    pairs_per_grade = {}
    for grade in range(8,13):
        entries_per_grade[grade] = range(compadmin.admin_number_of_individuals() - len(individual_list[grade]))
        #Place the "Previously Selected" number of pairs at the top of the list (So it appears as a default)
        pairs_per_grade[grade] = [pair_list[grade]]
        pairs_per_grade[grade].extend([i for i in range(0, compadmin.admin_number_of_pairs() + 1) if i != pair_list[grade]])

    if request.method == 'POST':  # If the form has been submitted...
        form = (request.POST) # A form bound to the POST data

        #Delete all previously stored information

        try:
            assigned_school.address ='%s, %s, %s' % (form.getlist('physical_address','')[0], form.getlist('code','')[0], form.getlist('city','')[0])
            assigned_school.language = form.getlist('language','')[0]
            assigned_school.phone = form.getlist('school_number','')[0]
            assigned_school.save()
                
            #Register a single responsible teacher (assigned to that school)
            rtschool = assigned_school #School.objects.get(pk=int(form.getlist('school','')[0]))
            rtfirstname = form.getlist('rt_firstname','')[0]
            rtsurname = form.getlist('rt_surname','')[0]
            rtphone_primary = form.getlist('rt_phone_primary','')[0].strip().replace(' ', '')
            rtphone_alt = form.getlist('rt_phone_alt','')[0].strip().replace(' ', '')
            rtphone_cell = form.getlist('rt_phone_cell','')[0].strip().replace(' ', '')
            rtemail_school = form.getlist('rt_email_school','')[0].strip().replace(' ', '')
            rtemail_personal = form.getlist('rt_email_personal','')[0].strip().replace(' ', '')

            #rtregistered_by =  User.objects.get(pk=int(form.getlist('rt_registered_by','')[0]))
            rt_query = ResponsibleTeacher(firstname = rtfirstname , surname = rtsurname, phone_primary = rtphone_primary,
                                        phone_alt = rtphone_alt, phone_cell=rtphone_cell, school = rtschool,
                                        email_school = rtemail_school, email_personal=rtemail_personal, is_primary = True)

            #Delete responsible teacher before saving the new one
            for rt in responsible_teacher:
                rt.delete()

            rt_query.save()
            rt_query.reference=rt_query.id
            rt_query.save()

            #Register an alternate responsible teacher
            artschool = assigned_school #School.objects.get(pk=int(form.getlist('school','')[0]))
            artfirstname = form.getlist('art_firstname','')[0]
            artsurname = form.getlist('art_surname','')[0]
            artphone_primary = form.getlist('art_phone_primary','')[0].strip().replace(' ', '')
            artphone_alt = form.getlist('art_phone_alt','')[0].strip().replace(' ', '')
            artphone_cell = form.getlist('art_phone_cell','')[0].strip().replace(' ', '')
            artemail_school = form.getlist('art_email_school','')[0].strip().replace(' ', '')
            artemail_personal = form.getlist('art_email_personal','')[0].strip().replace(' ', '')

            #rtregistered_by =  User.objects.get(pk=int(form.getlist('rt_registered_by','')[0]))
            art_query = ResponsibleTeacher(firstname = artfirstname , surname = artsurname, phone_primary = artphone_primary,
                                        phone_alt = artphone_alt, phone_cell=artphone_cell, school = artschool,
                                        email_school = artemail_school, email_personal=artemail_personal, is_primary = False)

            #Delete responsible teacher before saving the new one
            for art in alt_responsible_teacher:
                art.delete()

            art_query.save()
            art_query.reference=art_query.id
            art_query.save()

            num_pairs = 0
            #Registering per grade
            for grade in range (8,13):
                #Registering the different pairs
                #Information is set to null, only school name is given and reference
                #Reference if the ID of the first person in the pair

                if compadmin.admin_number_of_pairs() == 0:
                    break

                for p in range(int(form.getlist("pairs",'')[grade-8])):
                        firstname = 'Pair/Paar'
                        surname = str(grade)+chr(65 + p)   # Maps 0, 1, 2, 3... to A, B, C...
                        pair_number = 51 + p
                        language = form.getlist('language','')[0]
                        school = assigned_school
                        reference = '%3s%2s%2s' % (str(school.id).zfill(3), str(grade).zfill(2), str(pair_number).zfill(2))
                        paired = True
                        location = assigned_school.location

                        query = SchoolStudent(firstname=firstname , surname=surname, language=language, reference=reference,
                                    school=school, grade=grade, paired=paired, location=location)
                        query.save()
                        num_pairs += 1

            num_invigilators = 0
            #Add invigilator information
            for invigilator in invigilator_list:
                invigilator.delete()
            if compadmin.competition_has_invigilator():
                for j in range(10):
                    school = assigned_school
                    ifirstname = correctCapitals(form.getlist('inv_firstname', [])[j] or '')
                    isurname = correctCapitals(form.getlist('inv_surname', [])[j] or '')
                    iphone_primary = form.getlist('inv_phone_primary', [])[j] or ''
                    iphone_primary = iphone_primary.strip().replace(' ', '')
                    iphone_alt = form.getlist('inv_phone_alt', [])[j] or ''
                    iphone_alt = iphone_alt.strip().replace(' ', '')
                    iemail = form.getlist('inv_email', [])[j] or ''
                    iemail = iemail.strip().replace(' ', '')
                    inotes = form.getlist('inv_notes', [])[j] or ''
                    inotes = inotes.strip()
                    location = assigned_school.location

                    if not (ifirstname and isurname and iemail):
                        ierror = "Invigilator information incomplete"
                        continue

                    query = Invigilator(school=school, firstname=ifirstname, surname=isurname, location=location,
                                    phone_primary=iphone_primary, phone_alt=iphone_alt, email=iemail, notes=inotes)
                    query.save()
                    num_invigilators += 1

            num_individuals = 0
            #Registering students, maximum number of students 25
            #Returns an error if information entered incorrectly

            for student in student_list:
                student.delete()

            for i in range (5 * compadmin.admin_number_of_individuals()):
                if form.getlist('firstname','')[i] == u'': continue
                firstname =  correctCapitals(form.getlist('firstname','')[i])
                surname =  correctCapitals(form.getlist('surname','')[i])
                ind_nr = (i % compadmin.admin_number_of_individuals()) + 1
                language =  form.getlist('language','')[0]
                school = assigned_school
                grade = form.getlist('grade','')[i]
                reference = '%3s%2s%2s' % (str(school.id).zfill(3), str(grade).zfill(2), str(ind_nr).zfill(2))
                paired = False
                location = assigned_school.location

                query = SchoolStudent(firstname=firstname, surname=surname, language=language, reference=reference,
                            school=school, grade=grade, paired=paired, location=location)
                query.save()
                num_individuals += 1

            #Update data that is pre-fetched to populate the school form so no data is lossed upon failed form submission
            student_list = SchoolStudent.objects.filter(school = assigned_school)
            individual_list, pair_list = compadmin.processGrade(student_list)
            entries_per_grade = {}
            pairs_per_grade = {}
            for grade in range(8,13):
                entries_per_grade[grade] = range(compadmin.admin_number_of_individuals() - len(individual_list[grade]))
                pairs_per_grade[grade] = [pair_list[grade]]
                pairs_per_grade[grade].extend([i for i in range(0, compadmin.admin_number_of_pairs() + 1) if i != pair_list[grade]])

            if 'submit_form' in request.POST: #Send confirmation email and continue
                enoughInvigilators.checkEnoughInvigilators(num_invigilators, num_individuals, num_pairs)
                if enoughInvigilators.enoughInvigilators: #Only proceed with submission if enough invigilators are entered
                    assigned_school.entered=1 #The school has made an entry
                    assigned_school.save()
                    #The school has made an entry
                    try:
                        confirmation.send_confirmation(request, assigned_school, cc_admin=True)
                        return HttpResponseRedirect('../submitted/')
                    except Exception as e:
                        print(e)
                        return HttpResponseRedirect('../submitted/')
            else:
                print('This should not happen')

        except Exception as e:
            error = "%s: Incorrect information inserted into fields. Please insert correct information" % e
    else:
        form = StudentForm() # An unbound form

    if responsible_teacher:
        responsible_teacher = responsible_teacher[0]
    else:
        responsible_teacher = None
        #If not null, then the form has been filled out.
        #Therefore - redirect to entry_review page
        pass #HttpResponseRedirect('../entry_review.html')
    if alt_responsible_teacher:
        alt_responsible_teacher = alt_responsible_teacher[0]
    else:
        alt_responsible_teacher = None
    invigilators = compadmin.competition_has_invigilator()
    full = []
    if assigned_school.entered == 1:
        full = assigned_school.address.split(',')
    full += ['']*(3-len(full))
    address = full[0].strip()
    code = full[1].strip()
    city = full[2].strip()

    student_list = SchoolStudent.objects.filter(school = assigned_school)
    individual_list, pair_list = compadmin.processGrade(student_list) #processGrade is defined below this method
    entries_per_grade = {} #Dictionary with grade:range(...)
    for grade in range(8,13):
        entries_per_grade[grade] = range(compadmin.admin_number_of_individuals() - len(individual_list[grade]))

    c = {'type':'Students',
        'schooln':assigned_school,
        'language_options':language_selection,
        'responsible_teacher':responsible_teacher,
        'alt_responsible_teacher':alt_responsible_teacher,
        'student_list':individual_list,
        'pairs_per_grade':pairs_per_grade,
        'pair_range':pairs_per_grade,
        'max_num_pairs': compadmin.admin_number_of_pairs(),
        'entries_per_grade':entries_per_grade,
        'invigilator_list': invigilator_list,
        'enough_invigilators': enoughInvigilators.enoughInvigilators,
        'entries_open': compadmin.isOpen() or request.user.is_staff,
        'grades':range(8,13), 
        'error':error,
        'invigilator_range':range(10-len(invigilator_list)), 
        'igrades':range(8,13),
        'editEntry':editEntry,
        'ierror':error,
        'invigilators':invigilators,
        'address':address,
        'code':code,
        'city':city,
        'maxEntries': compadmin.get_max_entries()}

    c.update(csrf(request))
    #TODO Cancel button (Go back to 'Entry Review' - if possible)
    return render_to_response(request, 'newstudents.html', c)

class enoughInvigilators():
    enoughInvigilators=True
        
    def checkEnoughInvigilators(num_invigilators, num_individuals, num_pairs):
        """
        Sets enoughtInvigilators to false only when: 
        the competiton has invigilator AND
        there are less than two invigilators but maximum number of students entered.
        In this case there are not enough invigilators entered and user should be prompted to add more.
        """

        if not compadmin.competition_has_invigilator():
            enoughInvigilators.enoughInvigilators=True
            return
        
        if num_invigilators>=2 or not compadmin.competition_has_invigilator():
            enoughInvigilators.enoughInvigilators=True
            return

        if num_pairs<(5*compadmin.admin_number_of_pairs()):
            enoughInvigilators.enoughInvigilators=True
            return
            
        if num_individuals<(5*compadmin.admin_number_of_individuals()):
            enoughInvigilators.enoughInvigilators=True
            return

        enoughInvigilators.enoughInvigilators=False


def correctCapitals(input_name):
    
    #Return true if all cased characters in the string are uppercase and there is at least one cased character, false otherwise.
    if not input_name.isupper():
        return input_name # Return unaltered input if it is not all capitals
    else:
        words = input_name.split()
        output = []
        for wd in words:
            output.append(wd.capitalize())
            
        return ' '.join(output) #Otherwise return name as first-letter-capitalised

#*****************************************
# School select.
# Should be redirected here (from newstudents) if there is no school associated with the particular user name
@login_required
def school_select(request):
    error = " "
    invalid_request = False
    inv_req_message = ''
    school_assignment = ''

    if not (compadmin.isOpen() or request.user.is_staff):
        return HttpResponseRedirect('/accounts/profile')

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
                return HttpResponseRedirect('../students/')

            elif school_assignment == request.user: #This should not happen
                return HttpResponseRedirect('../students/')
            else:
                invalid_request = True 
                inv_req_message = 'This school has already been assigned to another user. If you believe this to be an error, please contact ' + compadmin.admin_emailaddress() + '.'

    schoolOptions = School.objects.all()
    c = {'schools':schoolOptions, 'invalid_request' : invalid_request, 'inv_req_message' : inv_req_message, 'user':request.user,'error':error,'ierror':error, 'admin_emailaddress': compadmin.admin_emailaddress()}
    c.update(csrf(request))
    return render_to_response(request, 'school_select.html', c)

@login_required
def school_results(request):
    assigned_school = School.objects.get(assigned_to=request.user)
    if has_results(request, assigned_school):
        report = ResponsibleTeacher.objects.filter(school = assigned_school).filter(is_primary=True)
        if report:
            report = report[0]
        report.report_downloaded = datetime.now(tz=pytz.timezone("Africa/Johannesburg"))
        report.save()
        return compadmin.print_school_reports(request, [assigned_school])
    return HttpResponse("Results will be available soon.")

@login_required
def after_pg(request):
    comp = compadmin.Competition.objects.all()
    pg_date = comp[0].prizegiving_date
    return (datetime.now().date() > pg_date or (datetime.now().date() == pg_date and datetime.now().time() > time(21,0,0)))

@login_required
def has_results(request, assigned_school = None):
    if ResponsibleTeacher.objects.filter(school = assigned_school).count()==0:
        return False
    student_list = SchoolStudent.objects.filter(school=assigned_school)
    return True if student_list else False

@login_required 
def answer_sheets(request, assigned_school = None):
    assigned_school = School.objects.get(assigned_to=request.user)
    rteachers = ResponsibleTeacher.objects.filter(school=assigned_school.id)
    if rteachers and compadmin.school_students_venue_assigned(assigned_school):
        resp_teacher = rteachers.filter(is_primary=True)[0]
        alt_resp_teacher = rteachers.filter(is_primary=False)[0]
        if resp_teacher:
            resp_teacher.answer_sheet_downloaded = datetime.now(tz=pytz.timezone("Africa/Johannesburg"))
            resp_teacher.save()
        if alt_resp_teacher:
            alt_resp_teacher.answer_sheet_downloaded = datetime.now(tz=pytz.timezone("Africa/Johannesburg"))
            alt_resp_teacher.save()
        return compadmin.generate_school_answer_sheets(request, [assigned_school])
    elif not rteachers:
        return HttpResponse("A responsible teacher has not been provided for your school yet.")
    else:
        return HttpResponse("Your school's answer sheets cannot be generated at this time.")

@login_required
def school_certificates(request, assigned_school=None):
    assigned_school = School.objects.get(assigned_to=request.user)
    students = SchoolStudent.objects.filter(school=assigned_school.id)
    return compadmin.makeCertificates(students, assigned_school)
