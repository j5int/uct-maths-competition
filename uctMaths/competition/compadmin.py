# Some auxiliary functions and constants for competition
# administration.
from competition.models import SchoolStudent, School, Invigilator, Venue, ResponsibleTeacher 
from datetime import date

#A few administration constants and associated methods to be used around the website.

#The date until which entries are accepted
comp_closingdate=date(2013, 12, 19) #(YYYY, MM, DD) format
#The date of prizegiving
comp_prizegivingdate=date(2013, 12, 19) #(YYYY, MM, DD) format

admin_emailaddress='admin@admin.com' #Email address for inquiries/outgoing emails

def isOpen():
    """Logic to compare the closing date of the competition with today's date"""
    if date.today() > comp_closingdate:
        #print 'The competition is closed'
        return False
    else:
        #print 'The competition is open'
        return True

def closingDate():
    return str(comp_closingdate.day) + '/' + str(comp_closingdate.month)  + '/' + str(comp_closingdate.year)

#TODO: Auto-venue allocation algorithm
#def auto_allocate():
#    print 'auto_allocate'
#    student_list = SchoolStudent.objects.filter(school = assigned_school)
#    individual_list, pair_list = processGrade(student_list) #processGrade is defined below this method
#    #invigilator_list = Invigilator.objects.filter(school = assigned_school)
#    responsible_teacher = ResponsibleTeacher.objects.filter(school = assigned_school)

#Used in confirmation.py and views.py
def processGrade(student_list):
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

