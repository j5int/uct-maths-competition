# Some auxiliary functions and constants for competition
# administration.
from competition.models import SchoolStudent, School, Invigilator, Venue, ResponsibleTeacher 
from datetime import date
import operator


#A few administration constants and associated methods to be used around the website.

#The date until which entries are accepted
comp_closingdate=date(2014, 12, 21) #(YYYY, MM, DD) format
#The date of prizegiving
comp_prizegivingdate=date(2013, 12,13 ) #(YYYY, MM, DD) format

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
def auto_allocate(venue_list):
    """ Auto allocates unallocated students to the provided venue_list """

    venue_deallocate(venue_list)
    student_list = SchoolStudent.objects.all().filter(venue='').order_by('grade') #Order by grade (ASCENDING)

    print len(student_list), ' students are unallocated'
    grade_bucket = gradeBucket(student_list)

    venue_list.order_by('-seats') #Order by number of seats, descending.

    for venue in venue_list:

        while grade_bucket[venue.grade, venue.allocated_to_pairs]:
            if venue.occupied_seats < venue.seats - 1 and venue.allocated_to_pairs: #enough space for the pair

                studentp1 = grade_bucket[venue.grade, venue.allocated_to_pairs].pop()

                try:
                    for index, possible_pair in enumerate(grade_bucket[venue.grade, venue.allocated_to_pairs]):
                                if possible_pair.reference == studentp1.reference: #Match is found
                                    studentp2 = grade_bucket[venue.grade, venue.allocated_to_pairs].pop(index)
                    studentp1.venue = venue.code
                    studentp2.venue = venue.code

                    studentp1.save()
                    studentp2.save()

                    venue.occupied_seats+=2
                    venue.save()

                except IndexError: #Matching reference number (pair partner) can't be found! Serious error here.
                    grade_bucket[venue.grade, venue.allocated_to_pairs].append(studentp1)
                    print 'Pairing error!' 

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

#Would this be more/less efficient than query-based binning?
# I need to be able to access length of list, each student's details.
def gradeBucket(student_list):
    grade_bucket = { #(grade, is_paired) tuple as a key
                     (8, True) : [], (8, False) : [],
                     (9, True) : [], (9, False) : [],
                     (10, True) : [], (10, False) : [],
                     (11, True) : [], (11, False) : [],
                     (12, True) : [], (12, False) : []
                    }
    try:
        for student in student_list:
            grade_bucket[student.grade, student.paired].append(student)
    except IndexError:
        print 'Index Error'
    return grade_bucket

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

