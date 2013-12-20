# Some auxiliary functions and constants for competition
# administration.
from competition.models import SchoolStudent, School, Invigilator, Venue, ResponsibleTeacher 
from datetime import date
import operator


#A few administration constants and associated methods to be used around the website.

#The date until which entries are accepted
comp_closingdate=date(2013, 12, 21) #(YYYY, MM, DD) format
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
def auto_allocate():
    print 'auto_allocate'
    venue_deallocate()
    student_list = SchoolStudent.objects.all().order_by('grade') #Order by grade (ASCENDING)
    venue_list = Venue.objects.all().order_by('-seats') #Order by seats (DECENDING)

    grade_bucket = gradeBucket(student_list)

#   For each venue
    #calculate the "most filling" grade
    #If two are equal, take the grade with the most students left
    fullness = {8:1.0, 9:1.0, 10:1.0, 11:1.0, 12:1.0}

    for venue in venue_list:
        
        for key in range(8,13): #Better logic for choosing venues?
            fullness[key] = len(grade_bucket[key])

        #Find grade that maximises the use of the venue
        max_key = max(fullness.iteritems(), key=operator.itemgetter(1))[0]

        #Pop students until the bucket is empty or the venue is full
        while grade_bucket[max_key] and venue.pairs*2+venue.individuals < venue.seats:
            #TODO: Handle keeping-pairs-together
            student = grade_bucket[max_key].pop(0) #Better logic here!

            if student.paired: #find the second of the pair
                if venue.pairs*2+venue.individuals < venue.seats-1:#Fit both of the pair?
                    
                    try:
                        #try find the other student of the pair (match reference number)
                        for index, possible_pair in enumerate(grade_bucket[max_key]):
                            if possible_pair.reference == student.reference: #Match is found
                                paired_student = grade_bucket[max_key].pop(index)

                        if paired_student: #Paired student found. Save the pair
                            paired_student.venue = venue.code
                            student.venue = venue.code
                            paired_student.save()
                            student.save()
                            venue.pairs += 1
                        else: #This is a DB error! No matching pair found
                            print 'Pair error!'
                            
                    except IndexError:
                        print '[Pair error]'

                else: #Not enough seats to accomodate the pair
                    grade_bucket[max_key].append(student) #(Assumption - an individual in the queue?)
                    if sum(1 for indiv in grade_bucket[max_key] if not indiv.paired) == 0:
                        break #Avoid .append-induced infinite loop
            else:
                student.venue = venue.code
                venue.individuals += 1
                student.save()

        venue.grade = max_key
        venue.save()
        #ENDFOR (Loop iterates over all venues, despite having no more students to allocate)

    #Check to see if there are too many students
    remaining_students = sum(len(grade_bucket[grade]) for grade in range(8,13))

    if  remaining_students != 0:
        print remaining_students, ' unassigned students! Grade breakdown:', [len(grade_bucket[grade]) for grade in range(8,13)] #Display message to interface?

def venue_deallocate():
    """ Deallocate students from venues. Clear student.venue and venue.pairs, venue.individuals """
    student_list = SchoolStudent.objects.all().order_by('grade')
    venue_list = Venue.objects.all().order_by('-seats') #Order by seats (DECENDING)

    for student in student_list:
        student.venue = ''
        student.save()

    for venue in venue_list:
        venue.pairs = 0
        venue.individuals = 0
        venue.save()

#Would this be more/less efficient than query-based binning?
# I need to be able to access length of list, each student's details.
def gradeBucket(student_list):
    grade_bucket = { 8 : [] , 9 :  [] , 10 :  [] , 11 : [] , 12 : [] }
    try:
        for student in student_list:
            grade_bucket[student.grade].append(student)
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

