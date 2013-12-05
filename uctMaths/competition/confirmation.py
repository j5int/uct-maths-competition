from django.contrib.auth.decorators import login_required
from competition.models import SchoolStudent, School, Invigilator, Venue 
from django.core.mail import send_mail
import datetime


# Methods for very simple formatting of data entered by a certain user (filter)
# See info in settings.py for SMTP server emulation and set-up

@login_required
def send_confirmation(request):
	""" Formats student information for the particular user and sends it via. smtp"""

	username = request.user #Current user
	student_list = SchoolStudent.objects.filter(registered_by = username)
	invigilator_list = Invigilator.objects.filter(registered_by = username)
	# -- Still need to add 'ResponsibleTeacher' details
	#Header
	output_string = UMC_header()
	output_string += 'Confirmation letter for %s\nRequested by %s\n%s\n'%(student_list[0].school, username, UMC_datetime())

	#Invigilator output list
	output_string += print_invigilators(invigilator_list)
	output_string += print_students(student_list)

	### Debugging - output to file ###
	#temp_output = open('confirmation.txt', 'w')	
	#temp_output.write(temp_output)
	#temp_output.close()	

	### Send mail ###
	send_mail('Confirmation Email', output_string, 'support@sjsoft.com',['hayleym@sjsoft.com'], fail_silently=False)

def print_students(student_list,width=40):
	""" Prints and formats the data for each grade """

	return_string = ''
	#Bins for grouping team and individual participants
	pair_list = { 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0}
	single_list = { 8 : [], 9 : [], 10 : [], 11 : [], 12 : []}

	try:
		#Binning method
		for student in student_list:
			if student.firstname == '': # Better pair condition logic for this!
				pair_list[student.grade] += 1
			else: 
				single_list[student.grade].append((student.firstname, student.surname, student.sex))

	except IndexError: #If the user submitted an empty form
		print 'Index Error (Confirmation email)'
		pass #Report empty list to render?

	# Print out formatted lists for pairs and single participants
	for grade in range(8, 13):	
		grade_string = '\n%s\nGrade %d students (%d registered):\n%s\n'%('-'*width, grade, len(single_list[grade]) + pair_list[grade], '-'*width)
		grade_string += '\n%-15s %-15s %-2s\n%s\n'%('First Name', 'Surname', 'Sex', '- '*int(width/2))

		for single in single_list[grade]:
			grade_string+= '%-15s %-15s %1s\n'%(single[0], single[1], str(single[2].upper()))

		grade_string += '\n%d pairs registered\n'%(pair_list[grade]/2) 

		for pair_register in range(1, pair_list[grade]/2+1):
			grade_string += 'Group %d: \n\n'%(pair_register)

		return_string += grade_string + '\n'

	return return_string #Stored as one long formatted string. 


def print_invigilators(invigilator_list, width=40):
	"""Print invigilator section"""

	#Heading for invigilator section
	invig_string = '\n%s\nInvigilator list \n%s\n'%('-'*width)
	invig_string += '%-10s %-10s %-10s %-10s %-10s\n%s\n'%('First name', 'Surname', 'Phone','(Alternate)', 'Email','-'*width)

	for invigilator in invigilator_list:
		#first, surname, phonenumber (+alt), email_addrs 
		invig_string += '%-10s %-10s %-10s %-10s %-10s\n'%(invigilator.firstname, invigilator.surname, invigilator.phone_primary, invigilator.phone_alt,invigilator.email)

	return invig_string


def UMC_header(width=40):
	""" Text header for email """
	to_return = '%s\n%20s\n\n'%('_'*width,'UCT Mathematics Competition')
	return to_return


def UMC_datetime():
	""" Get/format current time/date of when the submission was passed """ 
	now = datetime.datetime.now()
	to_return = 'Generated %s:%s %s/%s/%s'%(now.hour, now.minute, now.day, now.month, now.year)
	return to_return
