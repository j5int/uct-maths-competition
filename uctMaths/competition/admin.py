from competition.models import *
from django.contrib import admin

#registers the models with admin
admin.site.register(SiteUser)
admin.site.register(SchoolUser)
admin.site.register(School)
admin.site.register(SchoolStudent)
admin.site.register(Venue)
admin.site.register(Invigilator)