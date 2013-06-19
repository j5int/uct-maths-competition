# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import loader, Context

def allauthtest(request):
	return render_to_response('base.html', {})

def content (request, ):
   #t = loader.get_template('base.html')
<<<<<<< HEAD
   return render_to_response('contents.html',{})
=======
   return render_to_response('test.html',{})
>>>>>>> f3401bef9e3f2712bc4286fc7042659e4fa9a4ea
   #return HttpResponse(t.render(base.html))

def main (request, ):
   return render_to_response('main.html',{})

def regStudent (request, ):
   return render_to_response('regStudent.html',{})

def index(request):
    return render_to_response('onlinemaths.html', {})
    
def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 3:
            errors.append('Please enter at most 20 characters.')
            return HttpResponse('You submisdsdsdstted')
        else:
            return HttpResponse('You submitted')
    else:
        return render_to_response('search_form.html',
        {'errors': errors})
  
