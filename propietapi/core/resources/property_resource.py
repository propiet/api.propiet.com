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
from tastypie.constants import ALL, ALL_WITH_RELATIONS
# core
from core.models  import Property
from core.resources import *

class PropertyResource(ModelResource):
     """ Class PropertyResource post endpoint.
        @author: Lionel Cuevas <lionel@hoopemedia.com>"""

     service = fields.ForeignKey(ServiceResource, 'service', full=True, null=True, blank=True)
     ambience = fields.ForeignKey(AmbienceResource, 'ambience', full=True, null=True, blank=True)
     feature = fields.ForeignKey(FeatureResource, 'feature', full=True, null=True, blank=True)
     location = fields.ForeignKey(LocationResource, 'location', full=True, null=True, blank=True)
     category = fields.ForeignKey(CategoryResource, 'category', full=True)
     subcategory = fields.ForeignKey(SubCategoryResource, 'subcategory', full=True)

     class Meta:
        queryset = Property.objects.all()
        resource_name = 'property'
        serializer = Serializer()
        paginator_class = Paginator
        excludes = ['creation_date', 'last_update']
        filtering = {
            'location': ALL_WITH_RELATIONS,
            'category': ALL_WITH_RELATIONS,
            'subcategory': ALL_WITH_RELATIONS,
            'antiqueness': ['exact', 'lt', 'lte', 'gte', 'gt'],
            'orientation': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        #authentication = ApiKeyAuthentication()
        #authorization = DjangoAuthorization()