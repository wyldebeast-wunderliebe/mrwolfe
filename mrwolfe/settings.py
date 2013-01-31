# Django settings for pgintranet project.
# -*- coding: utf-8 -*-
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Bob Dobalina', 'bob@evilempire.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mrwolfe',
        'USER': 'root',
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'nl-NL'

DATE_FORMAT = 'j F Y'
SYSTEM_DATE_FORMAT = 'd-m-Y'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = PROJECT_ROOT + '/media/'

SERVE_MEDIA = not DEBUG

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = PROJECT_ROOT + '/statics/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT + '/staticsources',
    )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    )

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4dd4c93f-cf29-4f51-924c-ae29e70af14c'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.contrib.auth.middleware.RemoteUserMiddleware',
    )

TEMPLATE_CONTEXT_PROCESSORS =(
    "django.contrib.auth.context_processors.auth",
    #"django.core.context_processors.debug",
    #"django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'mrwolfe.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django_openid_auth',
    'django_extensions',
    'compressor',
    'haystack',
    'pu_in_core',
    'pu_in_content',
    'mrwolfe'
)

TEST_APPS = ("mrwolfe")

# Add our own role based backend...
#
AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
    )


# Should users be created when new OpenIDs are used to log in?
OPENID_CREATE_USERS = True

# When logging in again, should we overwrite user details based on
# data received via Simple Registration?
OPENID_UPDATE_DETAILS_FROM_SREG = True

# If set, always use this as the identity URL rather than asking the
# user.  This only makes sense if it is a server URL.
OPENID_SSO_SERVER_URL = 'https://www.google.com/accounts/o8/id'

# Tell django.contrib.auth to use the OpenID signin URLs.
LOGIN_URL = '/openid/login/'
LOGIN_REDIRECT_URL = '/'
ALLOWED_EXTERNAL_OPENID_REDIRECT_DOMAINS = []

# Should django_auth_openid be used to sign into the admin interface?
OPENID_USE_AS_ADMIN_LOGIN = False

OPENID_USE_EMAIL_FOR_USERNAME = True

## END OpenID settings

APPEND_SLASH=False

# BEGIN logging
#
LOGFILE="mrwolfe.log"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'},
        },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGFILE,
            'maxBytes': 1024 * 1024 * 20, # 20 MB
            'backupCount': 10,
            'formatter': 'standard',
            },
        },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        },
        'utils': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'mrwolfe': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}

#
# END logging

# compressor
#COMPRESS_ENABLED = True


# BEGIN Mr.Wolfe settings
#
ISSUE_STATUS_CHOICES = (
    ('open', 'Open'),
    ('closed', 'Closed'),
    ('progress', 'In progress'),    
    )

ISSUE_STATUS_OPEN = ISSUE_STATUS_CHOICES[0][0]
ISSUE_STATUS_CLOSED = ISSUE_STATUS_CHOICES[1][0]
ISSUE_STATUS_PROGRESS = ISSUE_STATUS_CHOICES[2][0]

ISSUE_STATUS_DEFAULT = ISSUE_STATUS_OPEN

# Do we allow incoming messages from non contacts?
ALLOW_NON_CONTACTS = False

MESSAGE_FIELDS = (("subject", "Subject"),
                  ("from", "From"),
                  ("to", "To"),
                  ("text", "Message body"))

NOTIFICATION_MAP = {
    'issue_received': 'notification/issue_received.html',
    'issue_closed': 'notification/issue_closed.html',
}

DEFAULT_FROM_ADDR = "support@evilempire.com"

#
# END Mr.Wolfe settings

# BEGIN Email settings
#
EMAIL_HOST = "smtp.evilempire.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "bobdobalina"
EMAIL_HOST_PASSWORD = "verySekret" 
EMAIL_USE_TLS = True
#
# END Email settings


# BEGIN search (Haystack)
#
HAYSTACK_SITECONF = "mrwolfe.init_haystack"
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 15
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(os.path.dirname(__file__), 'whoosh_index')
#
# END search
