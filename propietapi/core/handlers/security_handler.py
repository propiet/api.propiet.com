from django.contrib.auth.models import User
#from core.models import Agency
from functools import wraps
from django.http import HttpResponseRedirect
from django.conf import settings
from core.handlers.crypt_handler import CryptHandler
from tastypie.models import ApiKey


"""
Class Security perform user Security checks.
@author: Lionel Cuevas <lionel@hoopemedia.com>"""

class SecurityHandler():
	class Meta:
		app_label = 'core'

	def has_perm(self, request, data):
		""" Checks the Agency is owned by the user """
		user = request.user
		user_agency = Agency.objects.get(user=user)
		
		if int(data['agency']) == user_agency.agency_id or user.is_superuser:
			response = True
		else:
			response = False
		return response

	def is_superuser(self, request):
		if request.user.is_superuser:
			response = True
		else:
			response = False
		return response

	def is_valid_signature(self, request):
		api_key = request.POST.get('api_key')
		username = request.POST.get('username')
		signature = request.POST.get('signature')
		crypt = CryptHandler()
		gen_sign = crypt.get_signature(api_key, username)
		if(gen_sign == signature):
			return True
		else:
			return False

	def is_valid_key(self, request):
		try:

			api_key = request.POST.get('k')			
			user_api = ApiKey.objects.get(key=api_key)
			if(user_api.key):
				return True
			else:
				return False
		except ApiKey.DoesNotExist as e:
			pass
        	return e