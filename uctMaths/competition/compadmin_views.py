# Create your views here.
from __future__ import unicode_literals
import os
import shutil
from django.conf import settings
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
from competition.forms import StudentForm, SchoolForm, InvigilatorForm, ResponsibleTeacherForm, UploadResultsForm, UploadDeclarationForm
from competition.models import SchoolStudent, School, Invigilator, Venue, ResponsibleTeacher
from django.contrib.auth.models import User
#from django.contrib.contenttypes import *
from django.db import connection
from django.core import exceptions
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import default_storage
from django.core.files import File

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
                            'No errors occurred while importing results.',
                            'Please double check that all students in the database have been updated in the School Students tab'
                            ]
    #Present UploadResultsForm (defined in forms.py)
    fileUpload = UploadResultsForm()

    if not handler_output:
        handler_output = ['Please select a file to upload']

    #Present upload form and handler message (prompt for input/errors text) to the user
    c = {'fileUpload' : fileUpload, 'handler_output' : handler_output}
    c.update(csrf(request))

    return render_to_response('admin/upload_results.html', c, context_instance=RequestContext(request))

@login_required
def upload_declaration(request):
    """ Handle upload files from the user. Bound to the upload_declaration.html admin page."""

    handler_output=[]#Sent to html template for feedback to user

    #Once the user has pressed 'Submit'
    if request.method == 'POST':
        #a=request.POST
        try: #Try receive file from 'Submit' post from user
            form = UploadDeclarationForm(request.POST, request.FILES)
            file = request.FILES['upload_file']
            filepath = os.path.join(__file__,"..","..","Declaration")
            filename = str(file)
            if not filename == 'Declaration.pdf':
                handler_output = ['Declaration must be a pdf and be named Declaration.pdf']
            else:
                shutil.rmtree(filepath)
                os.mkdir(filepath)
                filepath = os.path.join(filepath,"")
                default_storage.save(filepath, File(file))
                if len(os.listdir(filepath)) == 1:
                    autofilename = os.listdir(filepath)[0]
                    os.rename(os.path.join(filepath,autofilename), os.path.join(filepath,filename))
        except Exception as e:#If the user just spams the 'Submit' button without selecting file
            handler_output = [e]

        if not handler_output: #No errors have occured
            handler_output = [
                            'No errors occurred while importing the declaration.']
    #Present UploadDeclarationForm (defined in forms.py)
    fileUpload = UploadDeclarationForm()

    if not handler_output:
        handler_output = ['Please select a file to upload']

    #Present upload form and handler message (prompt for input/errors text) to the user
    c = {'fileUpload' : fileUpload, 'handler_output' : handler_output}
    c.update(csrf(request))

    return render_to_response('admin/upload_declaration.html', c, context_instance=RequestContext(request))

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
        return ['Input filename error. Please ensure that the file name contains PR or IND so that pair or individual (respectively) results import can occur.']
 #------------------------------------------------#

    input_fstring=u''
    #Chunks for handling larger files - will essentially just have a long string of char's after this
    for chunk in inputf.chunks():
        input_fstring += chunk.decode('utf-8','replace') #Replace accented characters with unicode equivalents

    #Format for INIDIVIDUALS is (INDGR in filename):
    #"ReferenceN [0]      ","ENG", "School; Surname, (I)nitials", ... , [8] 75.0 (Score), ... ,[11] 208 (Rank), ...
    #Format for PAIRS is (PRGR in filename):
    #"ReferenceN [0]      ","ENG", "School; Pair / Paar X" , ... , [8] 75.0 (Score), ... ,[11] 208 (Rank), ...
    #NOTE: "ABSENT" can replace all scores

    # TODO: clean this up. It depends on the field formatting in the output_PRN_files method
    # in compadmin.py, which is slightly different for individuals and pairs.
    # Also, the homemade CSV parser in the following row should use a standard library which would ignore the commas
    # and semicolons inside a quoted field.
    
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
                rank = None
            else:
                if not pair_logic:
                    score = proc_line[8].strip()
                    rank = proc_line[11].strip()
                else:
                    score = proc_line[6].strip()
                    rank = proc_line[9].strip()


        #Search DB for that reference number:
            try:
                student = SchoolStudent.objects.get(reference=ref_num)
                student.score = float(score)
                student.rank = rank
                student.award = ''
                student.save()
            #Individual exceptions: using get() generates exceptions
            except ObjectDoesNotExist:
                dne_list.append('Reference number: %s not found in database.'%{ref_num})
                #Not a fatal error; continue with import
            except ValueError:
                dne_list.append('Reference number: %s contains a data-input error.'%{ref_num})
                #Not a fatal error; continue with import
            except exceptions.MultipleObjectsReturned:
                dne_list.append('ERROR. Import halted. Two students with the same reference: %s were found in the file. Please ensure that, if the file contains information for PAIRS that PR is present in the filename.'%{ref_num})
                return dne_list#Fatal error; STOP IMPORT where the error occured
        #Input data error (not vital to know this; likely not a student-invalid line)
        except IndexError:
            pass #TODO Find out what kind of data generates this error!

    #Return error list
    return dne_list
