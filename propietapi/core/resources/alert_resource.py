# -*- coding: utf-8 -*-
# Tastypie imports
from tastypie.authentication import ApiKeyAuthentication
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.http import HttpUnauthorized, HttpForbidden, HttpCreated
from tastypie.utils import trailing_slash 
from tastypie import fields
from tastypie.models import ApiKey
from tastypie.serializers import Serializer
from tastypie.paginator import Paginator
# core
from core.models  import Alert

class AlertResource(ModelResource):
     """ Class AlertResource post endpoint.
        @author: Lionel Cuevas <lionel@hoopemedia.com>"""

     class Meta:
        queryset = Alert.objects.all()
        resource_name = 'alert'
        serializer = Serializer()
        paginator_class = Paginator
        #excludes = ['email', 'password', 'is_superuser']
        # Add it here.
        #authentication = ApiKeyAuthentication()
        #authorization = DjangoAuthorization()