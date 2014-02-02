from core.handlers.serializer import SerializationHandler
from core.handlers.crypt_handler import CryptHandler
from core.handlers.security_handler import SecurityHandler

class RequestHandler():
	"""Class RequestHandler handles parsing of requests params.
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""

	serializer = SerializationHandler()
	crypt = CryptHandler()

	class Meta:
	    app_label = 'core'

	def getData(self, request, **options):
		""" Returns data object from request """
		if(request.method == 'POST'):
			security = SecurityHandler()
			if(security.is_valid_key(request)):
				content = request.POST.get('request')				
			else:
				return False
		else:
			content = content = ''

		data_decoded = self.serializer.decode(content)
		return data_decoded

	def getDataSignature(self, request, **options):
		""" Returns data object from request """
		if(request.method == 'POST'):
			security = SecurityHandler()
			if(security.is_valid_signature(request)):
				content = request.POST.get('request')
				content = self.crypt.decode(content)
			else:
				content = ''
		else:
			content = request.POST.get('request')

		data_decoded = self.serializer.decode(content)
		return data_decoded

	def getDataAuth(self, request, **options):
		""" Returns data object from request """
		if(request.method == 'POST'):
			content = request.POST.get('request')
			#content = self.crypt.decode(content)			
		else:
			content = request.POST.get('request')

		data_decoded = self.serializer.decode(content)
		return data_decoded