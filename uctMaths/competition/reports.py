from django.contrib.auth.decorators import login_required
from models import SchoolStudent, School, Invigilator, Venue, ResponsibleTeacher
from django.core.mail import EmailMessage
import datetime

import compadmin #import the competition administrator (secretary's) email (to be CC'd in the 
                 # report email.
import views

# Methods for very simple formatting of data entered by a certain user (filter)
# See info in settings.py for SMTP server emulation and set-up

@login_required
def send_confirmation(request,result,rteacher,in_school='UNDEFINED',cc_admin=False):
    """ Formats student information for the particular user and sends it via. smtp"""

    if request.user.first_name not in ['', None] and request.user.last_name  not in ['', None]:
        name = request.user.first_name + " " + request.user.last_name
    else:
        name = request.user.username
    #rteacher = ResponsibleTeacher.objects.filter(school = in_school)[0]
    #Header
    output_string = 'Dear %s, \n\n' \
                    'This email contains results for %s from the UCT Mathematics Competition. ' \
                    'Attached you will find a printer-friendly .pdf file that contains your school\'s ' \
                    'results. \n\n' \
                    'Regards,\n\n' \
                    'The UCT Mathematics Competition team'%(name, in_school)
    output_string += UMC_header()
    output_string += 'Results letter for %s\nRequested by %s\n%s\n'%(in_school, name, UMC_datetime())


    recipient_list = [rteacher.email]
    if cc_admin:
        recipient_list.append(compadmin.admin_emailaddress())

    email = EmailMessage(
                        '(Do not reply) UCT Mathematics Competition %s Competition Results'%(in_school),#Subject line
                        output_string, #Body
                        'UCT Mathematics Competition <UCTMathsCompetition@j5int.com>',#from
                        recipient_list,
                        )
    #result = response
    email.attach('%s_results.pdf'%(unicode(in_school)),result.getvalue(), mimetype='application/pdf')
    email.send()

def UMC_header(width=40):
    """ Text header for email """
    to_return = '\n\n%20s\n\n%20s\n\n'%('~'*10, 'UCT Mathematics Competition Results')
    return to_return


def UMC_datetime(width=40):
    """ Get/format current time/date of when the submission was passed """ 
    now = datetime.datetime.now()
    to_return = 'Generated %s:%s %s/%s/%s\n\n'%(now.hour, now.minute, now.day, now.month, now.year)
    return to_return
