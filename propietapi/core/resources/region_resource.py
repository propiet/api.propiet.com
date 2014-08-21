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
from cities_light.models  import Region

class RegionResource(ModelResource):
     """ Class RegionResource post endpoint.
        @author: Lionel Cuevas <lionel@hoopemedia.com>"""

     class Meta:
        queryset = Region.objects.all()
        resource_name = 'region'
        serializer = Serializer()
        paginator_class = Paginator
        excludes = ['creation_date', 'last_update','alternate_names','display_name', 'geoname_id','geoname_code','name_ascii','search_names','slug']        
        filtering = {
            'id': ['exact', 'lt', 'lte', 'gte', 'gt','in'],
            'name': ['exact', 'lt', 'lte', 'gte', 'gt','in'],            
        }
        #authentication = ApiKeyAuthentication()
        #authorization = DjangoAuthorization()