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
from core.models  import Operation

class OperationResource(ModelResource):
     """ Class OperationResource post endpoint.
        @author: Lionel Cuevas <lionel@hoopemedia.com>"""

     class Meta:
        queryset = Operation.objects.all()
        resource_name = 'operation'
        serializer = Serializer()
        paginator_class = Paginator
        excludes = ['creation_date', 'last_update']
        filtering = {
            'id': ['exact', 'lt', 'lte', 'gte', 'gt','in'],
            'operation': ['exact', 'lt', 'lte', 'gte', 'gt','in'],            
        }
        #authentication = ApiKeyAuthentication()
        #authorization = DjangoAuthorization()