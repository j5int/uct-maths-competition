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


@login_required
def upload_results(request):

    if request.method == 'POST':
        #a=request.POST
        form = UploadResultsForm(request.POST, request.FILES)
        handle_uploaded_file(request.FILES['upload_file'])
    else:
        pass
        
    fileUpload = UploadResultsForm()
    c = {'fileUpload' : fileUpload}
    c.update(csrf(request))

    return render_to_response('admin/upload_results.html', c, context_instance=RequestContext(request))
    
def handle_uploaded_file(inputf):
#    with file as open(file_name):
    print inputf.name
    for chunk in inputf.chunks():
        print str(chunk)
