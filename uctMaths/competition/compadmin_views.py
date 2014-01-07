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

import confirmation
import compadmin

import csv

@login_required
def upload_results(request):

    if request.method == 'POST':
        #a=request.POST
        form = UploadResultsForm(request.POST, request.FILES)
        handler_output = handle_uploaded_file(request.FILES['upload_file'])
    else:
        handler_output = ''
        
    fileUpload = UploadResultsForm()
    c = {'fileUpload' : fileUpload, 'handler_output' : handler_output}
    c.update(csrf(request))

    return render_to_response('admin/upload_results.html', c, context_instance=RequestContext(request))


def handle_uploaded_file(inputf):
    """ Handle input .RES file and print any errors to user (ie. return a string to be used in template) """
    #TODO Better file format checking!
    if '.RES' not in inputf.name:
        return 'Incorrect file format provided.'



    #Find student based on reference number.
#    student_list = Student.objects.all()

    # *Filter* student DB based on filename? Allow "Escape Character"
#    if 'X' not in inputf.name:
#        grade = 0
#        if 'PR' in inputf.name:
#            paired = True #A pair file
#        elif 'IND' in inputf.name:
#            paired = False
#        for k in range (8,13):
#            if k in inputf.name:
#                grade = k
#                break
#    else:

    input_fstring=''
    #Chunks for handling larger files - will essentially just have a long string of char's after this
    for chunk in inputf.chunks():
        input_fstring += chunk

    #Format for INIDIVIDUALS is (INDGR in filename):
    #"ReferenceN      ","ENG", "School; SurnameName, (I)nitial" 11,    8,   11,  75.0, 41.7, 41.7, 208, 5
    #Format for PAIRS is (PRGR in filename):
    #"ReferenceN      ","ENG", "School; Pair / Paar X" 11,    8,   11,  75.0, ... ,[10]: 208 (Rank), 5
    #NOTE: "ABSENT" can replace all scores

    list_input = input_fstring.replace('\n', '').replace('"', '').replace(';',',').split('\r')#Split based on carriage returns
    output_string = ''

    #For each line in the input string, complete formatting steps
    for line in list_input:
        proc_line = line.split(',')
        try:
            ref_num = proc_line[0].strip() #strip white space

            #Populate the relevant details 
            if 'ABSENT' in line:
                score = 0
                rank = 'ABSENT'
            else:
                score = proc_line[8].strip()
                rank = proc_line[11].strip()

        #Search DB for that reference number:
            try:
                student = SchoolStudent.objects.get(reference=ref_num)
                print student
                student.score = float(score)
                student.rank = rank
                student.save()
            except ObjectDoesNotExist:
                print ref_num, 'does not exist!'
            except ValueError:
                print 'Val Error!'

        except IndexError:
            pass #Empty line or somesuch

    return list_input
