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
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django_extensions',
    'compressor',
    'haystack',
    'pu_in_core',
    'pu_in_content',
    'mrwolfe'
)

TEST_APPS = ("mrwolfe")

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    )

LOGIN_REDIRECT_URL = "/login/"
LOGIN_URL = "/login"

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
#
#COMPRESS_ENABLED = not DEBUG


# BEGIN Mr.Wolfe settings
#
ISSUE_STATUS_CHOICES = (
    ('open', 'Open'),
    ('closed', 'Closed'),
    ('progress', 'In progress'),
    ('hold', 'On hold')
    )

ISSUE_STATUS_OPEN = ISSUE_STATUS_CHOICES[0][0]
ISSUE_STATUS_CLOSED = ISSUE_STATUS_CHOICES[1][0]
ISSUE_STATUS_PROGRESS = ISSUE_STATUS_CHOICES[2][0]
ISSUE_STATUS_HOLD = ISSUE_STATUS_CHOICES[3][0]

ISSUE_STATUS_DEFAULT = ISSUE_STATUS_OPEN

# Do we allow incoming messages from non contacts?
# If so, the sender address is set into the Issue.submitter_address field
#
ALLOW_NON_CONTACTS = True

MESSAGE_FIELDS = (("subject", "Subject"),
                  ("from", "From"),
                  ("to", "To"),
                  ("text", "Message body"))

# Override notification templates if you wish
#
NOTIFICATION_MAP = {
    'issue_received': 'notification/issue_received.html',
    'issue_closed': 'notification/issue_closed.html',
    'issue_created': 'notification/issue_created.html',
}

# This is the address of your actual site. Used for sending URL's of
# issues to operators.
#
HOST_ADDRESS = "http://support.evilempire.com"

DEFAULT_FROM_ADDR = "support@evilempire.com"

# Blacklist for sending out notifications. Add any mailboxes that you
# read here, so as to never send to the mailbox that you also read
# mail off...
#
NOTIFICATION_BLACKLIST = []

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
HAYSTACK_WHOOSH_PATH = os.path.join(os.path.dirname(__file__), 'whoosh_index')
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'URL': 'http://127.0.0.1:7070/solr',
        'PATH': HAYSTACK_WHOOSH_PATH
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 27
#
# END search
