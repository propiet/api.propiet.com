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
from core.models import Post,Service, Ambience, Feature, Property, Category, SubCategory, Operation, Location, UserProfile, PostPhoto
from core.forms import GetObjectForm, PropertyForm
from cities_light.models import Country, Region, City
from django.utils.translation import ugettext_lazy as _

from lxml import etree

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
            url(r"^(?P<resource_name>%s)/features%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('features'), name="api_list_features"),
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
            url(r"^(?P<resource_name>%s)/search%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('search'), name="api_list_search"),
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
        
     def search(self, request, **kwargs):
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            
            return self.create_response(request, {
                'response':{
                    'data':{
                        'list':[
                            {"CATEGORIES":CATEGORIES,
                            "OPERATION_TYPE":OPERATION_TYPE},                            
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

     def features(self, request, **kwargs):
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            
            object_list = Feature.objects.all()
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
            category_id = int(request_data['data']['category'])
            category = Category.objects.get(pk=category_id)
            subcategory_id = int(request_data['data']['subcategory'])
            subcategory = SubCategory.objects.get(pk=subcategory_id)
            operation_id = int(request_data['data']['operation_type'])
            operation = Operation.objects.get(pk=operation_id)

            form = PropertyForm()
            default_data = {}            
            for field in form:

                # Required by Category
                if(category.name == 'Departamentos' or category.name == 'Casas' or category.name == 'PH' or category.name == 'Quintas'):
                    if(field.html_name == 'square_meters'):
                        default_data[field.html_name] = {}
                        default_data[field.html_name]['label'] = _(field.label)
                        default_data[field.html_name]['field'] = field.as_widget(attrs={"required":True,"class":"form-control"})
                    elif(field.html_name == 'quantityAmbiences'):
                        default_data[field.html_name] = {}
                        default_data[field.html_name]['label'] = _(field.label)
                        default_data[field.html_name]['field'] = field.as_widget(attrs={"required":True,"class":"form-control"})
                    elif(field.html_name == 'quantityBedrooms'):
                        default_data[field.html_name] = {}
                        default_data[field.html_name]['label'] = _(field.label)
                        default_data[field.html_name]['field'] = field.as_widget(attrs={"required":True,"class":"form-control"})
                    elif(field.html_name == 'antiqueness'):
                        default_data[field.html_name] = {}
                        default_data[field.html_name]['label'] = _(field.label)
                        default_data[field.html_name]['field'] = field.as_widget(attrs={"required":True,"class":"form-control"})
                    else:
                        default_data[field.html_name] = {}
                        default_data[field.html_name]['label'] = _(field.label)
                        default_data[field.html_name]['field'] = field.as_widget(attrs={"class":"form-control"})

                elif(category.name == 'Terrenos y Lotes'):
                    if(field.html_name == 'square_meters'):
                        default_data[field.html_name] = {}
                        default_data[field.html_name]['label'] = _(field.label)
                        default_data[field.html_name]['field'] = field.as_widget(attrs={"required":True,"class":"form-control"})
                    else:
                        default_data[field.html_name] = {}
                        default_data[field.html_name]['label'] = _(field.label)
                        default_data[field.html_name]['field'] = field.as_widget(attrs={"class":"form-control"})

                elif(category.name == 'Campos y chacras'):
                    if(field.html_name == 'hectares'):
                        default_data[field.html_name] = {}
                        default_data[field.html_name]['label'] = _(field.label)
                        default_data[field.html_name]['field'] = field.as_widget(attrs={"required":True,"class":"form-control"})
                    else:
                        default_data[field.html_name] = {}
                        default_data[field.html_name]['label'] = _(field.label)
                        default_data[field.html_name]['field'] = field.as_widget(attrs={"class":"form-control"})

                elif(category.name == 'Cocheras'):
                    if(field.html_name == 'garageCoverage'):
                        default_data[field.html_name] = {}
                        default_data[field.html_name]['label'] = _(field.label)
                        default_data[field.html_name]['field'] = field.as_widget(attrs={"required":True,"class":"form-control"})
                    else:
                        default_data[field.html_name] = {}
                        default_data[field.html_name]['label'] = _(field.label)
                        default_data[field.html_name]['field'] = field.as_widget(attrs={"class":"form-control"})

                elif(category.name == 'Galpones, depósitos y edificios industriales' or category.name == 'Locales comerciales' or category.name == 'Oficinas' or category.name == 'Consultorios'):
                    if(field.html_name == 'square_meters'):
                        default_data[field.html_name] = {}
                        default_data[field.html_name]['label'] = _(field.label)
                        default_data[field.html_name]['field'] = field.as_widget(attrs={"required":True,"class":"form-control"})
                    elif(field.html_name == 'antiqueness'):
                        default_data[field.html_name] = {}
                        default_data[field.html_name]['label'] = _(field.label)
                        default_data[field.html_name]['field'] = field.as_widget(attrs={"required":True,"class":"form-control"})
                    else:
                        default_data[field.html_name] = {}
                        default_data[field.html_name]['label'] = _(field.label)
                        default_data[field.html_name]['field'] = field.as_widget(attrs={"class":"form-control"})
                else:
                    default_data[field.html_name] = {}
                    default_data[field.html_name]['label'] = _(field.label)
                    default_data[field.html_name]['field'] = field.as_widget(attrs={"class":"form-control"})

            # Unnecesary Fields
            del default_data['user']
            del default_data['category']
            del default_data['subcategory']
            del default_data['location']
            del default_data['features']
            del default_data['services']
            del default_data['ambiences']

            # Required by Operation
            if(operation.operation == 'Venta'):
                if(category.name == 'Departamentos'):
                    del default_data['stage']
                    del default_data['deliveryYear']
                else:
                    del default_data['expenses']
                    del default_data['stage']
                    del default_data['deliveryYear']
            elif(operation.operation == 'Alquiler'):
                del default_data['stage']
                del default_data['deliveryYear']
                del default_data['suitableCredit']
                del default_data['providesFunding']
            else: # Emprendimiento
                del default_data['buildingType']                
                del default_data['buildingStatus']
                del default_data['antiqueness']
                del default_data['expenses']
                del default_data['suitableCredit']
                del default_data['providesFunding']

            # Remove by category
            if(category.name == 'Departamentos'):
                del default_data['roofType']
                del default_data['industrialRoofType']
                del default_data['roofHeight']
                del default_data['gateType']
                del default_data['frontGround']
                del default_data['largeGround']
                del default_data['hectares']
                del default_data['fot']
                del default_data['fos']        
            elif(category.name == 'Casas'):         
                del default_data['buildingStatus']       
                del default_data['apartmentsPerFloor']                
                del default_data['floorNumber']
                del default_data['quantityElevators']
                del default_data['industrialRoofType']
                del default_data['roofHeight']
                del default_data['gateType']
                del default_data['quantityBuildingFloors']                                
                del default_data['frontGround']
                del default_data['largeGround']
                del default_data['hectares']
                del default_data['fot']
                del default_data['fos']
            elif(category.name == 'PH'):          
                del default_data['buildingStatus']      
                del default_data['apartmentsPerFloor']                
                del default_data['floorNumber']
                del default_data['quantityElevators']
                del default_data['industrialRoofType']
                del default_data['roofHeight']
                del default_data['gateType']
                del default_data['quantityBuildingFloors']                                
                del default_data['frontGround']
                del default_data['largeGround']
                del default_data['hectares']
                del default_data['fot']
                del default_data['fos']
            elif(category.name == 'Quintas'):
                del default_data['buildingStatus']
                del default_data['apartmentsPerFloor']                
                del default_data['floorNumber']
                del default_data['quantityElevators']
                del default_data['industrialRoofType']
                del default_data['roofHeight']
                del default_data['gateType']
                del default_data['quantityBuildingFloors']                                
                del default_data['frontGround']
                del default_data['largeGround']
                del default_data['hectares']
                del default_data['fot']
                del default_data['fos']
            elif(category.name == 'Terrenos y Lotes'):
                del default_data['antiqueness']                
                del default_data['total_uncovered_meters']
                del default_data['lightness']
                del default_data['orientation']
                del default_data['disposition']
                del default_data['quantityAmbiences']
                del default_data['quantityBathrooms']
                del default_data['quantityBedrooms']
                del default_data['quantityGarages']
                del default_data['garageCoverage']
                del default_data['buildingType']                
                del default_data['buildingStatus']
                del default_data['buildingCategory']
                del default_data['apartmentsPerFloor']
                del default_data['quantityBuildingFloors']
                del default_data['floorNumber']
                del default_data['quantityElevators']
                del default_data['roofType']
                del default_data['industrialRoofType']
                del default_data['roofHeight']
                del default_data['gateType']                
                del default_data['suitableProfessional']
                del default_data['commercialUsage']
            elif(category.name == 'Campos y chacras'):
                del default_data['antiqueness']                
                del default_data['total_uncovered_meters']
                del default_data['lightness']
                del default_data['orientation']
                del default_data['disposition']
                del default_data['quantityAmbiences']
                del default_data['quantityBathrooms']
                del default_data['quantityBedrooms']
                del default_data['quantityGarages']
                del default_data['garageCoverage']
                del default_data['buildingType']                
                del default_data['buildingStatus']
                del default_data['buildingCategory']
                del default_data['apartmentsPerFloor']
                del default_data['quantityBuildingFloors']
                del default_data['floorNumber']
                del default_data['quantityElevators']
                del default_data['roofType']
                del default_data['industrialRoofType']
                del default_data['roofHeight']
                del default_data['gateType']                
                del default_data['suitableProfessional']
                del default_data['commercialUsage']
            elif(category.name == 'Cocheras'):                                
                del default_data['square_meters']
                del default_data['total_uncovered_meters']
                del default_data['lightness']
                del default_data['orientation']
                del default_data['disposition']
                del default_data['quantityAmbiences']
                del default_data['quantityBathrooms']
                del default_data['quantityBedrooms']
                del default_data['quantityGarages']                
                del default_data['buildingType']                
                del default_data['buildingStatus']
                del default_data['buildingCategory']
                del default_data['apartmentsPerFloor']
                del default_data['quantityBuildingFloors']
                del default_data['floorNumber']
                del default_data['quantityElevators']
                del default_data['roofType']
                del default_data['industrialRoofType']
                del default_data['roofHeight']
                del default_data['gateType']
                del default_data['frontGround']
                del default_data['largeGround']
                del default_data['hectares']
                del default_data['fot']
                del default_data['fos']
                del default_data['suitableProfessional']
                del default_data['commercialUsage']
            elif(category.name == 'Galpones, depósitos y edificios industriales'):
                del default_data['disposition']
                del default_data['quantityAmbiences']
                del default_data['quantityBedrooms']
                del default_data['buildingType']                
                del default_data['buildingCategory']
                del default_data['apartmentsPerFloor']                
                del default_data['floorNumber']                
                del default_data['roofType']                                
                del default_data['gateType']                
                del default_data['hectares']                
                del default_data['fos']
                del default_data['suitableProfessional']                
            elif(category.name == 'Locales comerciales'):                
                del default_data['quantityAmbiences']                
                del default_data['quantityBedrooms']                
                del default_data['buildingType']
                del default_data['buildingCategory']
                del default_data['apartmentsPerFloor']
                del default_data['quantityBuildingFloors']
                del default_data['floorNumber']
                del default_data['quantityElevators']
                del default_data['roofType']
                del default_data['industrialRoofType']
                del default_data['roofHeight']
                del default_data['gateType']
                del default_data['frontGround']
                del default_data['largeGround']
                del default_data['hectares']
                del default_data['fot']
                del default_data['fos']
                del default_data['suitableProfessional']
                del default_data['commercialUsage']
            elif(category.name == 'Oficinas'):
                del default_data['roofType']
                del default_data['industrialRoofType']
                del default_data['roofHeight']
                del default_data['gateType']
                del default_data['quantityAmbiences']                
                del default_data['quantityBedrooms']
                del default_data['frontGround']
                del default_data['largeGround']
                del default_data['hectares']
                del default_data['fot']
                del default_data['fos']
                del default_data['suitableProfessional']
                del default_data['commercialUsage']
            elif(category.name == 'Consultorios'):
                del default_data['roofType']
                del default_data['industrialRoofType']
                del default_data['roofHeight']
                del default_data['gateType']
                del default_data['quantityAmbiences']                
                del default_data['quantityBedrooms']
                del default_data['frontGround']
                del default_data['largeGround']
                del default_data['hectares']
                del default_data['fot']
                del default_data['fos']
                del default_data['suitableProfessional']
                del default_data['commercialUsage']
            else:
                del default_data['suitableProfessional']
                del default_data['commercialUsage']

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
