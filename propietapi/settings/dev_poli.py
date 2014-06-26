#! coding: utf-8

from settings.dev import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'propiet_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            "init_command": "SET unique_checks=0;",
        },
    }
}
__author__ = 'poli'
