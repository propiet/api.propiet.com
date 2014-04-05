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
from core.models  import Service

class ServiceResource(ModelResource):
     """ Class ServiceResource post endpoint.
        @author: Lionel Cuevas <lionel@hoopemedia.com>"""

     class Meta:
        queryset = Service.objects.all()
        resource_name = 'service'
        serializer = Serializer()
        paginator_class = Paginator
        excludes = ['creation_date', 'last_update']
        #authentication = ApiKeyAuthentication()
        #authorization = DjangoAuthorization()