from allauth.account.admin import (EmailAddressAdmin as AllAuth_EmailAddressAdmin,
                                   EmailConfirmationAdmin as AllAuth_EmailConfirmationAdmin)
from django.contrib import admin
from allauth.account.models import EmailAddress as AllAuth_EmailAddress
from .app_settings import app_settings
from .models import EmailConfirmation, EmailAddress
from ..utils import get_user_model

User = get_user_model()

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

# admin.site.register(EmailConfirmation, EmailConfirmationAdmin)