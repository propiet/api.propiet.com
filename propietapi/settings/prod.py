#! coding: utf-8

from settings.base import *

BROKER_URL = 'amqp://propiet:propiet@localhost:5672//'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'propiet_prod_db',
        'USER': 'root',
        'PASSWORD': 'pr0p1eT',
        'HOST': '',
        'PORT': '',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'info@propiet.com'
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'AKIAINE3NNQDKNSTE4LA'
EMAIL_HOST_PASSWORD = 'AluYW9uzNxrRZRpKXxvZjhUuTzJ48pzN3PsBS642Owp2'

ALLOWED_HOSTS = ['api.propiet.com', ]

__author__ = 'poli'
