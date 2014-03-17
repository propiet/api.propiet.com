# -*- coding: utf-8 -*-
# Django imports
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models.loading import get_model
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
from core.models  import Post, Location, Property
from core.forms import PostForm, GetObjectForm, LocationForm, PostAgentForm, PostStatusForm
from core.constants import *


class PostResource(ModelResource):
     """ Class PostResource post endpoint.
        @author: Lionel Cuevas <lionel@hoopemedia.com>"""

     requestHandler = RequestHandler()
     serializer = SerializationHandler()

     class Meta:
        allowed_methods = ['post']
        queryset = Post.objects.all() 
        resource_name = 'post'        

     def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/search%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('search'), name="api_post_search"),
            url(r"^(?P<resource_name>%s)/list%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('list'), name="api_post_list"),
            url(r"^(?P<resource_name>%s)/add%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('add'), name="api_post_add"), 
            url(r"^(?P<resource_name>%s)/update%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('update'), name="api_post_update"),
            url(r"^(?P<resource_name>%s)/status%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('status'), name="api_post_status"),
            url(r"^(?P<resource_name>%s)/assign%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('assign'), name="api_post_assign"),
            url(r"^(?P<resource_name>%s)/unassign%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('unassign'), name="api_post_unassign"),
            url(r"^(?P<resource_name>%s)/get%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get'), name="api_post_get"),
            url(r"^(?P<resource_name>%s)/get_form%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_form'), name="api_post_get_form"),          
        ]

     def search(self, request, **kwargs):        
        request_data = self.requestHandler.getDataAuth(request)
        kwargs = {}
        if request_data:
            if('operation' in request_data):
                kwargs['operation'] = request_data['operation']

            if('category' in request_data):
                kwargs['category'] = request_data['category']

            if('region' in request_data):
                kwargs['region'] = request_data['region']

            if('city' in request_data):
                cities = []                
                for i in request_data['city']:                                        
                    cities.append(i['id'])
                kwargs['city__in'] = cities

            if('price_min' in request_data):
                kwargs['price__gte'] = request_data['price_min']

            if('price_max' in request_data):
                kwargs['price__lte'] = request_data['price_max']

            if('currency' in request_data):
                kwargs['currency'] = request_data['currency']

            kwargs['status'] = 3 #Retrieve only Published posts
            post_list = Post.objects.filter(**kwargs).order_by('-creation_date')
            paginator = Paginator(post_list.values(), 50)
            if('page' in request_data['pagination']):                
                page = request_data['pagination']['page']
            else:
                page = 1
            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)            
            if posts:                                      
                return self.create_response(request, {
                    'response':{
                        'data':{
                            'list':list(posts)
                            },
                        'pagination': {
                            'page': page,
                            'count': paginator.count,
                            'num_pages': paginator.num_pages,
                            'page_range': paginator.page_range,
                            },
                        'success': True
                        },                    
                })
            else:
                return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False}}, HttpUnauthorized)
               
     def list(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)
        if request_data:
            user = int(request_data['data']['user'])
            status = int(request_data['data']['status'])
            agent = int(request_data['data']['agent'])

            if(agent == 0 and user > 0 and status >= 0):
                post_list = Post.objects.filter(user=user,status=status).order_by('-creation_date')
            elif (agent == 0 and user == 0 and status >= 0):
                post_list = Post.objects.filter(status=status,agent=None).order_by('-creation_date')
            elif (agent > 0 and user == 0 and status < 0):
                post_list = Post.objects.filter(agent=agent).order_by('-creation_date')
            else:
                post_list = Post.objects.filter(user=user,status=status,agent=agent).order_by('-creation_date')

            paginator = Paginator(post_list.values(), 50)
            if('page' in request_data['pagination']):
                page = request_data['pagination']['page']
            else:
                page = 1
            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
            if posts:                                      
                return self.create_response(request, {
                    'response':{
                        'data':{
                            'list':list(posts)
                            },
                        'pagination': {
                            'page': page,
                            'count': paginator.count,
                            'num_pages': paginator.num_pages,
                            'page_range': paginator.page_range,
                            },
                        'success': True
                        },                    
                })
            else:
                return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})            
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False}}, HttpUnauthorized)

     def get(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)
        if request_data:
            post_id = int(request_data['data']['id'])            
            post = Post.objects.get(pk=post_id)
            if post:
                property = Property.objects.get(pk=post.property.pk)
                location = Location.objects.get(property=post.property.pk)
                user = User.objects.get(pk=post.user.pk)
                if(post.agent != None):
                    agent = User.objects.get(pk=post.agent.pk)                
                        
                    return self.create_response(request, {
                        'response':{
                            'data':{
                                'post_data': {
                                    'id': post.pk,
                                    'category': {'id':post.category.pk, 'name':post.category.name},
                                    'operation': {'id':post.operation.pk, 'name':post.operation.operation},
                                    'price': post.price,
                                    'currency': {'id':post.currency.pk, 'name':post.currency.name},
                                    'title': post.title,
                                    'status': post.status,
                                    'description': post.description,
                                    'region': {'id':post.region.pk, 'name':post.region.name},
                                    'city':{'id':post.city.pk, 'name':post.city.name},
                                },
                                'post':self.serializer.encode(post),
                                'property':self.serializer.encode(property),                            
                                'location':self.serializer.encode(location),
                                'user':self.serializer.encode(user),
                                'agent':self.serializer.encode(agent),
                                },                        
                            'success': True
                            },                    
                    })
                else:
                    return self.create_response(request, {
                        'response':{
                            'data':{
                                'post_data': {
                                    'id': post.pk,
                                    'category': {'id':post.category.pk, 'name':post.category.name},
                                    'operation': {'id':post.operation.pk, 'name':post.operation.operation},
                                    'price': post.price,
                                    'currency': {'id':post.currency.pk, 'name':post.currency.name},
                                    'title': post.title,
                                    'status': post.status,
                                    'description': post.description,
                                    'region': {'id':post.region.pk, 'name':post.region.name},
                                    'city':{'id':post.city.pk, 'name':post.city.name},
                                },
                                'post':self.serializer.encode(post),
                                'property':self.serializer.encode(property),                            
                                'location':self.serializer.encode(location),
                                'user':self.serializer.encode(user),                                
                                },                        
                            'success': True
                            },                    
                    })
            else:
                return self.create_response(request, {'response': {'error':'ERR_NOT_FOUND','success': False }})            
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False}}, HttpUnauthorized)
     
     def add(self, request, **kwargs):       
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)        
        if request_data:
            locationForm = LocationForm(request_data['data']['location'])
            try:
                if(locationForm.is_valid()):
                    location = locationForm.save()
                    request_data['data']['property']['location'] = location.pk
                    propertyForm = self._get_property_form(request_data['data']['property'])
                    propertyForm.location = location.pk

                    if(propertyForm.is_valid()):
                        unit = propertyForm.save()
                        request_data['data']['post']['property'] = unit.pk
                        request_data['data']['post']['region'] = location.region.pk
                        request_data['data']['post']['city'] = location.city.pk
                        postForm = PostForm(request_data['data']['post'])
                        postForm.property = unit.pk
                        postForm.region = location.region.pk
                        postForm.city = location.city.pk
                        if(postForm.is_valid()):
                            postForm.save()
                            return self.create_response(request, {'response': {'data':'SCC_CREATED','success': True }},HttpCreated)
                        else:
                            return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':postForm.errors,'success': False }})
                    else:
                        return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':propertyForm.errors,'success': False }})                   
                else:
                    return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':locationForm.errors,'success': False }}) 
            except ValidationError as e:
                pass
                return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':{'location_form': locationForm.errors, 'property_form':propertyForm.errors, 'post_form':postForm.errors},'success': False }})
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)
     
     def update(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)        
        if request_data:

            location_id = request_data['data']['location']['id']
            location = Location.objects.get(pk=location_id)
            locationForm = LocationForm(request_data['data']['location'], instance=location)
            try:
                if(locationForm.is_valid()):
                    location = locationForm.save()
                    
                    property = self._get_property_model(request_data['data']['property'])
                    propertyForm = self._get_property_form(request_data['data']['property'], instance=property)
                    if(propertyForm.is_valid()):
                        unit = propertyForm.save()
                        
                        post_id = request_data['data']['post']['id']
                        post = Location.objects.get(pk=post_id)
                        postForm = PostForm(request_data['data']['post'], instance=post)
                        if(postForm.is_valid()):
                            postForm.save()
                            return self.create_response(request, {'response': {'data':'SCC_UPDATED','success': True }})
                        else:
                            return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':postForm.errors,'success': False }})
                    else:
                        return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':propertyForm.errors,'success': False }})                   
                else:
                    return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':locationForm.errors,'success': False }}) 
            except ValidationError as e:
                pass
                return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':{'location_form': locationForm.errors, 'property_form':propertyForm.errors, 'post_form':postForm.errors},'success': False }})
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)

     def status(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)        
        if request_data:
            post_id = int(request_data['data']['post'])
            status = int(request_data['data']['status'])
            form_data = {'status': status}
            post = Post.objects.get(pk=post_id)
            postStatusForm = PostStatusForm(form_data, instance=post)
            try:
                if(postStatusForm.is_valid()):
                    postStatusForm.save()
                    return self.create_response(request, {'response': {'data':'SCC_UPDATED','success': True }})
                else:
                    return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':postStatusForm.errors,'success': False }}) 
            except ValidationError as e:
                pass
                return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':postStatusForm.errors,'success': False }})
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)

     def assign(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)        
        if request_data:
            posts = request_data['data']['posts']
            agent_id = request_data['data']['agent']
            form_data = {'agent': int(agent_id), 'status':3}

            for post_id in posts:
                post = Post.objects.get(pk=int(post_id))                
                postAgentForm = PostAgentForm(form_data, instance=post)
                try:
                    if(postAgentForm.is_valid()):
                        postAgentForm.save()                        
                    else:
                        return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':postAgentForm.errors,'success': False }}) 
                except ValidationError as e:
                    pass
                    return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':postAgentForm.errors,'success': False }})
            return self.create_response(request, {'response': {'data':'SCC_UPDATED','success': True }})      
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)

     def unassign(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)        
        if request_data:
            posts = request_data['data']['posts']
            agent_id = request_data['data']['agent']
            form_data = {'agent': None, 'status': 1}

            for post_id in posts:
                post = Post.objects.get(pk=int(post_id), agent=int(agent_id))                
                postAgentForm = PostAgentForm(form_data, instance=post)
                try:
                    if(postAgentForm.is_valid()):
                        postAgentForm.save()                        
                    else:
                        return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':postAgentForm.errors,'success': False }}) 
                except ValidationError as e:
                    pass
                    return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':postAgentForm.errors,'success': False }})
            return self.create_response(request, {'response': {'data':'SCC_UPDATED','success': True }})
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)

     def _get_property_form(self, data):        
        category = int(data['category'])
        subcategory = int(data['subcategory'])
        model = str(PROPERTYFORM[category][subcategory])
        form_class = GetObjectForm(model)
        form = form_class(data)
        return form

     def _get_property_model(self, data):
        property_id = int(data['id'])
        category = int(data['category'])
        subcategory = int(data['subcategory'])
        model_name = str(PROPERTYFORM[category][subcategory])
        model_class = get_model(app_label='core', model_name=model_name)
        model = model_class.objects.get(pk=property_id)
        return model
     
     def get_form(self, request, **kwargs):
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            post_id = int(request_data['data']['id'])
            post = Post.objects.get(pk=post_id)
            category = int(post.property.category.pk)
            subcategory = int(post.property.subcategory.pk)
            operation_type = int(post.operation.pk)            
            model = str(PROPERTYFORM[category][subcategory])
            form_class = GetObjectForm(model)
            form = form_class(instance=post.property)
            default_data = {}

            for field in form:
                if(OPERATION_TYPE[operation_type] == 'Venta' or OPERATION_TYPE[operation_type] == 'Emprendimiento'):
                    if (field.label != 'Ambiences' and field.label != 'Location' 
                    and field.label != 'Category' and field.label != 'Subcategory'
                    and field.label != 'User' and field.label != 'Services'
                    and field.label != 'Features' and field.label != 'Expenses'):

                        field_label = FIELDS_LABELS[field.html_name]
                        default_data[field_label] = field.as_widget(attrs={"class":"form-control"})
                else:
                    if (field.label != 'Ambiences' and field.label != 'Location' 
                    and field.label != 'Category' and field.label != 'Subcategory'
                    and field.label != 'User' and field.label != 'Services'
                    and field.label != 'Features' and field.label != 'ProvidesFunding'
                    and field.label != 'SuitableCredit'):

                        field_label = FIELDS_LABELS[field.html_name]
                        default_data[field_label] = field.as_widget(attrs={"class":"form-control"})

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