from django.contrib.auth.decorators import login_required
from models import SchoolStudent, School, Invigilator, Venue, ResponsibleTeacher
from django.core.mail import EmailMessage
import datetime

import compadmin #import the competition administrator (secretary's) email (to be CC'd in the 
                 # confirmation email.
import views

# Methods for very simple formatting of data entered by a certain user (filter)
# See info in settings.py for SMTP server emulation and set-up

@login_required
def send_confirmation(request, in_school='UNDEFINED',cc_admin=False):
    """ Formats student information for the particular user and sends it via. smtp"""

    if request.user.first_name not in ['', None] and request.user.last_name  not in ['', None]:
        name = request.user.first_name + " " + request.user.last_name
    else:
        name = request.user.username
    student_list = SchoolStudent.objects.filter(school = in_school)
    invigilator_list = Invigilator.objects.filter(school = in_school)
    rteacher = ResponsibleTeacher.objects.filter(school = in_school)[0]

    #Header
    output_string = 'Dear %s, \n\n' \
                    'This email confirms your entry for %s to the UCT Mathematics Competition. ' \
                    'Attached you will find a printer-friendly .pdf file that contains a record of your school\'s ' \
                    'entry. Below is a text-based summary of that same information.\n\n' \
                    'Regards,\n\n' \
                    'The UCT Mathematics Competition team'%(name, in_school)
    output_string += UMC_header()
    output_string += 'Confirmation letter for %s\nRequested by %s\n%s\n'%(in_school, name, UMC_datetime())

    output_string += print_responsibleTeacher(rteacher)
    output_string += print_invigilators(invigilator_list)
    output_string += print_students(student_list)
    ### Debugging - output to file ###
    #temp_output = open('confirmation.txt', 'w')
    #temp_output.write(temp_output)
    #temp_output.close()

    recipient_list = [request.user.email]
    if cc_admin:
        recipient_list.append(compadmin.admin_emailaddress())

    email = EmailMessage(
                        '(Do not reply) UCT Mathematics Competition %s Entry Confirmation'%(in_school),#Subject line
                        output_string, #Body
                        'UCT Mathematics Competition <UCTMathsCompetition@j5int.com>',#from
                        recipient_list,
                        )
    result = views.printer_entry_result(request)
    email.attach('%s_confirmation.pdf'%(unicode(in_school)),result.getvalue(), mimetype='application/pdf')
    email.send()


def print_students(student_list,width=40):
    """ Prints and formats the data for each grade """

    return_string = ''
    #Bins for grouping team and individual participants
    pair_list = { 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0}
    single_list = { 8 : [], 9 : [], 10 : [], 11 : [], 12 : []}

    try:
        #Binning method
        for student in student_list:
            if student.paired: # Better pair condition logic for this!
                pair_list[student.grade] += 1
            else: 
                single_list[student.grade].append((student.firstname, student.surname))

    except IndexError: #If the user submitted an empty form
        print 'Index Error (Confirmation email)'
        pass #Report empty list to render?

    # Print out formatted lists for pairs and single participants
    for grade in range(8, 12 + 1):	
        grade_string = '\nGrade %d students (%d registered):\n'%(grade, len(single_list[grade]) + pair_list[grade]*2)
        #grade_string += '\n%-15s %-15s \n%s\n'%('First Name', 'Surname', '- '*int(width/2))

        for single in single_list[grade]:
            grade_string+= '%s, %s\n'%(single[1], single[0])#str(single[2].upper()))

        if compadmin.admin_number_of_pairs() > 0:
            grade_string += '\n%d pair(s) registered for grade %d\n'%(pair_list[grade], grade) 

        #for pair_register in range(1, pair_list[grade]/2+1):
        #    grade_string += 'Group %d: \n\n'%(pair_register)

        return_string += grade_string

    return return_string #Stored as one long formatted string. 


def print_invigilators(invigilator_list, width=60):
    """Print invigilator section"""

    #Heading for invigilator section
    invig_string = '\nInvigilators:\n'
    invig_string += '%-20s %-15s %-15s %-20s %-20s\n%s\n'%('Name', 'Phone','(Alternate)', 'Email', 'Notes', '-'*80)

    try:
        for invigilator in invigilator_list:
            invig_string += '%-20s %-15s %-15s %-20s %-20s\n'%(invigilator.surname+', '+invigilator.firstname, invigilator.phone_primary, invigilator.phone_alt, invigilator.email, invigilator.notes)

    except IndexError: #If the user submitted an empty form
        print 'Index Error (Confirmation email - invigilator)'
        pass #Report empty list to render?

    return invig_string

def print_responsibleTeacher(rteacher, width=60):
    """Print responsible teacher section"""

    #Heading
    rt_string = 'Responsible teacher:\n'
    rt_string += '%-20s %-15s %-15s %-20s\n%s\n'%('Name', 'Phone','(Alternate)', 'Email','-'*80)

    try:
        rt_string += '%-20s %-15s %-15s %-20s\n'%(rteacher.surname+', '+rteacher.firstname, rteacher.phone_primary, rteacher.phone_alt,rteacher.email) 

    except IndexError: #If the user submitted an empty form
        print 'Index Error (Confirmation email - rteacher)'
        pass #Report empty list to render?

    return rt_string


def UMC_header(width=40):
    """ Text header for email """
    to_return = '\n\n%20s\n\n%20s\n\n'%('~'*10, 'UCT Mathematics Competition Entry')
    return to_return


def UMC_datetime(width=40):
    """ Get/format current time/date of when the submission was passed """ 
    now = datetime.datetime.now()
    to_return = 'Generated %s:%s %s/%s/%s\n\n'%(now.hour, now.minute, now.day, now.month, now.year)
    return to_return
