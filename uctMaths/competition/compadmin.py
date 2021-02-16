# Some auxiliary functions and constants for competition
# administration.
from __future__ import unicode_literals
from models import SchoolStudent, School, Invigilator, Venue, ResponsibleTeacher, Competition, LOCATIONS
from datetime import date
import xlwt
from django.http import HttpResponse, HttpResponseRedirect
import zipfile
import datetime
from django.core import exceptions 
import views
#A few administration constants and associated methods to be used around the website.

from django.core.context_processors import csrf
import ho.pisa as pisa
# StrIO can accept str and unicode values
import StringIO as StrIO
# CStringIO doesn't work well with unicode values. Only use it for UTF-8 encoded str.
import cStringIO as StringIO
from django.template.loader import get_template
from django.template import loader, Context
from models import LOCATIONS

import reports

import os
import sys
sys.path.append("../")
sys.setrecursionlimit(10000)

from background_task import background
from uctMaths.background_tasks import bg_generate_school_answer_sheets, bg_email_results, bg_generate_as_grade_distinction

def admin_emailaddress():
    """Get the competition admin's email address from the Competition.objects entry"""
    comp = Competition.objects.all() #Should only be one!
    if comp.count() == 1:
        return comp[0].admin_emailaddress
    else:
        return 'Not specified' #ERROR - essentially

def admin_number_of_pairs():
    """Get the number of pairs allowed in the competition"""
    comp = Competition.objects.all() #Should only be one!
    if comp.count() == 1:
        return comp[0].number_of_pairs
    else:
        return 0 #ERROR - essentially

def admin_number_of_individuals():
    """Get the number of individuals allowed in the competition"""
    comp = Competition.objects.all() #Should only be one!
    if comp.count() == 1:
        return comp[0].number_of_individuals
    else:
        return 0 #ERROR - essentially

def admin_individuals_range(begin=0):
    """Get the range of individuals allowed in the competition"""
    comp = Competition.objects.all() #Should only be one!
    if comp.count() == 1:
        return range(begin, comp[0].number_of_individuals)
    else:
        return 0 #ERROR - essentially

def admin_pairs_range(begin=0):
    """Get the range of pairs allowed in the competition"""
    comp = Competition.objects.all() #Should only be one!
    if comp.count() == 1:
        return range(begin, comp[0].number_of_pairs)
    else:
        return 0 #ERROR - essentially


def isOpen():
    """Logic to compare the closing date of the competition with today's date"""
    comp = Competition.objects.all()

    if comp.count() == 1:
        if date.today() > comp[0].newentries_Closedate or date.today() < comp[0].newentries_Opendate:
            #print 'The competition is closed'
            return False
        else: #'The competition is open'
            return True
    else:
            return False #Error!!

def closingDate():
    """ Display formatted dd/mm/yyyy date as string. Or message on unspecified date (to be displayed on 'Profile' page) """
    comp = Competition.objects.all()
    if comp.count() == 1:
        comp_closingdate = comp[0].newentries_Closedate
        return str(comp_closingdate.day) + '/' + str(comp_closingdate.month)  + '/' + str(comp_closingdate.year)
    else: #Error!
        return 'a date yet to be set by the admin'

def gradeBucket(student_list):
    """
    Sort ("bucket") the QuerySet list of students into a dict with key based on
    grade (integer), pairing status (boolean), and location (string).
    """

    #The key is a tuple: (grade, is_paired, location)
    grade_bucket = {}

    for grade in range(8,13):
        for is_paired in [True, False]:
            for location in LOCATIONS:
                grade_bucket[grade, is_paired, location[0]] = []
            grade_bucket[grade, is_paired, 'ALL'] = []

    try:
        for student in student_list:
            grade_bucket[student.grade, student.paired, student.location].append(student)
            grade_bucket[student.grade, student.paired, 'ALL'].append(student)
    except IndexError:
        # Empty QuerySet
        print 'Index Error'

    return grade_bucket


def auto_allocate(venue_list):
    """ Auto allocates currently unallocated (to avoid double-allocation when QuerySet is a subset of venues) students to the provided QuerySet (a list of venues selected at the admin interface. Grade set to 'None' venues are ignored in the allocation process."""
    venue_deallocate(venue_list)
    student_list = SchoolStudent.objects.all().filter(venue='').order_by('grade') #Order by grade (ASCENDING)

    print len(student_list), ' students are unallocated'
    grade_bucket = gradeBucket(student_list)

    for venue in venue_list.order_by('-seats'): #Allocate from the largest venue first.
        #Each venue in QuerySet where grade!=None; while students exist in grade bucket 
        #See method 'grade_bucket' for bucket format (Key is a tuple!)
        while venue.grade and grade_bucket[venue.grade, venue.allocated_to_pairs, venue.location]:
            #Pair logic
            if venue.occupied_seats < venue.seats - 1 and venue.allocated_to_pairs:
                pair = grade_bucket[venue.grade, venue.allocated_to_pairs, venue.location].pop()
                pair.venue = venue.code
                pair.save()

                #Update venue
                venue.occupied_seats += 2
                venue.save()

            #Individual logic
            elif venue.occupied_seats < venue.seats and not venue.allocated_to_pairs:
                student = grade_bucket[venue.grade, venue.allocated_to_pairs, venue.location].pop()
                student.venue = venue.code
                student.save()

                venue.occupied_seats += 1
                venue.save()

            else:
                break

def venue_deallocate(venue_list):
    """ Deallocate students from venues. Clear student.venue and venue.pairs, venue.individuals """
    student_list = SchoolStudent.objects.all().order_by('grade')

    for venue in venue_list:
        venue.occupied_seats = 0
        venue.save()

        for student in student_list: #Edit student records to reflect deallocation
            if student.venue == venue.code:
                student.venue = ''
                student.save()

#Used in confirmation.py and views.py
def processGrade(student_list):
    """ Helper function for sorting students into grades, pairs. Returns two lists: individuals, pairs. Somewhat deprecated by gradeBucket but still used in some places in the code. eg. Generating confirmation email when only the number of pairs for each grade are needed."""

    pair_list = { 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0}
    individual_list = { 8 : [] , 9 :  [] , 10 :  [] , 11 : [] , 12 : [] }

    try:
        for student in student_list:
            if student.paired:
                #Count number of pairs for each grade
                pair_list[student.grade]+=1 
            else: 
                individual_list[student.grade].append(student)
    except IndexError:
        print 'Index Error'

    return individual_list, pair_list

#Export venue lists to workbook.
#See http://scienceoss.com/write-excel-files-with-python-using-xlwt/
def output_register(venue_list):
    """Generate a register for each venue. Output QuerySet (venues) as separated sheets on an xls (excel document). A summary sheet of all venues in QuerySet is generated as first sheet."""

    output_workbook = xlwt.Workbook()
    student_header = ['Reference No.','School', 'First name(s)','Surname']

    #Generate summary sheet
    #----------------------
    summary_sheet = output_workbook.add_sheet('Venue_summary')
    summary_sheet.write(0,0,'Summary page')

    venue_h = ['Location', 'Venue', 'Building', 'Grade', 'Available seats', 'Occupied seats', 'Allocation']

    for index, header in enumerate(venue_h):
        summary_sheet.write(1, index, header)

    venue_list.order_by('grade')

    for v_index, venue in enumerate(venue_list):
        summary_sheet.write(v_index+2,0,str(venue.location))
        summary_sheet.write(v_index+2,1,str(venue.code))
        summary_sheet.write(v_index+2,2,venue.building)
        summary_sheet.write(v_index+2,3,str(venue.grade))
        summary_sheet.write(v_index+2,4,str(venue.seats))
        summary_sheet.write(v_index+2,5,str(venue.occupied_seats or 0))

        if venue.allocated_to_pairs:
            summary_sheet.write(v_index+2,6,'Pairs')
        else:
            summary_sheet.write(v_index+2,6,'Individuals')

    #TODO?:Print out the unallocated students?


    #Generate a 'Register' sheet for each venue in QuerySet
    #------------------------------------------------------
    for venue in venue_list:
        student_list = SchoolStudent.objects.all().filter(venue=venue.code)
        
        #TODO? Include invigilators in the sheet?
        #invigilator_list = Invigilator.objects.all().filter(venue=venue.code)

        if student_list:
            venue_sheet = output_workbook.add_sheet(str(venue.code))
            venue_header = [ #Heading for each sheet. ie. what this sheet contains (for when it's printed)
                            'Location:', str(venue.location),
                            'Venue:', str(venue.code),
                            'Building: ', str(venue.building),
                            'Grade:', str(venue.grade),
                            'Occupancy:', str(venue.occupied_seats or 0)+'/'+str(venue.seats),
                            'Allocation:', 'Pairs' if venue.allocated_to_pairs else 'Individuals'
                            ]

            #Print venue_header to the sheet
            for index in range(0,6):
                venue_sheet.write(index,0, venue_header[index*2])
                venue_sheet.write(index,1, venue_header[index*2+1])

            # Print student header (name columns) to sheet
            for h_index, word in enumerate(student_header):
                venue_sheet.write(7,h_index,student_header[h_index])

            # Print the students in that venue to sheet
            for s_index, student in enumerate(student_list):
                venue_sheet.write(s_index+8,0,str(student.reference))
                venue_sheet.write(s_index+8,2,student.firstname)
                venue_sheet.write(s_index+8,3,student.surname)
                venue_sheet.write(s_index+8,1,unicode(student.school))

        else:
            pass # Venue is empty - no point making a sheet for it...

    # Generate response and serve file to the user
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=venue_register(%s).xls'%(timestamp_now())
    response['Content-Type'] = 'application/ms-excel'
    output_workbook.save(response)
    return response

#Export venue lists to workbook.
#See http://scienceoss.com/write-excel-files-with-python-using-xlwt/

def output_studentlists(student_list):
    """Output Pair and Individual lists (SchoolStudent list QuerySet) for each grade and location as sheets on an xls"""

    grade_bucket = gradeBucket(student_list)

    output_workbook = xlwt.Workbook()
    student_header = ['School', 'Reference No.', 'First name(s)', 'Surname', 'Venue']

    for location in LOCATIONS:
        for grade in range(8, 13):

            #Process individual page
            student_sheet = output_workbook.add_sheet(location[1] + ' Grade ' + str(grade)+' individuals')

            #Print title and header
            student_sheet.write(0, 0, location[1] + ' Grade ' + str(grade) + ' individuals')
            for h_index, word in enumerate(student_header):
                student_sheet.write(1, h_index,word)
            #Print each student's details
            for index, student in enumerate(grade_bucket[grade, False, location[0]]):
                student_sheet.write(index+2, 0, unicode(student.school))
                student_sheet.write(index+2, 1, str(student.reference))
                student_sheet.write(index+2, 2, student.firstname)
                student_sheet.write(index+2, 3, student.surname)
                student_sheet.write(index+2, 4, student.venue)

            #Process pairs page
            student_sheet = output_workbook.add_sheet(location[1] + ' Grade ' + str(grade)+' pairs')
            #Print title and header
            student_sheet.write(0, 0, location[1] + ' Grade ' + str(grade) + ' pairs')
            for h_index, word in enumerate(student_header):
                student_sheet.write(1,h_index,word)
            #Print each student's details
            for index, student in enumerate(grade_bucket[grade, True, location[0]]):
                student_sheet.write(index+2, 0, unicode(student.school))
                student_sheet.write(index+2, 1, str(student.reference))
                student_sheet.write(index+2, 2, student.firstname)
                student_sheet.write(index+2, 3, student.surname)
                student_sheet.write(index+2, 4, student.venue)

    #Generate response and serve file (xls) to user
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=studentlist(%s).xls'%(timestamp_now())
    response['Content-Type'] = 'application/ms-excel'
    output_workbook.save(response)
    return response

def output_studenttags(student_list):
    """Generate individual and pair MailMerge lists for SchoolStudent QuerySet per location and grade.
    Served to user as a .zip file containing all the lists."""
    grade_bucket = gradeBucket(student_list)

    #Generate individuals name tags 
    #Eg: "Ref#","Name Surname","School name",Grade(int),"Building Room(Code)"
    venue_list = Venue.objects.all()
    output_stringIO = StringIO.StringIO() #Used to write to files then zip
    
    with zipfile.ZipFile(output_stringIO, 'w') as zipf:
        for location in LOCATIONS:
            for grade in range(8, 13):
                output_string = StrIO.StringIO()
                for student in grade_bucket[grade, False, location[0]]: #Individuals in grade + location
                    venue_object = [venue for venue in venue_list if venue.code == student.venue]
                    s_line = u''
                    s_line += '\"' + student.reference + '\",'
                    s_line += '\"' + student.firstname + ' ' + student.surname + '\",'
                    s_line += '\"' + unicode(student.school) + '\",'
                    s_line += str(student.grade) + ','
                    venue_str = venue_object[0] if len(venue_object) == 1 else 'Unallocated'
                    s_line += '\"' + unicode(venue_str) + '\"\n'
                    output_string.write(s_line)

                #Generate file from StringIO and write to zip (ensure unicode UTF-* encoding is used)
                zipf.writestr('Mailmerge_' + location[0] + '_GRD' + str(grade) + '_IND.txt', output_string.getvalue().encode('utf-8'))
                output_string.close()

                output_string = StrIO.StringIO()
                for student in grade_bucket[grade, True, location[0]]: #Pairs in grade + location
                    venue_object = [venue for venue in venue_list if venue.code == student.venue]
                    s_line = u''
                    s_line += '\"' + student.reference + '\",'
                    s_line += '\"' + student.firstname + ' ' + student.surname + '\",'
                    s_line += '\"' + unicode(student.school) + '\",'
                    s_line += str(student.grade) + ','
                    venue_str = venue_object[0] if len(venue_object) == 1 else 'Unallocated'
                    s_line += '\"' + unicode(venue_str) + '\"\n'
                    output_string.write(s_line)

                #Generate file from StringIO and write to zip (ensure unicode UTF-* encoding is used)
                zipf.writestr('Mailmerge_' + location[0] + '_GRD' +str(grade) + '_PAR.txt',
                              output_string.getvalue().encode('utf-8'))
                output_string.close()

    #Generate response and serve file to the user
    response = HttpResponse(output_stringIO.getvalue())
    response['Content-Disposition'] = 'attachment; filename=mailmergestudents(%s).zip'%(timestamp_now())
    response['Content-Type'] = 'application/x-zip-compressed'
    return response

#Called by admin to remove users associated with schools (Just clear that field)
def remove_user_assoc(school_list):
    """ Remove School-User association for School QuerySet. """
    for school in school_list:
        school.assigned_to = None
        school.save()

def remove_emails_addresses(school_list):
    """ Remove all addresses and school phone numbers from the database """
    for school in school_list:
        school.address = ""
        school.phone = ""
        school.save()

#Called by admin to generate formatted 'tag list' for selected schools
def output_schooltaglists(school_list):
    """ Generate the tags for a School QuerySet. Served as a single text file in HttpResponse. """

    output_stringio = StrIO.StringIO()

    #Generate and format school entry (as in spec. sheet)
    for school in school_list:
        s_entry = '\"' + school.contact + '\",'
        s_entry += '\"' + school.name + '\",'
        s_entry += '\"' + school.address + '\"\n'
        output_stringio.write(s_entry)

    #Serve to user as text file
    response = HttpResponse(output_stringio.getvalue().encode('utf-8'))
    response['Content-Disposition'] = 'attachment; filename=schooltags(%s).txt'%(timestamp_now())
    return response

def upload_results(request, student_list):
    """Facilitate upload of .RES (the results) files. Redirects to custom Admin page (upload_results.html), the logic contained in compadmin_views.py."""
    #Return response of redirect page
    response = HttpResponseRedirect('../../../competition/admin/upload_results.html')
    return response
    
def rank_schools(school_list):
    """ Ranks schools based on a sum of the top X scores. X is set via the 'Competition' form. """
    comp = Competition.objects.all() #Should only be one!
    
    if comp.count() == 1:
        top_score_candidates = comp[0].num_schoolcandidate_scores
    else:
        top_score_candidates = 0
        
    all_schools = School.objects.all()

    #Calculate total scores for all schools
    for school in all_schools:
        #Get ONLY the candidates from that school and order by score DESCENDING
        #FIXME ?: These DB operations just wouldn't work with the distinct command. Using less efficient python-lists methods
        #candidates = SchoolStudent.objects.order_by('reference').distinct('reference')#.filter(school=school).exclude(score=None)
        #candidates = candidates.order_by('-score')

        candidates = SchoolStudent.objects.filter(school=school).exclude(score=None).order_by('-score')

        #Calculate schools' total scores
        total_score = 0
        #Sum candidates scores (already sorted in descending order)
        for i, c in enumerate(candidates):
            if i < top_score_candidates:
                total_score = total_score + c.score
        school.report_emailed = None
        school.score = total_score
        school.save()

    #Rank schools
    #Order all schools in descending order
    all_schools = all_schools.order_by('-score')

    #Ensure that schools with equal scores are assigned the same rank
    #Generate a list from the schools (so that I can use .pop(0) commands on it)
    school_selection = []
    for s in all_schools:
        school_selection.append(s)

    rank_base = 1 
    rank_delta = 0 #Used when multiple schools have the same score

    while school_selection: #while the list is not empty

        rank_base = rank_base + rank_delta
        
        school = school_selection.pop(0)
        school.rank = rank_base
        current_score = school.score
        school.save()
        
        rank_delta = 1
        #Assign all schools with the same score the same rank
        #Use the rank_delta as a counter
        while school_selection and school_selection[0].score == current_score: 
            school = school_selection.pop(0)
            school.rank = rank_base
            rank_delta = rank_delta + 1
            school.save()


def rank_students(student_list):
    """Rank students on their uploaded score. Used if a score has been changed and the remaining students need to be re-classified"""

    #Rank students
    #Order all students in descending score order
    #Ensure that students with equal scores are assigned the same rank
    #Generate a list from the students (so that I can use .pop(0) commands on it)
    absent_students = SchoolStudent.objects.all().filter(score=None)
    for ab_stu in absent_students:
        ab_stu.rank = None
        ab_stu.save()

    #Need to do this for each grade, for paired/individuals.
    for grade_i in range(8, 13):
        pstudent_list=SchoolStudent.objects.all().filter(paired=True, grade=grade_i).exclude(score=None).order_by('-score')
        score_studentlist(pstudent_list)
        istudent_list=SchoolStudent.objects.all().filter(paired=False, grade=grade_i).exclude(score=None).order_by('-score')
        score_studentlist(istudent_list)

def score_studentlist(student_list):
    student_selection = []

    for s in student_list:
        student_selection.append(s)

    rank_base = 1 
    rank_delta = 0 #Used when multiple schools have the same score


    while student_selection: #while the list is not empty

        rank_base = rank_base + rank_delta
        
        student = student_selection.pop(0)
        student.rank = rank_base
        student.award = ''
        current_score = student.score
        student.save()
        
        rank_delta = 1
        #Assign all schools with the same score the same rank
        #Use the rank_delta as a counter
        while student_selection and student_selection[0].score == current_score: 
            student = student_selection.pop(0)
            student.rank = rank_base
            student.award = ''
            rank_delta = rank_delta + 1
            student.save()


def export_awards(request, student_list):
    """ Assign awards to participants (QuerySet is list of students) to students based on their rank. Serves an excel workbook with the awards for each student."""
    output_workbook = xlwt.Workbook()
    #Ranked gold for each grade (pairs, individuals separated) (alphabetical by surname)
    #Alphabetical list of school award winners
    #Generate gold-awards list (Top 10 individuals, top 3 pairs)

    school_list = School.objects.all()
    student_list = SchoolStudent.objects.all() #Regardless of admin UI selection

    for igrade in range(8, 13):
        #Gold awards
        wb_sheet = output_workbook.add_sheet('Gold Grade %d'%(igrade))
        #Generate QuerySets for GOLD medal winners (sorted by rank (descending))
        pairQS = student_list.filter(grade = igrade, paired=True, award= 'G').order_by('rank')
        individualQS = student_list.filter(grade = igrade, paired=False, award = 'G').order_by('rank')
        pairs_offset = 4 #Using an offset accounts for situations where more than 10 people are getting gold (ties at rank=10)

        wb_sheet.write(1,0,'Gold Award Winners: Grade %d Individuals'%(igrade))

        header = ['Rank', 'School', 'Reference', 'First Name', 'Last Name', 'Grade']
        for i, h in enumerate(header):
            wb_sheet.write(2, i, '%s'%h)
        pairs_offset = pairs_offset + 2

        for index, individual in enumerate(individualQS):
            wb_sheet.write(index+3,0,str(individual.rank))
            wb_sheet.write(index+3,1,unicode(individual.school))
            wb_sheet.write(index+3,2,str(individual.reference))
            wb_sheet.write(index+3,3,individual.firstname)
            wb_sheet.write(index+3,4,individual.surname)
            wb_sheet.write(index+3,5,individual.grade)
            school_list=school_list.exclude(name=individual.school) #Exclude school for Oxford prize
            pairs_offset = pairs_offset + 1
        
        wb_sheet.write(pairs_offset,0,'Gold Award Winners: Grade %d Pairs'%(igrade))
        header = ['Rank', 'School', 'Reference', 'First Name', 'Last Name', 'Grade']
        for i, h in enumerate(header):
            wb_sheet.write(pairs_offset+1, i, '%s'%h)
        pairs_offset = pairs_offset + 2
        for index, pair in enumerate(pairQS):
            wb_sheet.write(index+pairs_offset,0,str(pair.rank))
            wb_sheet.write(index+pairs_offset,1,unicode(pair.school))
            wb_sheet.write(index+pairs_offset,2,str(pair.reference))
            wb_sheet.write(index+pairs_offset,3,pair.firstname)
            wb_sheet.write(index+pairs_offset,4,pair.surname)
            wb_sheet.write(index+pairs_offset,5,pair.grade)
            school_list=school_list.exclude(name=pair.school) #Exclude school for Oxford prize

        #Merit awards
        wb_sheet = output_workbook.add_sheet('Merit Grade %d'%(igrade))
        #Generate QuerySets for MERIT medal winners (sorted by school (name descending))
        pairQS = student_list.filter(grade = igrade, paired=True, award__contains = 'M').order_by('school')
        individualQS = student_list.filter(grade = igrade, paired=False, award__contains = 'M').order_by('school')
        pairs_offset = 4 #Using an offset accounts for situations where more than 10 people are getting merit (ties at rank=200)

        wb_sheet.write(1,0,'Merit Award Winners: Grade %d Individuals'%(igrade))
        header = ['Rank', 'School', 'Reference', 'First Name', 'Last Name', 'Grade']
        for i, h in enumerate(header):
            wb_sheet.write(2, i, '%s'%h)
        pairs_offset = pairs_offset + 2

        for index, individual in enumerate(individualQS):
            wb_sheet.write(index+3,0,str(individual.rank))
            wb_sheet.write(index+3,1,unicode(individual.school))
            wb_sheet.write(index+3,2,str(individual.reference))
            wb_sheet.write(index+3,3,individual.firstname)
            wb_sheet.write(index+3,4,individual.surname)
            wb_sheet.write(index+3,5,individual.grade)
            pairs_offset = pairs_offset + 1
        
        wb_sheet.write(pairs_offset,0,'Merit Award Winners: Grade %d Pairs'%(igrade))
        header = ['Rank', 'School', 'Reference', 'First Name', 'Last Name', 'Grade']
        for i, h in enumerate(header):
            wb_sheet.write(pairs_offset+1, i, '%s'%h)
        pairs_offset = pairs_offset + 2
        for index, pair in enumerate(pairQS):
            wb_sheet.write(index+pairs_offset,0,str(pair.rank))
            wb_sheet.write(index+pairs_offset,1,unicode(pair.school))
            wb_sheet.write(index+pairs_offset,2,str(pair.reference))
            wb_sheet.write(index+pairs_offset,3,pair.firstname)
            wb_sheet.write(index+pairs_offset,4,pair.surname)
            wb_sheet.write(index+pairs_offset,5,pair.grade)


    #TODO Oxford prizes. 
    #School awards (Oxford prizes) are assigned to the top individual in each school where the school did not receive an individual or pair Gold award
    wb_sheet = output_workbook.add_sheet('Oxford Prizes (School Award)')
    award_winners = []
    
    for school in school_list:
        #Get the students from the eligible school, order by score (descending)
        school_students = SchoolStudent.objects.filter(school=school, paired=False, award__contains = 'OX').order_by('-score')

        if school_students:
            award_winners.append(school_students[0])

    wb_sheet.write(0, 0, 'Oxford School Award')
    header = ['', 'School', 'Reference', 'First Name', 'Last Name', 'Grade', 'Rank', 'Award']
    for i, h in enumerate(header):
        wb_sheet.write(1, i, '%s'%h)

    for index, aw in enumerate(award_winners):
        wb_sheet.write(index+2,1,unicode(aw.school))
        wb_sheet.write(index+2,2,str(aw.reference))
        wb_sheet.write(index+2,3,aw.firstname)
        wb_sheet.write(index+2,4,aw.surname)
        wb_sheet.write(index+2,5,aw.grade)
        wb_sheet.write(index+2,6,aw.rank)
        wb_sheet.write(index+2,7,aw.award)

    #Return the response with attached content to the user
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=awardlist(%s).xls'%(timestamp_now())
    response['Content-Type'] = 'application/ms-excel'
    output_workbook.save(response)
    return response


def assign_student_awards():

    school_list = School.objects.all()
    student_list = SchoolStudent.objects.all()

    for student in student_list:
        student.award = None
        student.save()

    for igrade in range(8, 13):
        #Assign gold awards
        pairQS = student_list.filter(grade = igrade, paired=True, rank__lt=4, score__gt=0).order_by('rank')
        individualQS = student_list.filter(grade = igrade, paired=False, rank__lt=11, score__gt=0).order_by('rank')

        for individual in individualQS:
            school_list=school_list.exclude(name=individual.school)
            individual.award='G'
            individual.save()
            
        for pair in pairQS:
            school_list=school_list.exclude(name=pair.school)
            pair.award='G'
            pair.save()

        #Merit awards
        pairQS = student_list.filter(grade = igrade, paired=True, rank__lt=101, rank__gt=3, score__gt=0).order_by('school')
        individualQS = student_list.filter(grade = igrade, paired=False, rank__lt=201, rank__gt=10, score__gt=0).order_by('school')

        for individual in individualQS:
            individual.award='M'
            individual.save()

        for pair in pairQS:
            pair.award='M'
            pair.save()

    for ischool in school_list:
        #See condition below (student must have entered AND written)
        #TODO: Do this better - so far assumes no student actually scored 0
        school_students = SchoolStudent.objects.filter(school=ischool, paired=False, score__gt=1).order_by('rank')

        #School may only receive an OX award if 10 or more individuals entered AND wrote.
        if len(school_students)>= 10:
        
            #The award winner is the one with the highest rank at the school (including possible ties)
            if school_students:
                for student in school_students:
                    if student.rank == school_students[0].rank:
                        if student.award is None:
                            student.award = ''
                        student.award=student.award+'OX'
                        student.save()
                    else:
                        break

def school_summary(request):
    """ Return for DL a summary list of all the schools that have made an entry; also create a "email these people" line with all the relevant email addresses. Or something like that."""

    output_workbook = xlwt.Workbook()
    school_list = School.objects.all().order_by('name') #ie. regardless of selection at admin screen
    
    wb_sheet = output_workbook.add_sheet('School Summary')
    school_summary_sheet(school_list, wb_sheet)
    
    wb_sheet = output_workbook.add_sheet('School Ranking Summary')
    school_rank = school_list.order_by('-rank')
    school_summary_sheet(school_rank, wb_sheet, rank_extend=True)

    #Return the response with attached content to the user
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=school_summary(%s).xls'%(timestamp_now())
    response['Content-Type'] = 'application/ms-excel'
    output_workbook.save(response)
    return response

def export_courier_address(request, school_list):
    """ Return for DL a list of school courier addresses"""
    output_workbook = xlwt.Workbook()
    errorSheet = False
    wb_sheet = output_workbook.add_sheet('School Addresses')
    header = ['Company Name','Email','Address','City','Postal/Zip Code','Province/Region','Country','Contact Name','Tel. No.']
    cell_row_offset = 0
    for index, h in enumerate(header):
        wb_sheet.write(cell_row_offset,index,'%s'%(h))
    
    cell_row_offset+=1
    error_sheet = None
    error_row = 0
    for ischool in school_list:
        errors = []
        resp_teacher = ResponsibleTeacher.objects.filter(school = ischool)
        full = ischool.address.split(',')
        full+=['']*(3-len(full))
        
        

        if(not resp_teacher):
            errors.append("responsible teacher")
        if(not full[0]):
            errors.append("address")
            if(not full[1]):
                errors.append("city")
                if(not full[2]):
                    errors.append("postal code") 
        if(not ischool.phone):
            errors.append("phone number")
        errorMessage ='No %s assigned to school' % ((', ').join(errors))
        if(errors):
            if(ischool.entered == 0):
                errorMessage = "Not entered"
            if(not errorSheet):
                error_sheet = output_workbook.add_sheet('Errors')
                error_sheet.write(error_row,0,"School")
                error_sheet.write(error_row,1,"Error")
            error_row+=1
            error_sheet.write(error_row,0,ischool.name)
            error_sheet.write(error_row,1,errorMessage)
            errorSheet = True
            continue 
        resp_teacher = resp_teacher[0]
        cell_row_offset = cell_row_offset + 1
        wb_sheet.write(cell_row_offset,0,unicode(ischool.name))
        wb_sheet.write(cell_row_offset,1,resp_teacher.email)
        wb_sheet.write(cell_row_offset,2,full[0])
        wb_sheet.write(cell_row_offset,3,full[2])
        wb_sheet.write(cell_row_offset,4,full[1])
        wb_sheet.write(cell_row_offset,5,"Western Cape")
        wb_sheet.write(cell_row_offset,6,"South Africa")
        wb_sheet.write(cell_row_offset,7,resp_teacher.firstname + " " + resp_teacher.surname)
        wb_sheet.write(cell_row_offset,8,ischool.phone)

    #Return the response with attached content to the user
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=school_addresses(%s).xls'%(timestamp_now())
    response['Content-Type'] = 'application/ms-excel'
    output_workbook.save(response)
    return response
    
    
def timestamp_now():
    now = datetime.datetime.now()
    to_return = '%s:%s[%s-%s-%s]'%(now.hour, now.minute, now.day, now.month, now.year)
    return to_return
    
def export_competition(request):
    """ Export all the information of this year's competition in single excel file"""

    output_workbook = xlwt.Workbook()
    school_list = School.objects.all().order_by('name') #ie. regardless of selection at admin screen
    student_list = SchoolStudent.objects.all().order_by('school')
    #resp_teachers = ResponsibleTeacher.objects.all().order_by('school')
    invigilator_list = Invigilator.objects.all().order_by('school')


    # --------------------- Generate School Summary ---------------------------
    wb_sheet = output_workbook.add_sheet('School Summary')
    school_summary_sheet(school_list, wb_sheet, rank_extend=True)
    
    wb_sheet = output_workbook.add_sheet('Student Summary')
    archive_all_students(student_list, wb_sheet)
    
    wb_sheet = output_workbook.add_sheet('Invigilator Summary')
    archive_all_invigilators(invigilator_list, wb_sheet)

    #Return the response with attached content to the user
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=competition_archive(%s).xls'%(timestamp_now())
    response['Content-Type'] = 'application/ms-excel'
    output_workbook.save(response)
    return response

def school_summary_sheet(school_list, wb_sheet, rank_extend=False):
    """ Helper function to export_entire_competition and school_summary methods."""
    
    wb_sheet.write(0,0,'School summary sheet')
    wb_sheet.write(1,0,'Generated')
    wb_sheet.write(1,1,'%s'%(timestamp_now()))

    header = ['School', 'Location', 'Resp. Teach Name', 'Resp. Teach. Email', 'Resp. Teach. Phone', 'Resp. Teach. Alt Phone', 'Individuals', 'Pairs', 'Total']
    if rank_extend:
        header.append('Rank')
        header.append('Score')

    responsible_teacher_mailinglist = []

    cell_row_offset = 6

    for index, h in enumerate(header):
        wb_sheet.write(cell_row_offset,index,'%s'%(h))

    for school_obj in school_list:
        try: #Try get the student list for the school assigned to the requesting user
            student_list = SchoolStudent.objects.all().filter(school=school_obj)
            resp_teacher = ResponsibleTeacher.objects.get(school=school_obj)
        except exceptions.ObjectDoesNotExist:#Non-entry
            pass #Handled in if-not-empty statement below

        if student_list and resp_teacher: #If the lists are not empty

            grade_summary = gradeBucket(student_list) #Bin into categories (Pairing, grade)
            count_individuals = 0
            count_pairs = 0

            for i in range(8,13):
                count_pairs = count_pairs + len(grade_summary[i,True,'ALL'])
                count_individuals = count_individuals + len(grade_summary[i,False,'ALL'])

            cell_row_offset = cell_row_offset + 1
            wb_sheet.write(cell_row_offset,0,unicode(school_obj.name))
            wb_sheet.write(cell_row_offset,1,unicode(school_obj.location))
            wb_sheet.write(cell_row_offset,2,('%s %s')%(resp_teacher.firstname, resp_teacher.surname))
            wb_sheet.write(cell_row_offset,3,resp_teacher.email)
            wb_sheet.write(cell_row_offset,4,resp_teacher.phone_primary)
            wb_sheet.write(cell_row_offset,5,resp_teacher.phone_alt)
            wb_sheet.write(cell_row_offset,6,count_individuals)
            wb_sheet.write(cell_row_offset,7,count_pairs)
            wb_sheet.write(cell_row_offset,8,int(count_pairs*2 + count_individuals))
            if rank_extend:
                wb_sheet.write(cell_row_offset,9,school_obj.rank)
                wb_sheet.write(cell_row_offset,10,school_obj.score)

            responsible_teacher_mailinglist.append(resp_teacher.email)
    
    wb_sheet.write(3,0,'Mailing list')
    wb_sheet.write(3,1,', '.join(responsible_teacher_mailinglist))
    return wb_sheet

def archive_all_students(student_list, wb_sheet):
    """ Helper function to export_entire_competition."""

    wb_sheet.write(0,0,'Student summary sheet')
    wb_sheet.write(1,0,'Generated')
    wb_sheet.write(1,1,'%s'%(timestamp_now()))

    header = ['Reference', 'School', 'Location', 'Firstname', 'Surname', 'Grade', 'Score', 'Rank', 'Award','Language']

    cell_row_offset = 3

    for index, h in enumerate(header):
        wb_sheet.write(cell_row_offset,index,'%s'%(h))
    
    cell_row_offset = cell_row_offset + 1
    student_lang = {'b':'Bilingual', 'a':'Afrikaans', 'e':'English'}
    
    for student in student_list:#print details for every student on the list
        wb_sheet.write(cell_row_offset,0, student.reference)
        wb_sheet.write(cell_row_offset,1,unicode(student.school))
        wb_sheet.write(cell_row_offset,2,unicode(student.location))
        wb_sheet.write(cell_row_offset,3, student.firstname)
        wb_sheet.write(cell_row_offset,4, student.surname)
        wb_sheet.write(cell_row_offset,5, student.grade)
        wb_sheet.write(cell_row_offset,6, student.score)
        wb_sheet.write(cell_row_offset,7, student.rank)
        wb_sheet.write(cell_row_offset,8, student.award)
        wb_sheet.write(cell_row_offset,9, student_lang[student.language])
        cell_row_offset = cell_row_offset + 1

    return wb_sheet
    
def archive_all_invigilators(invigilator_list, wb_sheet):
    """ Helper function to export_err'thing."""
    wb_sheet.write(0,0,'Invigilator summary sheet')
    wb_sheet.write(1,0,'Generated')
    wb_sheet.write(1,1,'%s'%(timestamp_now()))

    header = ['School', 'Location', 'Firstname', 'Surname', 'Phone Primary', 'Alternate', 'Email']
    cell_row_offset = 3

    for index, h in enumerate(header):
        wb_sheet.write(cell_row_offset,index,'%s'%(h))
    
    cell_row_offset = cell_row_offset + 1
    
    for invigilator in invigilator_list:#Print details for all invigilators on the list
        wb_sheet.write(cell_row_offset,0,unicode(invigilator.school))
        wb_sheet.write(cell_row_offset,1,unicode(invigilator.location))
        wb_sheet.write(cell_row_offset,2, invigilator.firstname)
        wb_sheet.write(cell_row_offset,3, invigilator.surname)
        wb_sheet.write(cell_row_offset,4, invigilator.phone_primary)
        wb_sheet.write(cell_row_offset,5, invigilator.phone_alt)
        wb_sheet.write(cell_row_offset,6, invigilator.email)
        wb_sheet.write(cell_row_offset,7, invigilator.notes)
        cell_row_offset = cell_row_offset + 1

    return wb_sheet

def print_school_confirmations(request, school_list):
    result = views.printer_entry_result(request, school_list)
    response = HttpResponse(result.getvalue())
    response['Content-Disposition'] = 'attachment; filename=school_confirmation(%s).pdf'%(timestamp_now())
    response['Content-Type'] = 'application/pdf'
    return response
    
def timestamp_now():
    """ Time-stamp-formatting method. Used for all files served by server and a few xls sheets. NB: check cross-OS compatibility! """
    now = datetime.datetime.now()
    to_return = '%s:%s-%s%s%s'%(str(now.hour).zfill(2), str(now.minute).zfill(2), str(now.day).zfill(2), str(now.month).zfill(2), str(now.year).zfill(4))
    return to_return
    
def output_PRN_files(student_list):
    """Generate PRN files lists for all students, regardless of selection at admin UI. Served to user as a .zip file with each (10 files) Paired/Grade list."""

    student_list = SchoolStudent.objects.all()
    grade_bucket = gradeBucket(student_list)

    output_stringIO = StringIO.StringIO() #Used to write to files then zip
    
    with zipfile.ZipFile(output_stringIO, 'w') as zipf: 
        for grade in range(8, 13):
            #with open('Grade'+str(grade)+'individuals.txt', 'w') as temp_file:
            output_string = StrIO.StringIO()

            for student in grade_bucket[grade, False, 'ALL']: #Individual students
                s_line = u'%-10s %3s %s; %s, %s\n'%(student.reference, 'SCI', unicode(student.school)[0:10], student.surname, student.firstname[0])
                output_string.write(s_line)
                
            #Generate file from StringIO and write to zip (ensure unicode UTF-* encoding is used)
            zipf.writestr('INDGR%d.PRN'%(grade), output_string.getvalue().encode('utf-8'))
            output_string.close()
            output_string = StrIO.StringIO()
            for student in grade_bucket[grade, True, 'ALL']: #Paired students
                s_line = u'%-10s %3s %s%s %s\n'%(student.reference, 'SCI', unicode(student.school)[0:10], 'Pair / Paar ', student.surname)  
                #TODO: Seems like an error to me... But it's like this in the sample files.
                output_string.write(s_line)
            
            #Generate file from StringIO and write to zip (ensure unicode UTF-* encoding is used)
            zipf.writestr('PRGR%d.PRN'%(grade), output_string.getvalue().encode('utf-8'))
            output_string.close()
    #Generate response and serve file to the user
    response = HttpResponse(output_stringIO.getvalue())
    response['Content-Disposition'] = 'attachment; filename=PRN_files(%s).zip'%(timestamp_now())
    response['Content-Type'] = 'application/x-zip-compressed'
    return response

def update_school_entry_status():
    school_objects = School.objects.all()
    for school_obj in school_objects:
        try:
            responsible_teachers = ResponsibleTeacher.objects.get(school=school_obj)
            school_obj.entered=1 #If a responsible teacher is found; the school has entered
            school_obj.save()
        except exceptions.ObjectDoesNotExist:
            school_obj.entered=0
            school_obj.answer_sheets_emailed = None
            school_obj.save()

def email_school_reports(request, school_list):
    if not views.after_pg(request):
        comp = Competition.objects.all()
        msg = ""
        if comp.count() == 1:
            pg_date = comp[0].prizegiving_date
            msg = datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + " is before prizegiving date: " + str(pg_date) + " 21:00" 
            msg += "<br>"+"Please wait until after the prize giving before sending out the results" 
            msg += " or change the date at: "+"<a href=\"/admin/competition/competition/\">Competition</a>"
        else:
            msg+="Competition hasn't been set at "+"<a href=\"/admin/competition/competition/\">Competition</a>"
        return HttpResponse(msg)
    else:
        text = ""
        successes = []
        errors = []
        for ischool in school_list:
            txt = "(Key %s) %s: \n" % (str(ischool.key), ischool.name.strip())
            if views.has_results(request, ischool):
                bg_email_results(ischool.id)
                successes.append(ischool.name.strip())
            else:
                has_scores = views.has_results(request, ischool)
                teacher_assigned = len(ResponsibleTeacher.objects.filter(school=ischool.id)) > 0
                if not teacher_assigned:
                    txt += "\t- no responsible teacher assigned.\n"
                elif not has_scores:
                    txt += "\t- no students assigned.\n"
                errors.append(txt)
        if len(successes) > 0:
            text += "Attempting to send emails to the following schools: " + ", ".join(successes) + "\n\n"
        if len(errors) > 0:
            text += "Emails will not be sent to the following schools with given reason: \n" + "".join(errors)
        response = HttpResponse(text)
        filename = 'ReportEmailStatus(%s).txt' % (timestamp_now())
        response['Content-Disposition'] = 'attachment; filename=%s' % (filename)
        response['Content-Type'] = 'application/txt'
        return response


def get_school_report_name(school):
    return "UCTMaths_School_Report_%s.pdf" % (unicode(school.name).strip().replace(" ", "_"))

def print_school_reports(request, school_list):
    result = printer_school_report(request, school_list)
    response = HttpResponse(result.getvalue())
    if len(school_list) > 1:
        response['Content-Disposition'] = 'attachment; filename=SchoolsReport(%s).pdf'%(timestamp_now())
    else:
        response['Content-Disposition'] = 'attachment; filename=%s' % (get_school_report_name(school_list[0]))
    response['Content-Type'] = 'application/pdf'
    return response

def printer_school_report(request, school_list=None):
    """ Generate the school report for each school in the query set"""

    html = '' #Will hold rendered templates
    for assigned_school in school_list:
        student_list = SchoolStudent.objects.filter(school = assigned_school)
        grade_bucket = {8:[], 9:[], 10:[], 11:[], 12:[]}
        for igrade in range(8, 13):
            grade_bucket[igrade].extend(student_list.filter(grade=igrade).order_by('reference'))
        responsible_teacher = ResponsibleTeacher.objects.filter(school = assigned_school)
        timestamp = str(datetime.datetime.now().strftime('%d %B %Y at %H:%M'))
        gold_count = student_list.filter(award='G').count()
        merit_count = student_list.filter(award='M').count()
        merit_count = merit_count + student_list.filter(award='MOX').count()
        school_award = student_list.filter(award='OX') | student_list.filter(award='MOX')

        school_award_blurb = 'Congratulations! %s has received '%(unicode(assigned_school))

        if merit_count > 0 or gold_count > 0:
            if gold_count > 0:
                school_award_blurb+='%d Gold award%s'%(gold_count, 's' if gold_count>1 else '')
            if school_award.count() > 0:
                school_award_blurb+='an Oxford Prize for %s %s' % (school_award[0].firstname, school_award[0].surname)
            if (gold_count > 0 or school_award.count() > 0) and merit_count > 0:
                school_award_blurb+=' and '
            if merit_count > 0:
                school_award_blurb+='%d Merit award%s'%(merit_count, 's' if merit_count>1 else '')
        else:
            school_award_blurb = ''
        year = str(datetime.datetime.now().strftime('%Y'))

        if responsible_teacher:
            c = {'type':'Students',
                'timestamp':timestamp,
                'schooln':assigned_school,
                'responsible_teacher':responsible_teacher[0],
                'student_list':grade_bucket,
                'entries_open':isOpen(),
                'school_award_blurb':school_award_blurb,
                'grade_range':range(8,13),
                'year':year}
            #Render the template with the context (from above)

            template = get_template('school_report.html')
            c.update(csrf(request))
            context = Context(c)
            html += template.render(context) #Concatenate each rendered template to the html "string"

    result = StringIO.StringIO()
    #Generate the pdf doc
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result, encoding='UTF-8')
    if not pdf.err:
        return result
    else:
        pass #Error handling?

def multi_reportgen(request, school_list):
    output_stringIO = StringIO.StringIO() #Used to write to files then zip

    with zipfile.ZipFile(output_stringIO, 'w') as zipf:
        for ischool in school_list:
            output_string=printer_school_report(request, [ischool])
            zipf.writestr('UCTMaths_Report_%s.pdf'%(ischool.name), output_string.getvalue())

    response = HttpResponse(output_stringIO.getvalue())
    if len(school_list) == 1:
        response['Content-Disposition'] = 'attachment; filename=%s' % (get_school_report_name(ischool))
        response['Content-Type'] = 'application/pdf'
    else:
        response['Content-Disposition'] = 'attachment; filename=SchoolReports(%s).zip'%(timestamp_now())
        response['Content-Type'] = 'application/x-zip-compressed'
    return response


def certificate_list(request, school_list):
    #Calculate number of gold, merit and participation certificates per school
    output_workbook = xlwt.Workbook()

    school_list = School.objects.all().filter(entered=1).order_by('name')
    student_list = SchoolStudent.objects.all() #Regardless of admin UI selection

    wb_sheet = output_workbook.add_sheet('Certificate List')
    wb_sheet.write(1, 0, 'Certificates by school:')
    header = ['School', 'Gold', 'Merit', 'Participation', 'Total Participated']
    for i, h in enumerate(header):
        wb_sheet.write(2, i, '%s' %h)
    offset = 3
    index = 0
    gold_total = 0
    merit_total = 0
    part_total = 0
    all_total = 0
    for school in school_list:
        ind_g = student_list.filter(school=school, paired=False, award='G')
        pair_g = student_list.filter(school=school, paired=True, award='G')
        ind_m = student_list.filter(school=school, paired=False, award__contains='M')
        pair_m = student_list.filter(school=school, paired=True, award__contains='M')
        ind_all = student_list.filter(school=school, paired=False, score__gt=0)
        pair_all = student_list.filter(school=school, paired=True, score__gt=0)

        gold_num = len(ind_g) + (len(pair_g) * 2)
        merit_num = len(ind_m) + (len(pair_m) * 2)
        part_num = len(ind_all) + (len(pair_all) * 2) - gold_num - merit_num
        total = gold_num + merit_num + part_num
        gold_total = gold_total + gold_num
        merit_total = merit_total + merit_num
        part_total = part_total + part_num

        wb_sheet.write(index + offset, 0, unicode(school))
        wb_sheet.write(index + offset, 1, gold_num)
        wb_sheet.write(index + offset, 2, merit_num)
        wb_sheet.write(index + offset, 3, part_num)
        wb_sheet.write(index + offset, 4, total)
        index = index + 1

    all_total = gold_total + merit_total + part_total
    offset = offset + 2
    wb_sheet.write(index + offset, 0, 'Total')
    wb_sheet.write(index + offset, 1, gold_total)
    wb_sheet.write(index + offset, 2, merit_total)
    wb_sheet.write(index + offset, 3, part_total)
    wb_sheet.write(index + offset, 4, all_total)
    #Return the response with attached content to the user
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=certificate_list(%s).xls'%(timestamp_now())
    response['Content-Type'] = 'application/ms-excel'
    output_workbook.save(response)
    return response


def get_answer_sheet_name(school):
    return "UCTMaths_Answer_Sheets_%s.pdf" % (unicode(school.name).strip().replace(" ", "_"))

def generate_school_answer_sheets(request, school_list):
    no_venue = []
    no_students = []
    for school in school_list:
        if len(SchoolStudent.objects.filter(school = school)) == 0:
            no_students.append(school.name.strip())
        elif not school_students_venue_assigned(school):
            no_venue.append(school.name.strip())
    print(no_venue,no_students)
    if no_venue or no_students:
        text = "Unable to download answer sheets because:\n\n"
        if no_venue:
            text+="-students at " + ", ".join(no_venue) + " have not been assigned venues.\n"
        if no_students:
            text+="-no students have been registered at "+ ", ".join(no_students)
        response = HttpResponse(text)
        response['Content-Disposition'] = 'attachment; filename=AnswerSheetDownloadErrors(%s).txt'%(timestamp_now())
        response['Content-Type'] = 'application/txt'
        return response
    
    output_stringIO = StringIO.StringIO() #Used to write to files then zip
    start = datetime.datetime.now()
    with zipfile.ZipFile(output_stringIO, 'w') as zipf:
        for ischool in school_list:
            output_string=printer_answer_sheet(request, ischool)
            zipf.writestr(get_answer_sheet_name(ischool), output_string.getvalue())
    
    response = HttpResponse(output_stringIO.getvalue())
    if len(school_list) == 1:
        response['Content-Disposition'] = 'attachment; filename=%s'%(get_answer_sheet_name(school_list[0]))
        response['Content-Type'] = 'application/pdf'
    else:
        response['Content-Disposition'] = 'attachment; filename=Answer_Sheets(%s).zip' % (timestamp_now())
        response['Content-Type'] = 'application/x-zip-compressed'
    diff = datetime.datetime.now() - start
    print(str(diff))
    return response

def get_student_answer_sheet(request, student):
    # Get the text for a single student's answer sheet
    venue = Venue.objects.filter(code = student.venue)[0]
    c = {
        'name':student.firstname + " " + student.surname,
        'school':student.school.name,
        'grade':str(student.grade),
        'code':str(student.reference),
        'venue':str(venue.building)+ ' - '+ str(venue.code),
    }
    if student.paired:
        template = get_template('pair_as_template.html')
    else:
        template = get_template('individual_as_template.html')
    c.update(csrf(request))
    context = Context(c)
    return template.render(context)

def printer_answer_sheet(request, assigned_school=None):
    """ Generate the school answer sheet for each school in the query set"""

    html = '' #Will hold rendered templates
    student_list = SchoolStudent.objects.filter(school = assigned_school)
    for istudent in student_list:
        html += get_student_answer_sheet(request, istudent) #Concatenate each rendered template to the html "string"

    result = StringIO.StringIO()
    #Generate the pdf doc
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result, encoding='UTF-8')
    if not pdf.err:
        return result
    else:
        pass #Error handling?

def venue_assigned(student):
    # Check that the student has a venue allocated
    return len(student.venue) > 0

def school_students_venue_assigned(school):
    # Check that the venue is assigned for all students in this school
    students = SchoolStudent.objects.filter(school=school.id)
    for student in students:
        if not venue_assigned(student):
            return False 
    return len(students)>0

def email_school_answer_sheets(request, schools):
    response = None


    successes = []
    errors = []

    # register a background task to send an email for each school which has venues and a teacher assigned
    for school in schools:
        venues_assigned = school_students_venue_assigned(school)
        teacher_assigned = len(ResponsibleTeacher.objects.filter(school=school.id)) > 0

        if (not venues_assigned) or (not teacher_assigned):
            txt = "(Key %s) %s: \n" % (str(school.key), school.name.strip())
            if not teacher_assigned:
                txt += "\t- no responsible teacher assigned.\n"
            if not venues_assigned:
                txt += "\t- not all students have been assigned venues.\n"
            errors.append(txt)
        else:
            print("Creating background task for %s with ID %d." % (school.name, school.id))
            bg_generate_school_answer_sheets(school.id)
            successes.append(school.name.strip())
    
    
    text = ""
    if len(successes) > 0:
        text += "Attempting to send emails to the following schools: " + ", ".join(successes) + "\n\n"
    if len(errors) > 0:
        text += "Emails will not be sent to the following schools with given reason: \n" + "".join(errors)

    response = HttpResponse(text)
    filename = 'AnswerSheetEmailStatus(%s).txt' % (timestamp_now())
    response['Content-Disposition'] = 'attachment; filename=%s' % (filename)
    response['Content-Type'] = 'application/txt'
    
    return response

def has_invigilator():
    return Competition.objects.all()[0].invigilators

def can_download_answer_sheets():
    return Competition.objects.all()[0].answer_sheet_download_enabled
    
def generate_grade_pdfs(request, schools):
    all_students = SchoolStudent.objects.filter().order_by('school')
    no_venue_assigned = []
    for student in all_students:
        if not venue_assigned(student):
            no_venue_assigned.append("%s(%s)" % (student.firstname + " " + student.surname, student.school.name))
    if no_venue_assigned:
        response = HttpResponse("Unable to generate answer sheets for the following students because no venues were assigned: " + ", ".join(no_venue_assigned))
        response['Content-Disposition'] = 'attachment; filename=AnswerSheetGradeGenerationErrors(%s).txt'%(timestamp_now())
        response['Content-Type'] = 'application/txt'
        return response

    for grade in range(8, 12 + 1):
        print("Creating background task for AS generation for grade %d." % grade)
        bg_generate_as_grade_distinction(grade, True)
        bg_generate_as_grade_distinction(grade, False)
    
    response = HttpResponse("""Attempting to generate answer sheets for all students, distinguished by grade. 
This will take some time if many students have been entered. 
Emails with the answer sheets by grade will be sent to the competition admin's email address(%s) in the next hour.
""" % (admin_emailaddress()))
    response['Content-Disposition'] = 'attachment; filename=AnswerSheetGradeGenerationStatus(%s).txt'%(timestamp_now())
    response['Content-Type'] = 'application/txt'
    return response
