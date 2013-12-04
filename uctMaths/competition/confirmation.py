from django.contrib.auth.decorators import login_required
from competition.models import SchoolStudent, School, Invigilator, Venue 
from django.core.mail import send_mail
import datetime

@login_required
def send_confirmation(request):
	""" Formats student information for the particular user """

	username = request.user #Current user
	studentOptions = SchoolStudent.objects.filter(registered_by = username)
					#Gets all the students who were registered by current user

	pair_list = { 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0}
 	individual_list = { 8 : [], 9 : [], 10 : [], 11 : [], 12 : []}
 	
	try:	
		for student in studentOptions:
		
			if student.firstname == '': # Better pair condition logic for this!
				pair_list[student.grade] += 1
		
			else: #Store individual in grade bin
				individual_list[student.grade].append((student.firstname, student.surname))

		output_string = UMC_header()
		output_string += 'Confirmation letter for %s\nRequested by %s\n%s\n'%(studentOptions[0].school, username, UMC_datetime())
   		
		output_string = output_string + print_grade(individual_list, pair_list)	
		
		### Debugging - output to file ###
		#temp_output = open('confirmation.txt', 'w')	
		#temp_output.write(temp_output)
		#temp_output.close()	
		
		### Send mail ###
		send_mail('Confirmation Email', output_string, 'support@sjsoft.com',['hayleym@sjsoft.com'], fail_silently=False)	
	
	except IndexError: #If the user submitted an empty form
		pass #handle error?
				

def print_grade(single_list, pair_list,width=40):
	""" Prints and formats the data for each grade """

	return_string = ''
	
	for grade in range(8, 13):	
		grade_string = '\n%s\nGrade %d students (%d registered):\n%s\n'%('-'*width, grade, len(single_list[grade]) + pair_list[grade], '-'*width)
		grade_string += '\n%-15s %-15s \n%s\n'%('First Name', 'Surname', '- '*int(width/2))
		
		for single in single_list[grade]:
			grade_string+= '%-15s %-15s\n'%(single[0], single[1])
		
		grade_string += '\n%d pairs registered\n'%(pair_list[grade]/2) 
		
		for pair_register in range(1, pair_list[grade]/2+1):
			grade_string += 'Group %d: \n %s %s \n %s %s\n'%(pair_register, '_'*12, '_'*12, '_'*12, '_'*12)

		return_string += grade_string + '\n'		

	return return_string #Stored as one long formatted string. 

def UMC_header(width=40):
	""" Title for email """
	to_return = '%s\n%20s\n\n'%('_'*width,'UCT Mathematics Competition')
	return to_return


def UMC_datetime():
	""" Get/format current time/date of when the submission was passed """ 
	now = datetime.datetime.now()
	to_return = 'Generated %s:%s %s/%s/%s'%(now.hour, now.minute, now.day, now.month, now.year)
	return to_return
