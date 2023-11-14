# Django settings for uctMaths project.
import os



# import background_task
from backports.configparser import RawConfigParser

config = RawConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'settings.ini'))

DEBUG = config.get('debug', 'DEBUG')
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': config.get('database', 'DATABASE_ENGINE'),
        'NAME': config.get('database', 'DATABASE_NAME'),    #new UCT database
        'USER': config.get('database', 'DATABASE_USER'),
        'PASSWORD': config.get('database', 'DATABASE_PASSWORD'),
        'HOST': config.get('database', 'DATABASE_HOST'),                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': config.get('database', 'DATABASE_PORT'),                      # Set to empty string for default.
    }
}

#Email settings
SMTP_ENABLED = config.get('email', 'SMTP_ENABLED')
EMAIL_BACKEND = config.get('email', 'EMAIL_BACKEND')
EMAIL_USE_TLS = config.get('email', 'EMAIL_USE_TLS')
EMAIL_HOST = config.get('email', 'EMAIL_HOST')
EMAIL_HOST_USER = config.get('email', 'EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config.get('email', 'EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config.get('email', 'DEFAULT_FROM_EMAIL')
SERVER_EMAIL = config.get('email', 'SERVER_EMAIL')
EMAIL_PORT = config.get('email', 'EMAIL_PORT')

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Africa/Johannesburg'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
# MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = config.get('secrets', 'SECRET_KEY')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'allauth.account.middleware.AccountMiddleware'
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#allauth
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)
ACCOUNT_AUTHENTICATION_METHOD ="username"
#endallauth

ROOT_URLCONF = 'uctMaths.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'uctMaths.wsgi.application'

#allauth
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.template.context_processors.request",
    'django.contrib.auth.context_processors.auth',
    "apps.allauth.account.context_processors.account",
    # "django.core.context_processors.auth",

)
#endallauth

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'apps/allauth/apps/allauth/templates'),
                 os.path.join(BASE_DIR, 'apps/competition/apps/competition/interface'),
                 os.path.join(BASE_DIR, 'apps/allauth/apps/allauth/templates'),
                 os.path.join(BASE_DIR, 'apps/competition/apps/competition/interface')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                "django.template.context_processors.request",
                'django.contrib.auth.context_processors.auth',
                "apps.allauth.account.context_processors.account",
                "django.contrib.messages.context_processors.messages",

            ],
        },
    },
]

INSTALLED_APPS = (
    'uctMaths',
    'apps.competition',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    #admin and admin docs
    'django.contrib.admin',
    'django.contrib.admindocs',
    #allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #endallauth
    #Import-export functionality
    'import_export', #(https://django-import-export.readthedocs.org/en/latest/configuration.html)
    # Background process handling
    # 'background_task'
)

# BACKGROUND_TASK_RUN_ASYNC = False
MAX_ATTEMPTS = 9

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'applogfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'UCTMATHS.log',
            'maxBytes': 1024*1024*15, # 15MB
            'backupCount': 10,
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'APPNAME': {
            'handlers': ['applogfile',],
            'level': 'DEBUG',
        },
        'ho.pisa': {
            'handlers': ['applogfile'],
            'level': 'ERROR'
       },
    }
}
