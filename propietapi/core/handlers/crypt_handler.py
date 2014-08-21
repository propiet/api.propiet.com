from hashlib import sha1
import hmac
from base64 import b64decode, b64encode


class CryptHandler():
	"""Class CryptHandler.
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""

	class Meta:
		app_label = 'core'

	def encode(self, data):
		return b64encode(data)

	def decode(self, data):
		return b64decode(data) 

	def get_signature(self, key, data):
		key = str(key)
		data = str(data)
		hashed = hmac.new(key, data, sha1)
		return self.encode(hashed.digest())