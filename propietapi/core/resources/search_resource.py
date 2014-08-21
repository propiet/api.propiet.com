# -*- coding: utf-8 -*-
# Tastypie imports
from tastypie.authentication import ApiKeyAuthentication
from tastypie.resources import ModelResource , ALL, ALL_WITH_RELATIONS
from tastypie.authorization import DjangoAuthorization
from tastypie.http import HttpUnauthorized, HttpForbidden, HttpCreated
from tastypie.utils import trailing_slash 
from tastypie import fields
from tastypie.models import ApiKey
from tastypie.serializers import Serializer
from tastypie.paginator import Paginator
# core
from core.models  import Post
from core.resources import *
from tastypie.constants import ALL, ALL_WITH_RELATIONS

class SearchResource(ModelResource):
     """ Class SearchResource post endpoint.
        @author: Lionel Cuevas <lionel@hoopemedia.com>"""

     property = fields.ForeignKey(PropertyResource, 'property', full=True)
     user = fields.ForeignKey(UserResource, 'user', full=True)
     category = fields.ForeignKey(CategoryResource, 'category', full=True)
     currency = fields.ForeignKey(CurrencyResource, 'currency', full=True)
     operation = fields.ForeignKey(OperationResource, 'operation', full=True)
     city = fields.ForeignKey(CityResource, 'city', full=True)
     region = fields.ForeignKey(RegionResource, 'region', full=True)
     post_photos = fields.ToManyField(PostPhotoResource, 'postphoto_set', full=True, null=True, blank=True)

     class Meta:
        queryset = Post.objects.all()
        resource_name = 'search'
        serializer = Serializer()
        paginator_class = Paginator
        filtering = {
            'property': ALL_WITH_RELATIONS,
            'category': ALL_WITH_RELATIONS,
            'currency': ALL_WITH_RELATIONS,
            'operation': ALL_WITH_RELATIONS,
            'price': ALL,
            'featured': ALL,
            'status': ALL,
            'city': ALL_WITH_RELATIONS,
            'region': ALL_WITH_RELATIONS,
        }
        #authentication = ApiKeyAuthentication()
        #authorization = DjangoAuthorization()