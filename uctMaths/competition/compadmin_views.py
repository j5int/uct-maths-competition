# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import loader, Context
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django import forms
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from competition.forms import StudentForm, SchoolForm, InvigilatorForm, ResponsibleTeacherForm, UploadResultsForm
from competition.models import SchoolStudent, School, Invigilator, Venue, ResponsibleTeacher
from django.contrib.auth.models import User
#from django.contrib.contenttypes import *
from django.db import connection
from django.core import exceptions
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError

import confirmation
import compadmin

import csv

@login_required
def upload_results(request):
    """ Handle upload files from the user. Bound to the upload_results.html admin page."""

    handler_output=[]#Sent to html template for feedback to user

    #Once the user has pressed 'Submit'
    if request.method == 'POST':
        #a=request.POST
        try: #Try receive file from 'Submit' post from user
            form = UploadResultsForm(request.POST, request.FILES)
            handler_output = handle_uploaded_file(request.FILES['upload_file'])
        except MultiValueDictKeyError:#If the user just spams the 'Submit' button without selecting file
            handler_output = ['Please select a valid .RES file from your computer by clicking the \'Browse...\' button']

        if not handler_output: #No errors have occured
            handler_output = [
                            'No errors occured while importing results.', 
                            'Please double check that all students in the database have been updated in the SchoolStudents tab'
                            ]
    #Present UploadResultsForm (defined in forms.py)
    fileUpload = UploadResultsForm()

    if not handler_output:
        handler_output = ['Please select a file to upload']

    #Present upload form and handler message (prompt for input/errors text) to the user
    c = {'fileUpload' : fileUpload, 'handler_output' : handler_output}
    c.update(csrf(request))

    return render_to_response('admin/upload_results.html', c, context_instance=RequestContext(request))


def handle_uploaded_file(inputf):
    """ Handle input .RES file and return any errors to calling function (ie. return a string to be used in template) """

    #TODO Better file format checking!
    if '.RES' not in inputf.name:
        return ['Incorrect file format provided.']

    #Find student based on reference number.
#    student_list = Student.objects.all()

    # Pairs require separate logic
#------------------------------------------------#
    if 'PR' in inputf.name:
        pair_logic = True
    elif 'IND' in inputf.name:
        pair_logic = False
    else:
        return ['Input filename error. Please ensure that the file name contains PR or IND so that pair or individual (respectively) results import can ocur.']
 #------------------------------------------------#

    input_fstring=''
    #Chunks for handling larger files - will essentially just have a long string of char's after this
    for chunk in inputf.chunks():
        input_fstring += chunk

    #Format for INIDIVIDUALS is (INDGR in filename):
    #"ReferenceN [0]      ","ENG", "School; Surname, (I)nitials", ... , [8] 75.0 (Score), ... ,[11] 208 (Rank), ...
    #Format for PAIRS is (PRGR in filename):
    #"ReferenceN [0]      ","ENG", "School; Pair / Paar X" , ... , [8] 75.0 (Score), ... ,[11] 208 (Rank), ...
    #NOTE: "ABSENT" can replace all scores

    list_input = input_fstring.replace('\r', '').replace('"', '').replace(';',',').split('\n')#Split based on carriage returns
    dne_list = [] #Hold "list of errors" to be placed on template. Called "Does Not Exist (DNE) list"

    #For each line in the input string, complete formatting steps
    for line in list_input:
        proc_line = line.split(',')
        try:
            ref_num = proc_line[0].strip() #strip white space

            #Populate the relevant details 
            if 'ABSENT' in line:
                score = 0
                rank = None #TODO:Check that this is okay...
            else:
                score = proc_line[8].strip()
                rank = proc_line[11].strip()

        #Search DB for that reference number:
            try:
                #Individuals - expecting only a single student with ref_num
                if not pair_logic:
                    student = SchoolStudent.objects.get(reference=ref_num)
                    student.score = float(score)
                    student.rank = rank
                    student.save()
                else:
                #Pairs - expecting two students with same ref_num
                    student_pair = SchoolStudent.objects.filter(reference=ref_num)
                    #If reference number is not found at all
                    if not student_pair: 
                        dne_list.append('Pairing error: no student with reference %s found in database'%{ref_num})
                        #Not a fatal error; continue with import
                        
                    #If both of the pair are found; update and save them
                    elif student_pair.count()==2:
                        
                        student_pair[0].score=float(score)
                        student_pair[0].rank=rank
                        student_pair[0].save()
                        
                        student_pair[1].score=float(score)
                        student_pair[1].rank=rank
                        student_pair[1].save()
                    
                    #If only one of the pair is found; display error
                    elif student_pair.count() == 1:
                        dne_list.append('Pairing error: only one student with reference %s found in database'%{ref_num})
                        #Not a fatal error; continue with import
                    
                    #If more than two are found; display error
                    else:
                        dne_list.append('Pairing error: more than 2 students with reference %s found in file.'%{ref_num})
            #Individual exceptions: using get() generates exceptions
            except ObjectDoesNotExist:
                dne_list.append('Reference number: %s not found in database.'%{ref_num})
                #Not a fatal error; continue with import
            except ValueError:
                dne_list.append('Reference number: %s contains a data-input error.'%{ref_num})
                #Not a fatal error; continue with import
            except exceptions.MultipleObjectsReturned:
                dne_list.append('ERROR. Import halted. Two students with the same reference: %s were found in the file. Please ensure that, if the file contains information for PAIRS that PR is present on the file name.'%{ref_num})
                return dne_list#Fatal error; STOP IMPORT where the error occured
        #Input data error (not vital to know this; likely not a student-invalid line)
        except IndexError:
            pass #TODO Find out what kind of data generates this error!

    #Return error list
    return dne_list
