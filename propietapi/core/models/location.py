from django.contrib.auth.models import User
from django.db import models
from cities_light.models import Country, Region, City

# Location Model
class Location(models.Model):
	"""Class Location
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""

	id = models.AutoField(primary_key=True, db_index=True)	
	address = models.CharField(max_length=500)	
	longitude = models.CharField(max_length=100, blank=True, null=True, default=0)
	latitude = models.CharField(max_length=100, blank=True, null=True, default=0)
	country = models.ForeignKey(Country, null=True)
	region = models.ForeignKey(Region, null=True)
	city = models.ForeignKey(City, null=True)

	class Meta:
		db_table = "core_location"
		app_label = "core"

	def get_user(self):
		return self.user	

	def __unicode__(self):
		return self.address+' > '+self.region.name+'-'+self.city.name