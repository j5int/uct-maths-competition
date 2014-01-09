# Some auxiliary functions and constants for competition
# administration.
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
                #First student of the pair
                studentp1 = grade_bucket[venue.grade, venue.allocated_to_pairs].pop()

                try:
                    #Try find paired student. IndexError if not found
                    for index, possible_pair in enumerate(grade_bucket[venue.grade, venue.allocated_to_pairs]):
                                if possible_pair.reference == studentp1.reference: #Match is found
                                    studentp2 = grade_bucket[venue.grade, venue.allocated_to_pairs].pop(index)

                    #Update both students in the pair
                    studentp1.venue = venue.code
                    studentp2.venue = venue.code

                    studentp1.save()
                    studentp2.save()

                    #Update venue
                    venue.occupied_seats+=2
                    venue.save()

                except IndexError: #Matching reference number (pair partner) can't be found! 
                    #TODO? Serious error here. Notify integrity error to admin?
                    grade_bucket[venue.grade, venue.allocated_to_pairs].append(studentp1)
                    print 'Pairing error!' 

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
                s_line = ''
                s_line += '\"' + str(student.reference) + '\",'
                s_line += '\"' + str(student.firstname) + ' ' + str(student.surname) + '\",'
                s_line += '\"' + str(student.school) +  '\",'
                s_line += str(student.grade) + ','
                venue_str = str(venue_object[0]) if len(venue_object)==1 else 'Unallocated'
                s_line += '\"' + venue_str + '\"\n'
                output_string.write(s_line)
                
            zipf.writestr('Mailmerge_Grade'+str(grade) +'_individuals.txt',output_string.getvalue())

            output_string = StringIO.StringIO()
            for student in grade_bucket[grade, True]: #Paired students in [grade]
                venue_object = [venue for venue in venue_list if venue.code == student.venue]
                s_line = ''
                s_line += '\"' + str(student.reference) + '\",'
                s_line += '\"' + str(student.firstname) + ' ' + str(student.surname) + '\",'
                s_line += '\"' + str(student.school) +  '\",'
                s_line += str(student.grade) + ','
                venue_str = str(venue_object[0]) if len(venue_object)==1 else 'Unallocated'
                s_line += '\"' + venue_str + '\"\n'
                output_string.write(s_line)

            #Generate file from StringIO and write to zip
            zipf.writestr('Mailmerge_Grade'+str(grade) +'_pairs.txt',output_string.getvalue())

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
        s_entry = '\"' + str(school.contact) + '\",'
        s_entry += '\"' + str(school.name) + '\",'
        s_entry += '\"' + str(school.address) + '\"\n'
        output_stringio.write(s_entry)

    #Serve to user as text file
    response = HttpResponse(output_stringio.getvalue())
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


    #TODO: Add logic for two schools having the same score

    
    #Ensure that schools with equal scores are assigned the same rank
    #TODO Needs testing!
    #Generate a list from the schools (so that I can use .pop(0) commands on it)
    school_selection = []
    for s in all_schools:
        school_selection.append(s)

    rank_base = 1
    rank_delta = 0
    
    while school_selection: #while the list is not empty

        rank_base = rank_base + rank_delta
        
        school = school_selection.pop(0)
        school.rank = rank_base
        current_score = school.score
        school.save()
        
        rank_delta = 1
        #Assign all schools with the same score the same rank
        #Use the rank_delta as a ticket
        while school_selection and school_selection[0].score == current_score: 
            school = school_selection.pop(0)
            school.rank = rank_base
            rank_delta = rank_delta + 1
            school.save()

#TODO
def assign_awards(student_list):
    """ Assign awards to participants (QuerySet is list of students) to students based on their rank. Serves an excel workboow with the awards for each student."""
    pass

#TODO
def rank_students(student_list):
    """Rank students on their uploaded score. Used if a score has been changed and the remaining students need to be re-classified"""
    pass
