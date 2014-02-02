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
from core.models  import SavedQuery, Alert
from core.forms import SavedQueryForm, AlertForm


class SavedQueryResource(ModelResource):
     """ Class SavedQueryResource saved query endpoint.
        @author: Lionel Cuevas <lionel@hoopemedia.com>"""
     requestHandler = RequestHandler() 

     class Meta:
        allowed_methods = ['post']
        queryset = SavedQuery.objects.all() 
        resource_name = 'saved_query'

     def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/add_logged_out%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('add_logged_out'), name="api_query_add_logged_out"),
            url(r"^(?P<resource_name>%s)/add_logged_in%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('add_logged_in'), name="api_query_add_logged_in"),
            url(r"^(?P<resource_name>%s)/delete%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('delete'), name="api_query_delete"), 
            url(r"^(?P<resource_name>%s)/list%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('list'), name="api_query_list"),            
        ]

     def list(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)
        if request_data:            
            query_list = SavedQuery.objects.filter(user=request.user).order_by('-creation_date')
            paginator = Paginator(query_list.values(), 50)
            if('page' in request_data['pagination']):
                page = request_data['pagination']['page']
            else:
                page = 1
            try:
                querys = paginator.page(page)
            except PageNotAnInteger:
                querys = paginator.page(1)
            except EmptyPage:
                querys = paginator.page(paginator.num_pages)
            if querys:                                      
                return self.create_response(request, {
                    'response':{
                        'data':{
                            'list':list(querys)
                            },
                        'success': True
                        },                    
                })
            else:
                return self.create_response(request, {'response': {'error':'ERR_EMPTY_LIST','success': False }})            
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False}}, HttpUnauthorized)

     def add_logged_out(self, request, **kwargs):
        self.is_secure(request) 
        request_data = self.requestHandler.getDataAuth(request)
        email = request_data['data']['email']
        name = request_data['data']['name']
        query = str(request_data['data']['query'])
        user,created = User.objects.get_or_create(username=email, email=email)
        if created:
            password = User.objects.make_random_password()
            user.set_password(password)
            user.is_active = False
            user.save()
            group = Group.objects.get(name='USER_SAVED_SEARCH')
            group.user_set.add(user)
            group.save()
            saved_query_form = SavedQueryForm()
            saved_query_form.user = user
            saved_query_form.name = name
            saved_query_form.query = query
            if(saved_query_form.is_valid()):
                saved_query = saved_query_form.save()
                alert_form = AlertForm()
                alert_form.user = user
                alert_form.name = 0
                alert_form.query = saved_query
                if(alert_form.is_valid()):
                    alert_form.save()
                    return self.create_response(request, {'response': {'data':'SCC_CREATED','success': False }}, HttpCreated)
                else:
                    return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','data':alert_form.errors,'success': False }})
            else:
                return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','data':saved_query_form.errors,'success': False }})
            # TO-DO: Send email to user with this data

        else:
            return self.create_response(request, {'response': {'error':'ERR_USER_EXISTS','success': False }}, HttpForbidden)            
        
     def add_logged_in(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)
        if request_data:
            user_id = int(request_data['data']['user'])
            name = request_data['data']['name']
            query = request_data['data']['query']
            user = User.objects.get(pk=user_id)            

            saved_query_form = SavedQueryForm()
            saved_query_form.user = user
            saved_query_form.name = name
            saved_query_form.query = query
            try:
                if(saved_query_form.is_valid()):                
                   saved_query = saved_query_form.save()
                   alert_form = AlertForm()
                   alert_form.user = user
                   alert_form.name = 0
                   alert_form.query = saved_query
                   alert_form.save()
                   return self.create_response(request, {'response': {'data':'SCC_CREATED','success': True }}, HttpCreated)
                else:                
                    return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','data':saved_query_form.errors,'success': False }})
            except ValidationError as e:
                    pass
                    return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','data':saved_query_form.errors,'success': False }})             
        else:                
            return self.create_response(request, {'response': {'error':'ERR_INVALID_KEY','success': False }}, HttpUnauthorized)

     def delete(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)
        if request_data:
            id = int(request_data['data']['id'])
            query = SavedQuery.objects.get(pk=id)
            user_id = int(request_data['data']['user'])
            user = User.objects.get(pk=user_id)                        
            if(user.pk == query.user.pk):        
               query.delete()               
               return self.create_response(request, {'response': {'data':'SCC_DELETED','success': True }})
            else:                
                return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)
        else:                
            return self.create_response(request, {'response': {'error':'ERR_INVALID_KEY','success': False }}, HttpUnauthorized)       
         
     def is_secure(self, request):         
         #if(request.is_secure()):                
        if(self.method_check(request, allowed=['post']) and request.user.is_authenticated()
            and self.throttle_check(request) == None):            
            self.log_throttled_access(request)            
        else: 
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)