# Django imports
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf.urls import *
from django.utils import simplejson
from django.core.exceptions import ValidationError
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
from core.models  import UserProfile
from core.forms import UserForm, UserProfileForm, UserRegistrationForm


class UserResource(ModelResource):
     """ Class UserResource user endpoint.
        @author: Lionel Cuevas <lionel@hoopemedia.com>"""
     requestHandler = RequestHandler() 

     class Meta:
        allowed_methods = ['post']
        queryset = User.objects.all() 
        resource_name = 'user'        

     def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/auth%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('login'), name="api_login"),
            url(r"^(?P<resource_name>%s)/logout%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('logout'), name="api_logout"), 
            url(r"^(?P<resource_name>%s)/update%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('update'), name="api_user_edit"),
            url(r"^(?P<resource_name>%s)/add%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('add'), name="api_user_add"),
            url(r"^(?P<resource_name>%s)/chpwd%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('change_password'), name="api_user_chpwd"),
            url(r"^(?P<resource_name>%s)/me%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('me'), name="api_user_me"),
        ]

     def login(self, request, **kwargs):
        self.is_secure(request) 
        data = self.requestHandler.getDataAuth(request)
        username = data['username']        
        password = data['password']
        user = authenticate(username=username, password=password)                
        if user:
            if user.is_active:
                login(request, user)
                api_key = ApiKey.objects.get(user=user)
                user_group = user.groups.all()[0]          
                return self.create_response(request, {
                    'response':{
                        'data':{
                            'user_id': user.pk,
                            'username': user.username,
                            'user_email': user.email,
                            'user_firstname': user.first_name,
                            'user_lastname': user.last_name,
                            'user_token': api_key.key,                            
                            'user_role': user_group
                            },
                        'success': True
                        },                    
                })
            else:
                return self.create_response(request, {'response': {'error':'ERR_USER_INACTIVE','success': False }}, HttpForbidden)                
        else:
            return self.create_response(request, {'response': {'error':'ERR_USER_INVALID','success': False }}, HttpUnauthorized)            

     def logout(self, request, **kwargs):
         self.method_check(request, allowed=['get','post'])
         if request.user and request.user.is_authenticated():
             logout(request)
             return self.create_response(request, {'response': { 'success': True }})
         else:
             return self.create_response(request, {'response': { 'success': False }}, HttpUnauthorized)    

     def me(self, request, **kwargs):
        self.is_secure(request) 
        data = self.requestHandler.getDataAuth(request)
        username = data['username']        
        self.method_check(request, allowed=['get','post'])
        if request.user and request.user.is_authenticated() and username == request.user.username:
            user = request.user
            api_key = ApiKey.objects.get(user=user)
            user_group = user.groups.all()[0]          
            return self.create_response(request, {
                'response':{
                    'data':{
                        'user_id': user.pk,
                        'username': user.username,
                        'user_email': user.email,
                        'user_firstname': user.first_name,
                        'user_lastname': user.last_name,
                        'user_token': api_key.key,                            
                        'user_role': user_group
                        },
                    'success': True
                    },                    
            })
        else:
            return self.create_response(request, {'response': {'error':'ERR_USER_INVALID','success': False }}, HttpUnauthorized)

     def update(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)
        if request_data:
            user_id = request_data['data']['user_id']
            user = User.objects.get(pk=user_id)
            profile = UserProfile.objects.get(pk=user)

            if(str(request.user.id) == user_id):
                userForm = UserForm(request_data['data'], instance=user)
                userProfileForm = UserProfileForm(request_data['data'], instance=profile) 
                try:
                    if(userForm.is_valid() and userProfileForm.is_valid()):
                       userForm.save()
                       userProfileForm.save()
                       return self.create_response(request, {'response': {'data':'SCC_UPDATED','success': True }})
                    else:            
                        return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','data':userProfileForm.errors,'user_data':userForm.errors,'success': False }})
                except ValidationError as e:
                    pass
                    return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','data':userProfileForm.errors,'user_data':userForm.errors,'success': False }})             
            else:                
                return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)
        else:                
            return self.create_response(request, {'response': {'error':'ERR_INVALID_KEY','success': False }}, HttpUnauthorized)
    
     def add(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:              
            userRegistrationForm = UserRegistrationForm(request_data['data'])            
            try:            
                if(userRegistrationForm.is_valid()):                           
                   userRegistrationForm.save()
                   return self.create_response(request, {'response': {'data':'SCC_CREATED','success': True }},HttpCreated)
                else:            
                    return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':userRegistrationForm.errors,'success': False }})     
            except ValidationError as e:
                pass
                return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','form':request_data['data'],'data':userRegistrationForm.errors,'success': False }})             
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)
     
     def change_password(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)
        if request_data:
            user_id = request_data['data']['user_id']
            user_raw_pass = request_data['data']['old_password']
            user = User.objects.get(pk=user_id)

            if(str(request.user.id) == user_id):
                if(user.check_password(user_raw_pass) == True):
                    try:
                        if(request_data['data']['password1'] == request_data['data']['password2']):
                           user.set_password(request_data['data']['password1'])
                           user.save()
                           return self.create_response(request, {'response': {'data':'SCC_UPDATED','success': True }})
                        else:            
                            return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','data':{'password1': 'passwords not match'},'success': False }})
                    except ValidationError as e:
                        pass
                        return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','data':{'old_password': 'invalid field'},'success': False }})
                else:
                    return self.create_response(request, {'response': {'error':'ERR_FORM_INVALID','data':{'old_password': 'invalid field'},'success': False }})
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