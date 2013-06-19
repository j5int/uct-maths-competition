# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import loader, Context


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def tester (request):
   #t = loader.get_template('base.html')
   return render_to_response('base.html',{})
   #return HttpResponse(t.render(base.html))

def index(request):
    return render_to_response('onlinemaths.html', {})

