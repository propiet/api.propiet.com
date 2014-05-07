from django import forms            
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm 
from core.models.user_profile import UserProfile

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
			user.save()
			group = Group.objects.get(name=role)
			group.user_set.add(user)
			group.save()
			profile = UserProfile()
			profile.user = user;
			profile.phone = phone;
			profile.agency_name = agency_name;
			profile.save()
		return user