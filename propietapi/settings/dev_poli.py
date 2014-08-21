#! coding: utf-8

from settings.dev import *

INSTALLED_APPS += ('djcelery', 'django_extensions', )

BROKER_URL = 'amqp://propiet:propiet@localhost:5672//'

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
