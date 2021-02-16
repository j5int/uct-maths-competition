from django.contrib.auth.decorators import login_required
from models import SchoolStudent, School, Invigilator, Venue, ResponsibleTeacher, Competition
from django.core.mail import EmailMessage
import datetime

import compadmin #import the competition administrator (secretary's) email (to be CC'd in the 
                 # report email.
import views
import StringIO
import os

# Methods for very simple formatting of data entered by a certain user (filter)
# See info in settings.py for SMTP server emulation and set-up

def send_results(in_school, result, cc_admin=False):
    """ Formats student information for the particular user and sends it via. smtp"""
    rteacher = ResponsibleTeacher.objects.filter(school=in_school.id)[0]
    name = rteacher.firstname + " " + rteacher.surname
    #Header
    output_string = 'Dear %s, \n\n' \
                    'This email contains results for %s from the UCT Mathematics Competition. ' \
                    'Attached you will find a printer-friendly .pdf file that contains your school\'s ' \
                    'results. \n\n' \
                    'Regards,\n\n' \
                    'The UCT Mathematics Competition team'%(name, in_school.name)
    output_string += UMC_header("Results")
    output_string += 'Results letter for %s\nRequested by %s\n%s\n'%(in_school.name, name, UMC_datetime())


    recipient_list = [rteacher.email]
    if cc_admin:
        recipient_list.append(compadmin.admin_emailaddress())

    send_email(
                '(Do not reply) UCT Mathematics Competition %s Competition Results'%(in_school.name),#Subject line
                output_string, #Body
                'UCT Mathematics Competition <UCTMathsCompetition@j5int.com>',#from
                [{"name": '%s' % (compadmin.get_school_report_name(in_school)), "value": result.getvalue(), "type": "application/pdf"}],
                recipient_list
    )

def send_answer_sheets(school, answer_sheet, cc_admin=False):
    rteachers = ResponsibleTeacher.objects.filter(school=school.id)
    if not rteachers:
        print("No responsible teacher for school!")
        return
    rteacher = rteachers[0]
    #Header
    output_string = 'Dear %s, \n\n' \
                    'This email contains answer sheets for %s for the upcoming UCT Mathematics Competition. ' \
                    'Attached you will find a printer-friendly .pdf file that contains the answer sheets that ' \
                    'your students will write on. \n\n' \
                    'Regards,\n\n' \
                    'The UCT Mathematics Competition team'%(rteacher.firstname + " " + rteacher.surname, school.name)
    output_string += UMC_header("Answer Sheets")
    output_string += 'Answer sheets for %s\n%s\n'%(school.name, UMC_datetime())
    recipient_list = [rteacher.email]
    if cc_admin:
        recipient_list.append(compadmin.admin_emailaddress())

    send_email(
        "(Do not reply) UCT Mathematics Competition %s Answer Sheets" % (school.name),
        output_string,
        "UCT Mathematics Competition <UCTMathsCompetition@j5int.com>",
        [{"name": "%s" % (compadmin.get_answer_sheet_name(school)), "value": answer_sheet.getvalue(), "type": "application/pdf"}],
        recipient_list
    )

def send_grade_answer_sheets_to_organiser(pdf_attachment_filename):
    print("Emailing " + os.path.basename(pdf_attachment_filename) + " to organiser.")
    f = open(pdf_attachment_filename, "rb")
    output_string = """Dear admin,
    
    This email contains part of the collection of answer sheets for all students, separated by grade. This is being sent because of the request to generate all answer sheets. 
    """
    send_email(
        "(Do not reply) " + os.path.basename(pdf_attachment_filename),
        output_string,
        "UCT Mathematics Competition <UCTMathsCompetition@j5int.com>",
        [
            {
                "name": os.path.basename(pdf_attachment_filename), 
                "value": StringIO.StringIO(f.read()).getvalue(), 
                "type": "application/pdf"
            }
        ],
        [Competition.objects.filter()[0].admin_emailaddress]
    )
    f.close()

def send_email(subject, body, sender, attachments, recipient_list):
    email = EmailMessage(
                        subject, body, sender, recipient_list,
    )
    for item in attachments:
        email.attach(item["name"], item["value"], mimetype=item["type"])
    email.send()

def UMC_header(content, width=40):
    """ Text header for email """
    to_return = '\n\n%20s\n\n%20s\n\n'%('~'*10, 'UCT Mathematics Competition ' + content)
    return to_return


def UMC_datetime(width=40):
    """ Get/format current time/date of when the submission was passed """ 
    now = datetime.datetime.now()
    to_return = 'Generated %s:%s %s/%s/%s\n\n'%(now.hour, now.minute, now.day, now.month, now.year)
    return to_return
