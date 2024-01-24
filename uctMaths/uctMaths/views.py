from django.http import HttpResponseRedirect


def index(request):
    #If the due date has not passed:
    return HttpResponseRedirect('/accounts/login')

from django.shortcuts import render as render_to_response
from django.template import RequestContext



def not_found_view(request):
    raise FileNotFoundError

def server_error_view(request):
    raise Exception

def handler404(request, *args, **argv):
    response = render_to_response(request,'404.html', {}, status=404)
    return response

def handler500(request, *args, **argv):
    response = render_to_response(request, '50x.html', {},status=500)
    return response