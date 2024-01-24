from django.contrib import admin
from django.urls import path, include

from . import views

from apps.competition import views as comp_views
from .views import not_found_view, server_error_view

admin.autodiscover()

urlpatterns = [
	#the sign in/up page at root
	path('', views.index, name='index'),

	#password reset
	# path(r'^resetpassword/$', password_reset),
	# path(r'^resetpassword/passwordsent/$', password_reset_done),
    # path(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    # path(r'^reset/done/$', password_reset_complete),
	path('account/', include('django.contrib.auth.urls')),
    
	#Aurelia is not quite sure what this does. It make the login work.
	# path(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
	path('accounts/profile/', comp_views.profile, name='profile'),

	#loads competitions/urls.py
    path('apps/competition/', include('apps.competition.urls')),
    #
    #
    # #admin and admin docs
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    #
    # #load allauth/account/urls.py
    path('accounts/', include('apps.allauth.account.urls')),
    path("403/", not_found_view),
    path("500/", server_error_view),
]

handler404 = 'uctMaths.views.handler404'
handler500 = 'uctMaths.views.handler500'