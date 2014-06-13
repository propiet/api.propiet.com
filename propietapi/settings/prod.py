#! coding: utf-8

from settings.base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'propiet_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'AKIAIQQ72BXKWY4UZWSQ'
EMAIL_HOST_PASSWORD = 'AhYJun4ixzaspxy3SpjadchVgiusVjuk1VpOo3RVHzeC'

ALLOWED_HOSTS = ['api.propiet.com', ]

__author__ = 'poli'
