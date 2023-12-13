from django.urls import path

from . import views

urlpatterns = [
    path("email/", views.email, name="account_email"),
    path("signup/", views.signup, name="account_signup"),
    path("login/", views.login, name="account_login"),
    path("password/change/", views.password_change, name="account_change_password"),
    path("password/set/", views.password_set, name="account_set_password"),
#    path(r"^password_delete/$", views.password_delete, name="acct_passwd_delete"),
#    path(r"^password_delete/done/$", "django.views.generic.simple.direct_to_template", {
#        "template": "account/password_delete_done.html",
#    }, name="acct_passwd_delete_done"),
    path("logout/", views.logout, name="account_logout"),
    
    path("email/confirm/", views.confirm_email, name="account_confirm_email"),
    
    # password reset
    path("password_reset/", views.password_reset, name="account_reset_password"),
    path("password/reset/done/", views.password_reset_done, name="account_reset_password_done"),
    path("password/reset/key/", views.password_reset_from_key, name="account_reset_password_from_key"),
    
    #localhost/accounts/
    # path(r'^$', views.allauthtest, name='allauthtest'),
]
