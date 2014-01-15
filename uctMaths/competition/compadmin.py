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

#A few administration constants and associated methods to be used around the website.

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
        summary_sheet.write(v_index+2,1,str(venue.building))
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
                venue_sheet.write(s_index+7,2,str(student.firstname))
                venue_sheet.write(s_index+7,3,str(student.surname))
                venue_sheet.write(s_index+7,1,str(student.school))

        else:
            pass #Venue is empty - no point making a sheet for it...
            #print 'Empty venue!'

    #Generate response and serve file to the user
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=venue_register.xls'
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
            student_sheet.write(index+2,0,str(student.school))
            student_sheet.write(index+2,1,str(student.reference))
            student_sheet.write(index+2,2,str(student.firstname))
            student_sheet.write(index+2,3,str(student.surname))
            student_sheet.write(index+2,4,str(student.venue))

        #Process pairs page
        student_sheet = output_workbook.add_sheet('Grade ' + str(grade)+' pairs')
        #Print title and header
        student_sheet.write(0, 0, 'Grade ' + str(grade) + ' pairs')
        for h_index, word in enumerate(student_header):
            student_sheet.write(1,h_index,word)
        #Print each student's details
        for index, student in enumerate(grade_bucket[grade, True]):
            student_sheet.write(index+2,0,str(student.school))
            student_sheet.write(index+2,1,str(student.reference))
            student_sheet.write(index+2,2,str(student.firstname))
            student_sheet.write(index+2,3,str(student.surname))
            student_sheet.write(index+2,4,str(student.venue))

    #Generate response and serve file (xls) to user
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=studentlist.xls'
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
            output_string = StringIO.StringIO()

            for student in grade_bucket[grade, False]:
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
            zipf.writestr('Mailmerge_Grade'+str(grade) +'_individuals.txt',output_string.getvalue().encode('utf-8'))

            output_string = StringIO.StringIO()
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
            zipf.writestr('Mailmerge_Grade'+str(grade) +'_pairs.txt',output_string.getvalue().encode('utf-8'))

    #Generate response and serve file to the user
    response = HttpResponse(output_stringIO.getvalue())
    response['Content-Disposition'] = 'attachment; filename=mailmergestudents.zip'
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
    response['Content-Disposition'] = 'attachment; filename=schooltags.txt'
    return response

def upload_results(request, student_list):
    """Facilitate upload of .RES (the results) files. Redirects to custom Admin page (upload_results.html), the logic contained in compadmin_views.py."""
    #Return response of redirect page
    response = HttpResponseRedirect('/competition/admin/upload_results.html')
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
    all_students = SchoolStudent.objects.all().exclude(score=None).order_by('-score')

    #Ensure that students with equal scores are assigned the same rank
    #Generate a list from the students (so that I can use .pop(0) commands on it)
    student_selection = []
    for s in all_students:
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
            wb_sheet.write(index+2,1,str(individual.school))
            wb_sheet.write(index+2,2,str(individual.reference))
            wb_sheet.write(index+2,3,str(individual.firstname))
            wb_sheet.write(index+2,4,str(individual.surname))
            school_list=school_list.exclude(name=individual.school) #Exclude school for Oxford prize
            pairs_offset = pairs_offset + 1
        
        wb_sheet.write(pairs_offset,0,'Gold award winners: Grade %d pairs'%(igrade))
        pairs_offset = pairs_offset + 1
        for index, pair in enumerate(pairQS):
            wb_sheet.write(index+pairs_offset,0,str(pair.rank))
            wb_sheet.write(index+pairs_offset,1,str(pair.school))
            wb_sheet.write(index+pairs_offset,2,str(pair.reference))
            wb_sheet.write(index+pairs_offset,3,str(pair.firstname))
            wb_sheet.write(index+pairs_offset,4,str(pair.surname))
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
            wb_sheet.write(index+2,1,str(individual.school))
            wb_sheet.write(index+2,2,str(individual.reference))
            wb_sheet.write(index+2,3,str(individual.firstname))
            wb_sheet.write(index+2,4,str(individual.surname))
            pairs_offset = pairs_offset + 1
        
        wb_sheet.write(pairs_offset,0,'Merit award winners: Grade %d pairs'%(igrade))
        pairs_offset = pairs_offset + 1
        for index, pair in enumerate(pairQS):
            #wb_sheet.write(index+pairs_offset,0,str(pair.rank))
            wb_sheet.write(index+pairs_offset,1,str(pair.school))
            wb_sheet.write(index+pairs_offset,2,str(pair.reference))
            wb_sheet.write(index+pairs_offset,3,str(pair.firstname))
            wb_sheet.write(index+pairs_offset,4,str(pair.surname))

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
        wb_sheet.write(index+1,1,str(aw.school))
        wb_sheet.write(index+1,2,str(aw.reference))
        wb_sheet.write(index+1,3,str(aw.firstname))
        wb_sheet.write(index+1,4,str(aw.surname))

    #Return the response with attached content to the user
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=awardlist.xls'
    response['Content-Type'] = 'application/ms-excel'
    output_workbook.save(response)
    return response
