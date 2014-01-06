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
    
    input_fstring=''
    #Chunks for handling larger files - will essentially just have a long string of char's after this
    for chunk in inputf.chunks():
        input_fstring += chunk

    #Format for INIDIVIDUALS is (INDGR in filename):
    #"ReferenceN      ","ENG", "School; SurnameName, (I)nitial" 11,    8,   11,  75.0, 41.7, 41.7, 208, 5
    #Format for PAIRS is (PRGR in filename):
    #"ReferenceN      ","ENG", "School; Pair / Paar X" 11,    8,   11,  75.0, 41.7, 41.7, 208, 5
    #NOTE: "ABSENT" can replace all scores

    list_input = input_fstring.replace('\n', '').replace('"', '').replace(';',',').split('\r')#Split based on carriage returns
    output_string = ''

    #For each line in the input string, complete formatting steps
    #for line in list_input:
    #    stripped_line = line.split(',')
    #    output_string+=str(stripped_line)+'\n'

    return list_input
