# Some auxiliary functions and constants for competition
# administration.
from __future__ import unicode_literals
from competition.models import SchoolStudent, School, Invigilator, Venue, ResponsibleTeacher, Competition
from datetime import date
import operator
import glob
import csv
import xlwt
import os
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse, HttpResponseRedirect
import zipfile
import StringIO
import datetime
from django.core import exceptions 
import views
#A few administration constants and associated methods to be used around the website.

from django.core.context_processors import csrf
from reportlab.pdfgen import canvas
import ho.pisa as pisa
import StringIO as StrIO
import cStringIO as StringIO
from django.template.loader import get_template
from django.template import loader, Context
from django.template import RequestContext


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
    """ Sort ("bucket") QuerySet (a list of students) into a dict with key based on (grade (integer), pairing status.
    Simplifies sorting/accessor logic base on entity. ie. [student.grade, student.pair] or [venue.grade, venue.allocated_to_pairs] """

    grade_bucket = { #(grade (integer), is_paired (boolean))
                     (8, True) : [], (8, False) : [],
                     (9, True) : [], (9, False) : [],
                     (10, True) : [], (10, False) : [],
                     (11, True) : [], (11, False) : [],
                     (12, True) : [], (12, False) : []
                    }
    try:
        for student in student_list:
            grade_bucket[student.grade, student.paired].append(student)
    #Empty QuerySet
    except IndexError:
        print 'Index Error'

    return grade_bucket


def auto_allocate(venue_list):
    """ Auto allocates currently unallocated (to avoid double-allocation when QuerySet is a subset of venues) students to the provided QuerySet (a list of venues selected at the admin interface. Grade set to 'None' venues are ignored in the allocation process."""
    venue_deallocate(venue_list)
    student_list = SchoolStudent.objects.all().filter(venue='').order_by('grade') #Order by grade (ASCENDING)

    print len(student_list), ' students are unallocated' #TODO: Error message to user?
    grade_bucket = gradeBucket(student_list)

    venue_list.order_by('-seats') #Order by number of seats, descending.

    for venue in venue_list: 
        #Each venue in QuerySet where grade!=None; while students exist in grade bucket 
        #See method 'grade_bucket' for bucket format (Key is a tuple!)
        while venue.grade and grade_bucket[venue.grade, venue.allocated_to_pairs]:
            #Pair logic
            if venue.occupied_seats < venue.seats - 1 and venue.allocated_to_pairs:
                studentp1 = grade_bucket[venue.grade, venue.allocated_to_pairs].pop()

                #Update both students in the pair
                studentp1.venue = venue.code
                studentp1.save()

                #Update venue
                venue.occupied_seats+=2
                venue.save()

            #Individual logic
            elif venue.occupied_seats < venue.seats and not venue.allocated_to_pairs:
                student = grade_bucket[venue.grade, venue.allocated_to_pairs].pop()
                student.venue = venue.code
                student.save()

                venue.occupied_seats+=1
                venue.save()

            else:
                break

def venue_deallocate(venue_list):
    """ Deallocate students from venues. Clear student.venue and venue.pairs, venue.individuals """
    student_list = SchoolStudent.objects.all().order_by('grade')

    for venue in venue_list:
        venue.occupied_seats=0
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
    #Generate a list of unallocated invigilators and students
    summary_sheet = output_workbook.add_sheet('Venue_summary')
    summary_sheet.write(0,0,'Summary page')

    venue_h = ['Venue', 'Building', 'Grade', 'Available seats', 'Occupied seats','Allocation']

    for index, header in enumerate(venue_h):
        summary_sheet.write(1, index, header)

    venue_list.order_by('grade')

    for v_index, venue in enumerate(venue_list):
        summary_sheet.write(v_index+2,0,str(venue.code))
        summary_sheet.write(v_index+2,1,venue.building)
        summary_sheet.write(v_index+2,2,str(venue.grade))
        summary_sheet.write(v_index+2,3,str(venue.seats))
        summary_sheet.write(v_index+2,4,str(venue.occupied_seats))

        if venue.allocated_to_pairs:
            summary_sheet.write(v_index+2,5,'Pairs')
        else:
            summary_sheet.write(v_index+2,5,'Individuals')

    #TODO?:Print out the unallocated students?


    #Generate a 'Register' sheet for each venue in QuerySet
    #------------------------------------------------------
    for venue in venue_list:
        student_list = SchoolStudent.objects.all().filter(venue=venue.code)
        
        #TODO? Include invigilators in the sheet?
        #invigilator_list = Invigilator.objects.all().filter(venue=venue.code)

        if student_list: #If the list is not empty.
            venue_sheet = output_workbook.add_sheet(str(venue.code))
            venue_header = [ #Heading for each sheet. ie. what this sheet contains (for when it's printed)
                            'Venue:', str(venue.code), 
                            'Building: ', str(venue.building),
                            'Grade:', str(venue.grade),
                            'Occupancy:', str(venue.occupied_seats)+'/'+str(venue.seats),
                            'Allocation:', 'Pairs' if venue.allocated_to_pairs else 'Individuals'
                            ]

            #Print venue_header to the sheet
            for index in range(0,5):
                venue_sheet.write(index,0, venue_header[index*2])
                venue_sheet.write(index,1, venue_header[index*2+1])

            #Print student header (name columns) to sheet
            for h_index, word in enumerate(student_header):
                venue_sheet.write(6,h_index,student_header[h_index])

            #Print the students in that venue to sheet
            for s_index, student in enumerate(student_list):
                venue_sheet.write(s_index+7,0,str(student.reference))
                venue_sheet.write(s_index+7,2,student.firstname)
                venue_sheet.write(s_index+7,3,student.surname)
                venue_sheet.write(s_index+7,1,unicode(student.school))

        else:
            pass #Venue is empty - no point making a sheet for it...
            #print 'Empty venue!'

    #Generate response and serve file to the user
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=venue_register(%s).xls'%(timestamp_now())
    response['Content-Type'] = 'application/ms-excel'
    output_workbook.save(response)
    return response

#Export venue lists to workbook.
#See http://scienceoss.com/write-excel-files-with-python-using-xlwt/

def output_studentlists(student_list):
    """Output 10 lists (SchoolStudent list QuerySet) as sheets on an xls (Paired, Individuals) for each grade"""

    grade_bucket = gradeBucket(student_list)

    output_workbook = xlwt.Workbook()
    student_header = ['School', 'Reference No.', 'First name(s)', 'Surname', 'Venue']

    for grade in range(8, 13):
    
        #Process individual page
        student_sheet = output_workbook.add_sheet('Grade ' + str(grade)+' individuals')

        #Print title and header
        student_sheet.write(0, 0, 'Grade ' + str(grade) + ' individuals')
        for h_index, word in enumerate(student_header):
            student_sheet.write(1,h_index,word)
        #Print each student's details
        for index, student in enumerate(grade_bucket[grade, False]):
            student_sheet.write(index+2,0,unicode(student.school))
            student_sheet.write(index+2,1,str(student.reference))
            student_sheet.write(index+2,2,student.firstname)
            student_sheet.write(index+2,3,student.surname)
            student_sheet.write(index+2,4,student.venue)

        #Process pairs page
        student_sheet = output_workbook.add_sheet('Grade ' + str(grade)+' pairs')
        #Print title and header
        student_sheet.write(0, 0, 'Grade ' + str(grade) + ' pairs')
        for h_index, word in enumerate(student_header):
            student_sheet.write(1,h_index,word)
        #Print each student's details
        for index, student in enumerate(grade_bucket[grade, True]):
            student_sheet.write(index+2,0,unicode(student.school))
            student_sheet.write(index+2,1,str(student.reference))
            student_sheet.write(index+2,2,student.firstname)
            student_sheet.write(index+2,3,student.surname)
            student_sheet.write(index+2,4,student.venue)

    #Generate response and serve file (xls) to user
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=studentlist(%s).xls'%(timestamp_now())
    response['Content-Type'] = 'application/ms-excel'
    output_workbook.save(response)
    return response

def output_studenttags(student_list):
    """Generate MailMerge lists for SchoolStudent QuerySet. Served to user as a .zip file with each (10 files) Paired/Grade list."""

    grade_bucket = gradeBucket(student_list)

    #Generate individuals name tags 
    #Eg: "Ref#","Name Surname","School name",Grade(int),"Building Room(Code)"
    venue_list = Venue.objects.all()
    output_stringIO = StringIO.StringIO() #Used to write to files then zip
    
    with zipfile.ZipFile(output_stringIO, 'w') as zipf: 
        for grade in range(8, 13):
            #with open('Grade'+str(grade)+'individuals.txt', 'w') as temp_file:
            output_string = StrIO.StringIO()
            for student in grade_bucket[grade, False]:
                venue_object = [venue for venue in venue_list if venue.code == student.venue]
                s_line = u''
                s_line += '\"' + student.reference + '\",'
                s_line += '\"' + student.firstname + ' ' + student.surname + '\",'
                s_line += '\"' + unicode(student.school) +  '\",'
                s_line += str(student.grade) + ','
                venue_str = venue_object[0] if len(venue_object)==1 else 'Unallocated'
                s_line += '\"' + str(venue_str) + '\"\n'
                output_string.write(s_line)

            #Generate file from StringIO and write to zip (ensure unicode UTF-* encoding is used)
            zipf.writestr('Mailmerge_GRD'+str(grade) +'_IND.txt',output_string.getvalue().encode('utf-8'))
            output_string.close()
            output_string = StrIO.StringIO()
            for student in grade_bucket[grade, True]: #Paired students in [grade]
                venue_object = [venue for venue in venue_list if venue.code == student.venue]
                s_line = u''
                s_line += '\"' + student.reference + '\",'
                s_line += '\"' + student.firstname + ' ' + student.surname + '\",'
                s_line += '\"' + unicode(student.school) +  '\",'
                s_line += str(student.grade) + ','
                venue_str = venue_object[0] if len(venue_object)==1 else 'Unallocated'
                s_line += '\"' + unicode(venue_str) + '\"\n'
                output_string.write(s_line)

            #Generate file from StringIO and write to zip (ensure unicode UTF-* encoding is used)
            zipf.writestr('Mailmerge_GRD'+str(grade) +'_PAR.txt',output_string.getvalue().encode('utf-8'))
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

#Called by admin to generate formatted 'tag list' for selected schools
def output_schooltaglists(school_list):
    """ Generate the tags for a School QuerySet. Served as a single text file in HttpResponse. """

    output_stringio = StringIO.StringIO()

    #Generate and format school entry (as in spec. sheet)
    for school in school_list:
        s_entry = '\"' + school.contact + '\",'
        s_entry += '\"' + unicode(school.name) + '\",'
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
    
#TODO
def rank_schools(school_list):
    """ Ranks schools based on a sum of the top X scores. X is set via the 'Competition' form. """
    comp = Competition.objects.all() #Should only be one!
    
    if comp.count() == 1:
        top_score_candidates = comp[0].num_schoolcandidate_scores
    else:
        num_schoolcandidate_scores = 0
        
    all_schools = School.objects.all()

    #Calculate total scores for all schools
    for school in all_schools:
        #Get ONLY the candidates from that school and order by score DESCENDING
        #FIXME ?: These DB operations just wouldn't work with the distinct command. Using less efficient python-lists methods
        #candidates = SchoolStudent.objects.order_by('reference').distinct('reference')#.filter(school=school).exclude(score=None)
        #candidates = candidates.order_by('-score')
        
        candidatesQS = SchoolStudent.objects.filter(school=school).exclude(score=None).order_by('-score')
        #Remove pairs (duplicate REF numbers)
        candidates = []
        
        #Pretty sloppy way of doing it. Need to be able to remove a C from list without affecting DB record
            #Couldn't find a method in QuerySet API

        for c in candidatesQS:
            #print c.firstname, c.surname, c.score
            candidates.append(c)
            
        for c in candidates:
            for index, p in enumerate(candidates):
                if p.paired and c.paired and p.reference == c.reference: #Match is found
                    candidates.pop(index)

        #Calculate schools' total scores
        total_score = 0
        #Sum candidates scores (already sorted in descending order)
        for i, c in enumerate(candidates):
            #print i, c.firstname, c.surname, c.score
            if i < top_score_candidates:
                total_score = total_score + c.score
        #print school.name, total_score
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
        current_score = student.score
        student.save()
        
        rank_delta = 1
        #Assign all schools with the same score the same rank
        #Use the rank_delta as a counter
        while student_selection and student_selection[0].score == current_score: 
            student = student_selection.pop(0)
            student.rank = rank_base
            rank_delta = rank_delta + 1
            student.save()


def assign_awards(request, student_list):
    """ Assign awards to participants (QuerySet is list of students) to students based on their rank. Serves an excel workboow with the awards for each student."""
    output_workbook = xlwt.Workbook()
    #Ranked gold for each grade (pairs, individuals separated) (alphabetical by surname)
    #Alphabetical list of school award winners
    #Generate gold-awards list (Top 10 individuals, top 3 pairs)

    school_list = School.objects.all()
    student_list = SchoolStudent.objects.all() #Regardless of admin UI selection

    for igrade in range(8, 13):
        #Gold awards
        wb_sheet = output_workbook.add_sheet('Gold Grade %d'%(igrade))
        #Generate QuerySets for GOLD medal winners (sorted by rank (descnding))
        pairQS = student_list.filter(grade = igrade, paired=True, rank__lt=4).order_by('rank')
        individualQS = student_list.filter(grade = igrade, paired=False, rank__lt=11).order_by('rank')
        pairs_offset = 4 #Using an offset accounts for situations where more than 10 people are getting gold (ties at rank=10)

        wb_sheet.write(1,0,'Gold award winners: Grade %d individuals'%(igrade))
        pairs_offset = pairs_offset + 1

        for index, individual in enumerate(individualQS):
            wb_sheet.write(index+2,0,str(individual.rank))
            wb_sheet.write(index+2,1,unicode(individual.school))
            wb_sheet.write(index+2,2,str(individual.reference))
            wb_sheet.write(index+2,3,individual.firstname)
            wb_sheet.write(index+2,4,individual.surname)
            school_list=school_list.exclude(name=individual.school) #Exclude school for Oxford prize
            pairs_offset = pairs_offset + 1
        
        wb_sheet.write(pairs_offset,0,'Gold award winners: Grade %d pairs'%(igrade))
        pairs_offset = pairs_offset + 1
        for index, pair in enumerate(pairQS):
            wb_sheet.write(index+pairs_offset,0,str(pair.rank))
            wb_sheet.write(index+pairs_offset,1,unicode(pair.school))
            wb_sheet.write(index+pairs_offset,2,str(pair.reference))
            wb_sheet.write(index+pairs_offset,3,pair.firstname)
            wb_sheet.write(index+pairs_offset,4,pair.surname)
            school_list=school_list.exclude(name=pair.school) #Exclude school for Oxford prize

        #Merit awards
        wb_sheet = output_workbook.add_sheet('Merit Grade %d'%(igrade))
        #Generate QuerySets for MERIT medal winners (sorted by school0 (name descending))
        pairQS = student_list.filter(grade = igrade, paired=True, rank__lt=101, rank__gt=4).order_by('school')
        individualQS = student_list.filter(grade = igrade, paired=False, rank__lt=201, rank__gt=10).order_by('school')
        pairs_offset = 4 #Using an offset accounts for situations where more than 10 people are getting merit (ties at rank=200)

        wb_sheet.write(1,0,'Merit award winners: Grade %d individuals'%(igrade))
        pairs_offset = pairs_offset + 1
        for index, individual in enumerate(individualQS):
            #wb_sheet.write(index+2,0,str(individual.rank))
            wb_sheet.write(index+2,1,unicode(individual.school))
            wb_sheet.write(index+2,2,str(individual.reference))
            wb_sheet.write(index+2,3,individual.firstname)
            wb_sheet.write(index+2,4,individual.surname)
            pairs_offset = pairs_offset + 1
        
        wb_sheet.write(pairs_offset,0,'Merit award winners: Grade %d pairs'%(igrade))
        pairs_offset = pairs_offset + 1
        for index, pair in enumerate(pairQS):
            #wb_sheet.write(index+pairs_offset,0,str(pair.rank))
            wb_sheet.write(index+pairs_offset,1,unicode(pair.school))
            wb_sheet.write(index+pairs_offset,2,str(pair.reference))
            wb_sheet.write(index+pairs_offset,3,pair.firstname)
            wb_sheet.write(index+pairs_offset,4,pair.surname)

    #TODO Oxford prizes. 
    #School awards (Oxford prizes) are assigned to the top individual in each school where the school did not receive an individual or pair Gold award
    wb_sheet = output_workbook.add_sheet('Oxford prizes (School Award)')
    award_winners = []
    
    for school in school_list:
        #Get the students from the eligible school, order by score (descending)
        school_students = SchoolStudent.objects.filter(school=school).order_by('-score')
        
        #The award winner  is that with the highest score at the school
        if school_students and school_students[0].score:
            award_winners.append(school_students[0])

    wb_sheet.write(0,0,'Oxford School award')
    for index, aw in enumerate(award_winners):
        wb_sheet.write(index+1,1,unicode(aw.school))
        wb_sheet.write(index+1,2,str(aw.reference))
        wb_sheet.write(index+1,3,aw.firstname)
        wb_sheet.write(index+1,4,aw.surname)

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
        school_students = SchoolStudent.objects.filter(school=ischool).order_by('-score')
        
        #The award winner  is that with the highest score at the school
        if school_students and school_students[0].score:
            if school_students[0].award is None:
                school_students[0].award = ''
            school_students[0].award=school_students[0].award+'OX'
            school_students[0].save()

def school_summary(request):
    """ Return for DL a summary list of all the schools that have made an entry; also create a "email these people" line with all the relevant emai adresses. Or something like that."""

    output_workbook = xlwt.Workbook()
    school_list = School.objects.all().order_by('name') #ie. regardless of selection at admin screen
    
    wb_sheet = output_workbook.add_sheet('School Summary')
    school_summary_sheet(school_list, wb_sheet)
    
    wb_sheet = output_workbook.add_sheet('School Ranking Summary')
    school_rank = school_list.order_by('-rank')
    school_summary_sheet(school_list, wb_sheet, rank_extend=True)

    #Return the response with attached content to the user
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=school_summary(%s).xls'%(timestamp_now())
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

    header = ['School', 'Resp. Teach Name', 'Resp. Teach. Email', 'Individuals', 'Pairs', 'Total']
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
            school_summary_info = [] #Entry for each grade
            count_individuals = 0
            count_pairs = 0

            for i in range(8,13):
                count_pairs = count_pairs + len(grade_summary[i,True])
                count_individuals = count_individuals + len(grade_summary[i,False])

            cell_row_offset = cell_row_offset + 1
            wb_sheet.write(cell_row_offset,0,unicode(school_obj.name))
            wb_sheet.write(cell_row_offset,1,('%s %s')%(resp_teacher.firstname, resp_teacher.surname))
            wb_sheet.write(cell_row_offset,2,resp_teacher.email)
            wb_sheet.write(cell_row_offset,4,count_pairs)
            wb_sheet.write(cell_row_offset,3,count_individuals)
            wb_sheet.write(cell_row_offset,5,int(count_pairs*2 + count_individuals))
            if rank_extend:
                wb_sheet.write(cell_row_offset,6,school_obj.rank)
                wb_sheet.write(cell_row_offset,7,school_obj.score)

            responsible_teacher_mailinglist.append(resp_teacher.email)
    
    wb_sheet.write(3,0,'Mailing list')
    wb_sheet.write(3,1,', '.join(responsible_teacher_mailinglist))
    return wb_sheet

def archive_all_students(student_list, wb_sheet):
    """ Helper function to export_entire_competition."""

    wb_sheet.write(0,0,'Student summary sheet')
    wb_sheet.write(1,0,'Generated')
    wb_sheet.write(1,1,'%s'%(timestamp_now()))

    header = ['Reference', 'School' , 'Firstname', 'Surname', 'Grade', 'Score', 'Rank', 'Award','Language']

    cell_row_offset = 3

    for index, h in enumerate(header):
        wb_sheet.write(cell_row_offset,index,'%s'%(h))
    
    cell_row_offset = cell_row_offset + 1
    student_lang = {'b':'Bilingual', 'a':'Afrikaans', 'e':'English'}
    
    for student in student_list:#print details for every student on the list
        wb_sheet.write(cell_row_offset,1,unicode(student.school))
        wb_sheet.write(cell_row_offset,0, student.reference)
        wb_sheet.write(cell_row_offset,2, student.firstname)
        wb_sheet.write(cell_row_offset,3, student.surname)
        wb_sheet.write(cell_row_offset,4, student.grade)
        wb_sheet.write(cell_row_offset,5, student.score)
        wb_sheet.write(cell_row_offset,6, student.rank)
        wb_sheet.write(cell_row_offset,7, student.award)
        wb_sheet.write(cell_row_offset,8, student_lang[student.language])
        cell_row_offset = cell_row_offset + 1

    return wb_sheet
    
def archive_all_invigilators(invigilator_list, wb_sheet):
    """ Helper function to export_err'thing."""
    wb_sheet.write(0,0,'Invigilator summary sheet')
    wb_sheet.write(1,0,'Generated')
    wb_sheet.write(1,1,'%s'%(timestamp_now()))

    header = ['School' , 'Firstname', 'Surname', 'Phone Primary', 'Alternate', 'Email']
    cell_row_offset = 3

    for index, h in enumerate(header):
        wb_sheet.write(cell_row_offset,index,'%s'%(h))
    
    cell_row_offset = cell_row_offset + 1
    
    for invigilator in invigilator_list:#Print details for all invigilators on the list
        wb_sheet.write(cell_row_offset,0,unicode(invigilator.school))
        wb_sheet.write(cell_row_offset,1, invigilator.firstname)
        wb_sheet.write(cell_row_offset,2, invigilator.surname)
        wb_sheet.write(cell_row_offset,3, invigilator.phone_primary)
        wb_sheet.write(cell_row_offset,4, invigilator.phone_alt)
        wb_sheet.write(cell_row_offset,5, invigilator.email)
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

            for student in grade_bucket[grade, False]:#Individual students
                s_line = u'%-10s %3s %s; %s, %s\n'%(student.reference, 'SCI', unicode(student.school)[0:10], student.surname, student.firstname[0])
                output_string.write(s_line)
                
            #Generate file from StringIO and write to zip (ensure unicode UTF-* encoding is used)
            zipf.writestr('INDGR%d.PRN'%(grade), output_string.getvalue().encode('utf-8'))
            output_string.close()
            output_string = StrIO.StringIO()
            for student in grade_bucket[grade, True]: #Paired students
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
            school_obj.save()

def print_school_reports(request, school_list):
    result = printer_school_report(request, school_list)
    response = HttpResponse(result.getvalue())
    response['Content-Disposition'] = 'attachment; filename=SchoolsReport(%s).pdf'%(timestamp_now())
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
        timestamp = str(datetime.datetime.now().strftime('%d %B %Y at %H:%M (local time)'))
        gold_count = student_list.filter(award='G').count()
        merit_count = student_list.filter(award='M').count()
        merit_count = merit_count + student_list.filter(award='MOX').count()

        school_award_blurb = 'Congratulations. %s has received '%(unicode(assigned_school))

        if merit_count > 0 or gold_count > 0:
            if gold_count > 0:
                school_award_blurb+='%d Gold award%s'%(gold_count, 's' if gold_count>1 else '')
            if gold_count and merit_count:
                school_award_blurb+=' and '
            if merit_count > 0:
                school_award_blurb+='%d Merit award%s'%(merit_count, 's' if gold_count>1 else '')
        else:
            pass #TODO:Congratualte school prize winner instead?

        if responsible_teacher:
            c = {'type':'Students',
                'timestamp':timestamp,
                'schooln':assigned_school,
                'responsible_teacher':responsible_teacher[0],
                'student_list':grade_bucket,
                'entries_open':isOpen(),
                'school_award_blurb':school_award_blurb,
                'grade_range':range(8,13),}
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
    response['Content-Disposition'] = 'attachment; filename=SchoolReports(%s).zip'%(timestamp_now())
    response['Content-Type'] = 'application/x-zip-compressed'
    return response

