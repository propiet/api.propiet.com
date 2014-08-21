# -*- coding: utf-8 -*-
# Django imports
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf.urls import *
from django.utils import simplejson
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Tastypie imports
from tastypie.authentication import ApiKeyAuthentication
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.http import HttpUnauthorized, HttpForbidden, HttpCreated
from tastypie.utils import trailing_slash 
from tastypie import fields
from tastypie.models import ApiKey
from tastypie.serializers import Serializer
# core
from core.handlers  import *
from core.constants import *
from core.models import Post,Service, Ambience, Feature, Property, Category, SubCategory, Operation
from core.forms import GetObjectForm, PropertyForm
from cities_light.models import Country, Region, City
from django.utils.translation import ugettext_lazy as _

class ProperatiResource(ModelResource):

    class Meta:
        serializer = Serializer(formats=['json', 'xml'])
        resource_name = 'properati'

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/feed%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('feed'), name="api_list_feed"),
            ]

    def feed(self, request, **kwargs):
        posts = Post.objects.all()

        respuesta = {
                    'ads':{
                        'ad': "test"
                    }

        }
        
        return self.create_response(request, respuesta)

    
        