from allauth.account.admin import (EmailAddressAdmin as AllAuth_EmailAddressAdmin,
                                   EmailConfirmationAdmin as AllAuth_EmailConfirmationAdmin)
from django.contrib import admin
from allauth.account.models import EmailAddress as AllAuth_EmailAddress
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .app_settings import app_settings
from .models import EmailConfirmation, EmailAddress

class EmailAddressAdmin(AllAuth_EmailAddressAdmin):
    list_display = ('email', 'user', 'primary', 'verified')
    list_filter = ('primary', 'verified')
    search_fields = ['email'] + list(map(lambda a: 'user__' + a,
                                    filter(lambda a: a and hasattr(User(), a),
                                           [app_settings.USER_MODEL_USERNAME_FIELD,
                                            'first_name',
                                            'last_name'])))
    raw_id_fields = ('user',)


class EmailConfirmationAdmin(AllAuth_EmailConfirmationAdmin):
    list_display = ('email_address', 'created', 'sent', 'key')
    list_filter = ('sent',)
    raw_id_fields = ('email_address',)


if admin.site.is_registered(AllAuth_EmailAddress):
    admin.site.unregister(AllAuth_EmailAddress)
admin.site.register(EmailAddress, EmailAddressAdmin)



@admin.action(description="Mark selected Users as inactive")
def make_published(modeladmin, request, queryset):
    queryset.update(is_active=False)


class j5UserAdmin(UserAdmin):
    actions = [make_published]

admin.site.unregister(User)
admin.site.register(User, j5UserAdmin)