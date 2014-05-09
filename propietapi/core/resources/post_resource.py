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
from core.models  import Post, Location, Property, UserProfile, PostPhoto
from core.forms import PostForm, GetObjectForm, LocationForm, PostAgentForm, PostStatusForm, PropertyForm, PostPhotoForm
from core.constants import *
from django.utils.translation import ugettext_lazy as _
#from PIL import Image
#import base64
#import cStringIO
from time import time
from django.core.files.base import ContentFile


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
            url(r"^(?P<resource_name>%s)/agent%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('agent'), name="api_post_get_agent"),
            url(r"^(?P<resource_name>%s)/photo/add%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('addPhoto'), name="api_post_photo_add"),
            url(r"^(?P<resource_name>%s)/photo/remove%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('removePhoto'), name="api_post_photo_remove"),
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
                    agent_profile = UserProfile.objects.get(pk=post.agent.pk)                
                    user_profile = UserProfile.objects.get(pk=user.pk)

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
                                    'hidden_note': post.hidden_note,
                                    'region': {'id':post.region.pk, 'name':post.region.name},
                                    'city':{'id':post.city.pk, 'name':post.city.name},
                                },
                                'post':self.serializer.encode(post),
                                'property':self.serializer.encode(property),
                                'services':self.serializer.encode(property.services.all()),
                                'features':self.serializer.encode(property.features.all()),
                                'ambiences':self.serializer.encode(property.ambiences.all()),
                                'location':self.serializer.encode(location),
                                'user':self.serializer.encode(user),
                                'user_profile':self.serializer.encode(user_profile),
                                'agent':self.serializer.encode(agent),
                                'agent_profile':self.serializer.encode(agent_profile),
                                'images':self.serializer.encode(PostPhoto.objects.filter(post=post.pk)),
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
                                    'hidden_note': post.hidden_note,
                                    'region': {'id':post.region.pk, 'name':post.region.name},
                                    'city':{'id':post.city.pk, 'name':post.city.name},
                                },
                                'post':self.serializer.encode(post),
                                'property':self.serializer.encode(property),
                                'services':self.serializer.encode(property.services.all()),
                                'features':self.serializer.encode(property.features.all()),
                                'ambiences':self.serializer.encode(property.ambiences.all()),                           
                                'location':self.serializer.encode(location),
                                'user':self.serializer.encode(user),
                                'user_profile':self.serializer.encode(user_profile),
                                'images':self.serializer.encode(PostPhoto.objects.filter(post=post.pk)),              
                                },                        
                            'success': True
                            },                    
                    })
            else:
                return self.create_response(request, {'response': {'error':'ERR_NOT_FOUND','success': False }})            
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False}}, HttpUnauthorized)

     def agent(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)
        if request_data:
            agent_id = int(request_data['data']['id'])            
            agent = User.objects.get(pk=agent_id)
            if agent:
                user_group = agent.groups.all()[0]
                user_profile = UserProfile.objects.get(user=agent)    
                return self.create_response(request, {
                    'response':{
                        'data':{
                            'id': agent.pk,
                            'username': agent.username,
                            'email': agent.email,
                            'firstname': agent.first_name,
                            'lastname': agent.last_name,
                            'role': user_group,
                            'phone': user_profile.phone
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
                    propertyForm = PropertyForm(request_data['data']['property'])
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
                            post = postForm.save()
                            return self.create_response(request, {'response': {'data':'SCC_CREATED','id':post.pk,'success': True }},HttpCreated)
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
                    category = int(request_data['data']['property']['category'])
                    subcategory = int(request_data['data']['property']['subcategory'])

                    post_id = request_data['data']['post']['id']
                    post = Post.objects.get(pk=post_id)

                    property_id = request_data['data']['property']['id']
                    property = Property.objects.get(pk=property_id)
                    
                    request_data['data']['property']['location'] = property.location.pk
                    propertyForm = PropertyForm(request_data['data']['property'], instance=property)                    

                    if(propertyForm.is_valid()):
                        unit = propertyForm.save()

                        request_data['data']['post']['property'] = post.property.pk
                        request_data['data']['post']['region'] = location.region.pk
                        request_data['data']['post']['city'] = location.city.pk
                        request_data['data']['post']['status'] = post.status
                        postForm = PostForm(request_data['data']['post'], instance=post)
                        postForm.property = unit.pk
                        postForm.region = location.region.pk
                        postForm.city = location.city.pk

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

     def addPhoto(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)        
        if request_data:
            post_id = int(request_data['data']['post'])
            base64_string = str(request_data['data']['file'])

            filename = "uploaded_image%s.png" % str(time()).replace('.','_')      
            # saving decoded image to database
            decoded_image = base64_string.decode('base64')
            post = Post.objects.get(pk=post_id)
            post_photo = PostPhoto()
            post_photo.file = ContentFile(decoded_image, filename)
            post_photo.post = post
            post_photo.save()
            
            #form_data = {'post': int(post_id), 'file':pic}            
            #postPhotoForm = PostPhotoForm(form_data)
            try:
                return self.create_response(request, {'response': {'data':'SCC_UPDATED','success': True }})      
            #    if(postPhotoForm.is_valid()):
            #        postPhotoForm.save()                        
            #    else:
            #        return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':postPhotoForm.errors,'success': False }}) 
            except ValidationError as e:
                pass
                return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':postPhotoForm.errors,'success': False }})
            return self.create_response(request, {'response': {'data':'SCC_UPDATED','success': True }})      
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)
     
     def removePhoto(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)        
        if request_data:
            pic_id = int(request_data['data']['id'])                                    
            try:
                pic = PostPhoto.objects.get(pk=pic_id)
                pic.delete()
                return self.create_response(request, {'response': {'data':'SCC_DELETED','success': True }})      
            except ValidationError as e:
                pass
                return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':postPhotoForm.errors,'success': False }})
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
            category = post.property.category
            subcategory = post.property.subcategory
            operation = post.operation

            form = PropertyForm(instance=post.property)
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
                del default_data['buildingCondition']
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
                del default_data['buildingCondition']
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
                del default_data['buildingCondition']
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
                del default_data['total_meters']
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
                del default_data['buildingCondition']
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
                del default_data['buildingCondition']
                del default_data['buildingCategory']
                del default_data['apartmentsPerFloor']                
                del default_data['floorNumber']                
                del default_data['roofType']                                
                del default_data['gateType']                
                del default_data['hectares']                
                del default_data['fos']
                del default_data['suitableProfessional']                
            elif(category.name == 'Locales comerciales'):                
                del default_data['total_meters']                
                del default_data['quantityAmbiences']                
                del default_data['quantityBedrooms']                
                del default_data['buildingType']
                del default_data['buildingCondition']                
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