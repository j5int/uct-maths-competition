from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from competition import views


urlpatterns = patterns('',
<<<<<<< HEAD

  url(r'^content/', views.content, name='content'),
  url(r'^main/', views.main, name='main'),
  url(r'^regStudent/', views.regStudent, name='regStudent'),
  url(r'^search-form/$', views.search_form),
  url(r'^search/$', views.search),
  #url(r'^$', views.current_datetime, name='current_datetime')
  #url(r'^$', views.index, name='index'),
  #url(r'^test/', views.tester, name='tester'),
  #url(r'^$', views.index, name='index'),
  url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),

=======
	url(r'^$', views.index, name='mths.uct.ac.za'),
	url(r'^content/', views.content, name='content'),
	url(r'^main/', views.main, name='main'),
	url(r'^regStudent/', views.regStudent, name='regStudent'),
	url(r'^search-form/$', views.search_form),
	url(r'^search/$', views.search),
	
	url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
>>>>>>> 778efb3367ab51d86da75dc40a95eb4b9aa58c81


)
