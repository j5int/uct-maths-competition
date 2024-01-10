from xhtml2pdf import pisa  
import sys
from django.utils import timezone

sys.path.append("../")

from apps.competition.models import School, ResponsibleTeacher, SchoolStudent
import os

# It seems that this file needs to be in the uctMaths folder and not competition. 
# Finding a workaround would make the code cleaner.

# All processes which could cause the server to hang due to run-time or volume should
# be background tasks

def current_time():
    t = timezone.now()
    return "%d-%d-%d %d:%d:%d" % (t.year, t.month, t.day, t.hour, t.minute, t.second)

def bg_email_results(school_id):
    
    print("%s: Emailing results for school with ID: %s" %(current_time(), str(school_id)) )
    from apps.competition.compadmin import printer_school_report
    from apps.competition.reports import send_results

    school = School.objects.filter(id=school_id)[0]
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
def bg_generate_school_answer_sheets(school_id):
    from apps.competition.compadmin import printer_answer_sheet
    from apps.competition.reports import send_answer_sheets
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

def bg_generate_as_grade_distinction(grade, paired):
    from apps.competition.compadmin import get_student_answer_sheet
    from io import StringIO
    import datetime
    from apps.competition.reports import send_grade_answer_sheets_to_organiser

    BATCH_SIZE = 2000

    startTime = datetime.datetime.now()
    students = SchoolStudent.objects.filter(grade=grade, paired=paired)
    if len(students) == 0:
        # Nothing to generate
        return
    batches = [students[i : i + BATCH_SIZE] for i in range(0, len(students), BATCH_SIZE)]
    for batch_no, batch in enumerate(batches):
        html = ""
        for pos, student in enumerate(batch):
            html += get_student_answer_sheet(None, student)

        filename = "generated_grade_answer_sheets/%s answer sheets - grade %d - %d of %d.pdf" % ("Pair" if paired else "Individual",
                                                                    grade, batch_no + 1, len(batches))
        if not os.path.exists("generated_grade_answer_sheets"):
            os.mkdir("generated_grade_answer_sheets")
        grade_result = open(filename, "w+b")
        print("Creating PDF for %s grade %d, batch %d of %d. Started at %s" % ("pairs" if paired else "individuals", grade, batch_no + 1, len(batches), str(startTime)))
        pdf = pisa.pisaDocument(html, grade_result, encoding="UTF-8")
        grade_result.close()
        send_grade_answer_sheets_to_organiser(filename)
        diff = datetime.datetime.now() - startTime 
        print("Batch completed. Time taken: %s" % str(diff))
    print("Task completed.")
