# -*- coding: utf-8 -*-
from django import forms            
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm 
from core.models.user_profile import UserProfile
import datetime, random, sha
from django.core.mail import send_mail

class UserRegistrationForm(UserCreationForm):
	username = forms.CharField(required = False)
	email = forms.EmailField(required = True)
	first_name = forms.CharField(required = True)
	last_name = forms.CharField(required = True)
	agency_name = forms.CharField(required = True)
	phone = forms.IntegerField(required = True)
	role = forms.CharField(required = True)

	class Meta:
		model = User
		fields = ('email', 'password1', 'password2')

	def save(self,commit = True):
		user = super(UserRegistrationForm, self).save(commit = False)
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		agency_name = self.cleaned_data['agency_name']
		phone = int(self.cleaned_data['phone'])
		role = self.cleaned_data['role']
		if commit:
			user.is_active = False
			user.save()
			group = Group.objects.get(name=role)
			group.user_set.add(user)
			group.save()
			profile = UserProfile()
			profile.user = user
			profile.phone = phone
			profile.agency_name = agency_name
			salt = sha.new(str(random.random())).hexdigest()[:5]
			profile.activation_key = sha.new(salt+user.username).hexdigest()
			profile.key_expires = datetime.datetime.today() + datetime.timedelta(2)
			profile.save()
			email_subject = '%s, Gracias por registrarte en propiet.com' % (user.first_name)
			email_body = "Hola %s, gracias por registrarte en propiet.com!\n\nPara completar tu registro, haz click en el siguiente enlace vigente durante 48 horas:\n\nhttp://www.propiet.com/confirmacion/%s \n\n" % (user.first_name, profile.activation_key)
			send_mail(email_subject,email_body,'propiet@inboxapp.me',[user.email])
		return user