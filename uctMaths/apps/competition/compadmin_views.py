# Create your views here.
from __future__ import unicode_literals
import os
import shutil
from django.shortcuts import render as render_to_response
from django.template.context_processors import csrf
from apps.competition.forms import UploadResultsForm, UploadDeclarationForm
from apps.competition.models import SchoolStudent
#from django.contrib.contenttypes import *
from django.core import exceptions
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import default_storage
from django.core.files import File

import csv
import io

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
            handler_output = ['Please select a valid Ranked.csv file from your computer by clicking the \'Browse...\' button']

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

    return render_to_response(request, 'admin/upload_results.html', c)

@login_required
def upload_declaration(request):
    """ Handle upload files from the user. Bound to the upload_declaration.html admin page."""

    handler_output=[]#Sent to html template for feedback to user

    #Once the user has pressed 'Submit'
    if request.method == 'POST':
        try: #Try receive file from 'Submit' post from user
            form = UploadDeclarationForm(request.POST, request.FILES)
            file = request.FILES['upload_file']
            filename = "Declaration.pdf"

            filepath = os.path.normpath(os.path.join(os.path.dirname(__file__), "../..", "Declaration", filename))
            if os.path.exists(os.path.dirname(filepath)):
                shutil.rmtree(os.path.dirname(filepath))
                os.mkdir(os.path.dirname(filepath))
            default_storage.save(filepath, File(file))
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

    return render_to_response(request, 'admin/upload_declaration.html', c)

def handle_uploaded_file(inputf):
    """ Handle input Ranked.csv file and return any errors to calling function (ie. return a string to be used in template) """

    #TODO Better file format checking!
    if 'Ranked.csv' not in inputf.name:
        return ['Incorrect file format provided.']

    input_fstring=''
    #Chunks for handling larger files - will essentially just have a long string of char's after this
    for chunk in inputf.chunks():
        input_fstring += chunk.decode('utf-8','replace') #Replace accented characters with unicode equivalents

    results = csv.DictReader(input_fstring)

    dne_list = [] #Hold "list of errors" to be placed on template. Called "Does Not Exist (DNE) list"

    ref_num_header = results.fieldnames[0]
    if 'Score' not in results.fieldnames:
        dne_list.append('Could not find score column. It should have the heading "Score".')
    if 'Rank' not in results.fieldnames:
        dne_list.append('Could not find rank column. It should have the heading "Rank".')
    if len(dne_list) > 0:
        return dne_list

    for result in results:
        ref_num = (result[ref_num_header]
            .strip('"')  # Sometimes the ref_num is quoted
            .zfill(7)  # Adds back leading zeroes which Excel can remove
        )
        score = result["Score"]
        rank = result["Rank"]

        try:
            student = SchoolStudent.objects.get(reference=ref_num)
            student.score = float(score)
            student.rank = rank
            student.award = ''
            student.save()
        # Individual exceptions: using get() generates exceptions
        except ObjectDoesNotExist:
            dne_list.append('Reference number: %s not found in database.' % (ref_num,))
            # Not a fatal error; continue with import
        except ValueError:
            dne_list.append('Reference number: %s contains a data-input error.' % (ref_num,))
            # Not a fatal error; continue with import
        except exceptions.MultipleObjectsReturned:
            dne_list.append('ERROR. Import halted. Two students with the same reference: %s were found in the file. Please ensure that, if the file contains information for PAIRS that PR is present in the filename.'%{ref_num})
            return dne_list  # Fatal error; STOP IMPORT where the error occured

    #Return error list
    return dne_list
