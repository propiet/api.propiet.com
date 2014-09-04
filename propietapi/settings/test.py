#! coding: utf-8

from prod import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'propiet_test_db',
        'USER': 'root',
        'PASSWORD': 'pr0p1eT',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['*', ]

__author__ = 'poli'
