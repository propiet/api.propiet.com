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
from core.models  import Location

class LocationResource(ModelResource):
     """ Class LocationResource post endpoint.
        @author: Lionel Cuevas <lionel@hoopemedia.com>"""

     class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
        serializer = Serializer()
        paginator_class = Paginator
        excludes = ['creation_date', 'last_update']
        filtering = {
            'id': ['exact', 'lt', 'lte', 'gte', 'gt','in','isnull'],
            'address': ['exact', 'lt', 'lte', 'gte', 'gt','in','contains','icontains'],            
        }
        #authentication = ApiKeyAuthentication()
        #authorization = DjangoAuthorization()