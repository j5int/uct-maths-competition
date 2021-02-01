from background_task import background

import ho.pisa as pisa
import sys
from django.utils import timezone
import pytz
import settings
sys.path.append("../")

from competition.models import School, ResponsibleTeacher

# It seems that this file needs to be in the uctMaths folder and not competition. 
# Finding a workaround would make the code cleaner.

# All processes which could cause the server to hang due to run-time or volume should
# be background tasks

def current_time():
    t = timezone.now()
    return "%d-%d-%d %d:%d:%d" % (t.year, t.month, t.day, t.hour, t.minute, t.second)

@background(queue="report-email-queue")
def bg_email_results(school_id):
    
    print("%s: Emailing results for school with ID: %s" %(current_time(), str(school_id)) )
    from competition.compadmin import printer_school_report, timestamp_now
    from competition.reports import send_results

    school = School.objects.filter(id=school_id)[0]
    print(school.name)
    rteachers = ResponsibleTeacher.objects.filter(school=school.id)
    if len(rteachers) == 0:
        print("%s: %s has not been allocated a responsible teacher!" % (current_time(), school.name))
        return
    
    result = printer_school_report(None, [school])
    send_results(school, result, True)
    school.report_emailed = timezone.now()
    school.save()
    print("%s: Finished sending report email for %s." % (current_time(), school.name))

# Ideally this function would be in competition/compadmin.py
@background(queue="AS-generation-queue")
def bg_generate_school_answer_sheets(school_id):
    from competition.compadmin import printer_answer_sheet, timestamp_now
    from competition.reports import send_answer_sheets
    print("%s: Emailing answer sheets for school with ID: %s" %(current_time(), str(school_id)) )

    school = School.objects.filter(id=school_id)[0]
    
    if len(ResponsibleTeacher.objects.filter(school=school.id)) == 0:
        print("%s: Cannot send an email to a school with no assigned responsible teacher!" % (current_time()))
        return
    pdf = printer_answer_sheet(None, school)
    if not pdf:
        print("%s: Unable to get answer sheets!" % (current_time()))
        return
    
    send_answer_sheets(school, pdf, True)
    school.answer_sheets_emailed = timezone.now()
    school.save()
    print("%s: Finished sending answer sheet email for %s." % (current_time(), school.name))
