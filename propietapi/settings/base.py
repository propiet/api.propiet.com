# -*- coding: utf-8 -*-
import os
from os import path
from django.utils.translation import ugettext_lazy as _

PROJECT_ROOT = path.abspath(path.dirname(__name__))

# Django settings for propietapi project.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    (u'Poli García', 'poli+propiet@devartis.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'propiet_db.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }    
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#CACHES = {
#    'default' : dict(
#        BACKEND = 'johnny.backends.memcached.MemcachedCache',
#        LOCATION = ['127.0.0.1:11211'],
#        JOHNNY_CACHE = True,
#    )
#}
#JOHNNY_MIDDLEWARE_KEY_PREFIX='jc_propietapi:'

# SSL configuration 
# uncomment the following lines to add SSL 
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = False

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Argentina/Buenos_Aires'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)

LANGUAGE_CODE = 'es-AR'

LANGUAGES = (
    ('es', _('Spanish')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths
    path.join(PROJECT_ROOT, 'admin'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&amp;lbc#h8h_var^4=^+e^av(6(72z8+6un9ol#++4tbdo7*u3m8l'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'propietapi.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'propietapi.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

)

DEFAULT_FROM_EMAIL = 'info@propiet.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'core',    
    'tastypie',
    'cities_light',
    'south',
    'imagekit',
)

SOUTH_MIGRATION_MODULES = {
    'cities_light': 'cities_light.south_migrations',
}

# Tastypie
TASTYPIE_ALLOW_MISSING_SLASH = True
TASTYPIE_FULL_DEBUG = True
TASTYPIE_CANNED_ERROR = 'Oops!'

# Grappelli
GRAPPELLI_ADMIN_TITLE = 'Propiet Backoffice'

# DJANGO-STORAGES

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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#Required Fields defaults
ZONA_PROP_HECTARES_DEFAULT = 1
ZONA_PROP_QUANTITY_AMBIENCES_DEFAULT = 1
ZONA_PROP_SQUARE_METERS_DEFAULT = 1
ZONA_PROP_COVERED_METERS_DEFAULT = 1
ZONA_PROP_QUANTITY_BEDROOMS_DEFAULT = 1


ZONAPROP_PROVEEDOR = 126
ZONAPROP_PASSWORD = 'PRN7F'
ZONAPROP_USUARIO = 12345678
ZONAPROP_HORARIO_ATENCION = u'Horario de atención'

ZONAPROP_PHONE_NUMBER = 'Default phone number'
ZONAPROP_AREA_CODE = 'Default Area Code'

ZONAPROP_CONTACT_MAIL = 'Default Contact Mail'
ZONAPROP_CONTACT_FIRST_NAME = 'Default First Name'
ZONAPROP_CONTACT_LAST_NAME = 'Default Last Name'