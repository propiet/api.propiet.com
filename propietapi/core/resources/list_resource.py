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
from core.models import Service, Ambience
from core.forms import GetObjectForm
from cities_light.models import Country, Region, City

class ListResource(ModelResource):
     """ Class ListResource lists endpoint.
        @author: Lionel Cuevas <lionel@hoopemedia.com>"""
     requestHandler = RequestHandler() 

     class Meta:
        allowed_methods = ['post','get']
        queryset = Service.objects.all() 
        resource_name = 'list'

     def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/categories%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('categories'), name="api_list_categories"),
            url(r"^(?P<resource_name>%s)/subcategories%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('subcategories'), name="api_list_subcategories"),
            url(r"^(?P<resource_name>%s)/post%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('post'), name="api_list_post"),
            url(r"^(?P<resource_name>%s)/services%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('services'), name="api_list_services"),
            url(r"^(?P<resource_name>%s)/ambiences%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('ambiences'), name="api_list_ambiences"),
            url(r"^(?P<resource_name>%s)/regions%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('regions'), name="api_list_regions"),
            url(r"^(?P<resource_name>%s)/cities%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('cities'), name="api_list_cities"),
            url(r"^(?P<resource_name>%s)/form/fields%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_form'), name="api_list_form"),
            url(r"^(?P<resource_name>%s)/operations%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('operations'), name="api_list_operations"),
        ]

     def categories(self, request, **kwargs):
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            
            return self.create_response(request, {
                'response':{
                    'data':{
                        'list':[CATEGORIES]
                        },
                    'success': True
                    },                    
            })
        else:
            return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})

     def subcategories(self, request, **kwargs):
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            category = int(request_data['data']['category'])
            return self.create_response(request, {
                'response':{
                    'data':{
                        'list':[SUBCATEGORIES[category]]
                        },
                    'success': True
                    },                    
            })
        else:
            return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})

     def operations(self, request, **kwargs):
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            
            return self.create_response(request, {
                'response':{
                    'data':{
                        'list':[OPERATION_TYPE]
                        },
                    'success': True
                    },                    
            })
        else:
            return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})

     def post(self, request, **kwargs):
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            
            return self.create_response(request, {
                'response':{
                    'data':{
                        'list':[
                            {"DISPOSITION_TYPE":DISPOSITION_TYPE,
                            "UNITY_TYPE":UNITY_TYPE,
                            "QUANTITY":QUANTITY,
                            "ORIENTATION_TYPE":ORIENTATION_TYPE,
                            "BUILDING_TYPE":BUILDING_TYPE,
                            "BUILDING_STATUS":BUILDING_STATUS,
                            "BUILDING_CATEGORY":BUILDING_CATEGORY,
                            "SUITABLE":SUITABLE,
                            "LIGHTNESS":LIGHTNESS,
                            "ROOF_TYPE":ROOF_TYPE,
                            "GATE_TYPE":GATE_TYPE,
                            "INDUSTRIAL_ROOF_TYPE":INDUSTRIAL_ROOF_TYPE},
                        ]
                    },
                    'success': True
                    },                    
            })
        else:
            return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})
        
     def services(self, request, **kwargs):
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            
            object_list = Service.objects.all()
            paginator = Paginator(object_list.values(), 50)
            if('page' in request_data['pagination']):                
                page = request_data['pagination']['page']
            else:
                page = 1
            try:
                objects = paginator.page(page)
            except PageNotAnInteger:
                objects = paginator.page(1)
            except EmptyPage:
                objects = paginator.page(paginator.num_pages)            
            if objects:                                      
                return self.create_response(request, {
                    'response':{
                        'data':{
                            'list':list(objects)
                            },
                        'success': True
                        },                    
                })
            else:
                return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})
        else:
            return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})

     def ambiences(self, request, **kwargs):
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            
            object_list = Ambience.objects.all()
            paginator = Paginator(object_list.values(), 50)
            if('page' in request_data['pagination']):                
                page = request_data['pagination']['page']
            else:
                page = 1
            try:
                objects = paginator.page(page)
            except PageNotAnInteger:
                objects = paginator.page(1)
            except EmptyPage:
                objects = paginator.page(paginator.num_pages)            
            if objects:                                      
                return self.create_response(request, {
                    'response':{
                        'data':{
                            'list':list(objects)
                            },
                        'success': True
                        },                    
                })
            else:
                return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})
        else:
            return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})

     def regions(self, request, **kwargs):
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            
            object_list = Region.objects.all()
            paginator = Paginator(object_list.values(), 50)
            if('page' in request_data['pagination']):
                page = request_data['pagination']['page']
            else:
                page = 1
            try:
                objects = paginator.page(page)
            except PageNotAnInteger:
                objects = paginator.page(1)
            except EmptyPage:
                objects = paginator.page(paginator.num_pages)            
            if objects:                                      
                return self.create_response(request, {
                    'response':{
                        'data':{
                            'list':list(objects)
                            },
                        'success': True
                        },                    
                })
            else:
                return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})
        else:
            return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})

     def cities(self, request, **kwargs):
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            region_id = int(request_data['data']['region'])
            object_list = City.objects.filter(region=region_id)
            paginator = Paginator(object_list.values(), 100)
            if('page' in request_data['pagination']):
                page = request_data['pagination']['page']
            else:
                page = 1
            try:
                objects = paginator.page(page)
            except PageNotAnInteger:
                objects = paginator.page(1)
            except EmptyPage:
                objects = paginator.page(paginator.num_pages)            
            if objects:                                      
                return self.create_response(request, {
                    'response':{
                        'data':{
                            'list':list(objects)
                            },
                        'success': True
                        },                    
                })
            else:
                return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})
        else:
            return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})     

     def get_form(self, request, **kwargs):
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            category = int(request_data['data']['category'])
            subcategory = int(request_data['data']['subcategory'])
            model = str(PROPERTYFORM[category][subcategory])
            form_class = GetObjectForm(model)
            form = form_class()
            default_data = {}

            for field in form:
                if (field.label != 'Ambiences' and field.label != 'Location' 
                and field.label != 'Category' and field.label != 'Subcategory'
                and field.label != 'User' and field.label != 'Services'
                and field.label != 'Features'):
                    default_data[field.html_name] = field

            return self.create_response(request, {
                'response':{
                    'data':{
                        'form':[default_data]
                        },
                    'success': True
                    },                    
            })
        else:
            return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})

     def is_secure(self, request):         
         #if(request.is_secure()):                
        if(self.method_check(request, allowed=['post']) and request.user.is_authenticated()
            and self.throttle_check(request) == None):            
            self.log_throttled_access(request)            
        else: 
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)