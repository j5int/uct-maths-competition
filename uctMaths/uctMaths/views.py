from django.http import HttpResponseRedirect


def index(request):
    #If the due date has not passed:
    return HttpResponseRedirect('/accounts/login')