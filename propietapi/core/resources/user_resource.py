# -*- coding: utf-8 -*-
# Django imports
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf.urls import *
from django.utils import simplejson
from django.db import IntegrityError
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.mail import send_mail
import datetime, random, sha
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
            url(r"^(?P<resource_name>%s)/activate%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('activate'), name="api_user_activate"),
            url(r"^(?P<resource_name>%s)/forgot_password%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('forgot_password'), name="api_user_forgot_password"),
            url(r"^(?P<resource_name>%s)/contact_agent%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('contact_agent'), name="api_user_contact_agent"),
            url(r"^(?P<resource_name>%s)/sell_agent%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('sell_agent'), name="api_user_sell_agent"),
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
                user_profile = UserProfile.objects.get(user=user)
                return self.create_response(request, {
                    'response':{
                        'data':{
                            'user_id': user.pk,
                            'username': user.username,
                            'user_email': user.email,
                            'user_firstname': user.first_name,
                            'user_lastname': user.last_name,
                            'user_token': api_key.key,                            
                            'user_role': user_group,
                            'user_phone': user_profile.phone
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
        request_data = self.requestHandler.getData(request)
        username = request_data['username']                
        if username:
            user = User.objects.get(username=username)
            api_key = ApiKey.objects.get(user=user)
            user_group = user.groups.all()[0]
            user_profile = UserProfile.objects.get(user=user)    
            return self.create_response(request, {
                'response':{
                    'data':{
                        'id': user.pk,
                        'username': user.username,
                        'email': user.email,
                        'firstname': user.first_name,
                        'lastname': user.last_name,
                        'role': user_group,
                        'phone': user_profile.phone
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
            user_id = request_data['data']['id']
            user = User.objects.get(pk=user_id)
            profile = UserProfile.objects.get(pk=user)

            if(user):
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
            except IntegrityError as e:
                pass
                return self.create_response(request, {'response': {'error':'ERR_USER_EXISTS','form':request_data['data'],'data':userRegistrationForm.errors,'success': False }})
            except IntegrityError as e:
                pass
                return self.create_response(request, {'response': {'error':'ERR_DATABASE','form':request_data['data'],'data':userRegistrationForm.errors,'success': False }})
        else:
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)
     
     def change_password(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)
        if request_data:
            user_id = request_data['data']['id']
            user_raw_pass = request_data['data']['old_password']
            user = User.objects.get(pk=user_id)

            if(user):
                if(user.check_password(user_raw_pass) == True):
                    try:
                        if(request_data['data']['password1'] == request_data['data']['password2']):
                           user.set_password(request_data['data']['password1'])
                           user.save()

                           email_subject = '%s, Se ha modificado su clave exitosamente' % (user.first_name)
                           email_body = "Hola %s, Se ha modificado su clave exitosamente!\n\nPara administrar su perfil acceda a:\n\nhttp://www.propiet.com/perfil \n\n" % (user.first_name)
                           send_mail(email_subject,email_body,'propiet@inboxapp.me',[user.email])

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

     def activate(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getData(request)
        if request_data:
            activation_key = request_data['data']['activation_key']
            try:
                profile = UserProfile.objects.get(activation_key=activation_key)            
                if(profile):
                    if profile.key_expires < datetime.datetime.today():
                        salt = sha.new(str(random.random())).hexdigest()[:5]
                        profile.activation_key = sha.new(salt+profile.user.username).hexdigest()
                        profile.key_expires = datetime.datetime.today() + datetime.timedelta(2)
                        profile.save()
                        email_subject = '%s, Activa tu cuenta en propiet.com' % (profile.user.first_name)
                        email_body = "%s, debido a que expiro tu anterior enlace de activacion de propiet.com\n\nTe enviamos uno nuevo, haz click en el siguiente enlace para activar tu cuenta vigente durante 48 horas:\n\nhttp://www.propiet.com/confirmacion/%s \n\n" % (profile.user.first_name, profile.activation_key)
                        send_mail(email_subject,email_body,'propiet@inboxapp.me',[profile.user.email])
                        return self.create_response(request, {'response': {'error':'ERR_USER_EXPIRED','success': False }})
                    user_account = profile.user
                    user_account.is_active = True
                    user_account.save()
                    profile.key_expires = datetime.datetime.today() - datetime.timedelta(2)
                    profile.save()
                    email_subject = 'Felicidades %s, ya sos parte de propiet.com' % (profile.user.first_name)
                    email_body = "%s, gracias confirmar tu cuenta!\n\nPropiet.com, Una mejor manera de vender y encontrar su hogar.\n\nhttp://www.propiet.com \n\n" % (profile.user.first_name)
                    send_mail(email_subject,email_body,'propiet@inboxapp.me',[profile.user.email])

                    return self.create_response(request, {'response': {'data':'SCC_UPDATED','success': True }})
                else:                
                    return self.create_response(request, {'response': {'data':'ERR_NOT_FOUND','success': False }})
            except ObjectDoesNotExist:
                pass
                return self.create_response(request, {'response': {'data':'ERR_NOT_FOUND','success': False }})
        else:                
            return self.create_response(request, {'response': {'data':'ERR_INVALID_KEY','success': False }}, HttpUnauthorized)

     def forgot_password(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            email = request_data['data']['email']
            try:
                user = User.objects.get(email=email)
                
                if(user):
                    password = User.objects.make_random_password()
                    user.set_password(password)
                    user.save()
                    email_subject = 'Recuperar Clave'
                    email_body = "Hola %s, Se ha generado una nueva clave.\n\nIngresar en: http://www.propiet.com/login\nEmail: %s \nClave: %s \n\nNo olvides que para cambiar esta clave auto-generada debes acceder a:\nhttp://www.propiet.com/perfil \n\n" % (user.first_name,user.email,password)
                    send_mail(email_subject,email_body,'propiet@inboxapp.me',[user.email])
                    return self.create_response(request, {'response': {'data':'SCC_UPDATED','success': True }})                
                else:                
                    return self.create_response(request, {'response': {'data':'ERR_NOT_FOUND','success': False }})
            except ObjectDoesNotExist:
                pass
                return self.create_response(request, {'response': {'data':'ERR_NOT_FOUND','success': False }})
        else:                
            return self.create_response(request, {'response': {'data':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)

     def contact_agent(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            agent_id = request_data['data']['agent']
            name = request_data['data']['name']
            phone = request_data['data']['phone']
            email = request_data['data']['email']
            message = request_data['data']['message']
            post_url = request_data['data']['post']
            try:
                agent = User.objects.get(pk=agent_id)
                
                if(agent):                    
                    email_subject = '%s, hay un usuario interesado en tu propiedad' % (agent.first_name)
                    email_body = "Hola %s, hay un usuario interesado en una de tus propiedades.\n\n Nombre: %s \nTel: %s \nEmail: %s \nMensaje: %s \nPropiedad: %s" % (agent.first_name, name, phone, email, message, post_url)
                    send_mail(email_subject,email_body,'propiet@inboxapp.me',[agent.email])
                    return self.create_response(request, {'response': {'data':'SCC_UPDATED','success': True }})                
                else:                
                    return self.create_response(request, {'response': {'data':'ERR_NOT_FOUND','success': False }})
            except ObjectDoesNotExist:
                pass
                return self.create_response(request, {'response': {'data':'ERR_NOT_FOUND','success': False }})
        else:                
            return self.create_response(request, {'response': {'data':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)
     
     def sell_agent(self, request, **kwargs):
        self.is_secure(request)
        request_data = self.requestHandler.getDataAuth(request)
        if request_data:
            lastname = request_data['data']['lastname']
            firstname = request_data['data']['firstname']
            phone = request_data['data']['phone']
            email = request_data['data']['email']
            message = request_data['data']['message']
            address = request_data['data']['address']
                               
            email_subject = 'Nuevo pedido de tasación'
            email_body = "Nombre: %s \nApellido: %s \nTel: %s \nEmail: %s \Dirección: %s \nDescripción: %s" % (firstname, lastname, phone, email, address, message)
            send_mail(email_subject,email_body,'propiet@inboxapp.me',['mfunes@propiet.com'])              
        else:                
            return self.create_response(request, {'response': {'data':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)

     def is_secure(self, request):         
         #if(request.is_secure()):                
        if(self.method_check(request, allowed=['post']) and request.user.is_authenticated()
            and self.throttle_check(request) == None):            
            self.log_throttled_access(request)            
        else: 
            return self.create_response(request, {'response': {'error':'ERR_UNAUTHORIZED','success': False }}, HttpUnauthorized)