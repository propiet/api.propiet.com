# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from cities_light.models import Country, Region, City
from django.utils.translation import ugettext_lazy as _

# Location Model
class Location(models.Model):
	"""Class Location
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""

	id = models.AutoField(primary_key=True, db_index=True)	
	address = models.CharField(max_length=500, verbose_name=_('Address'))	
	longitude = models.CharField(max_length=100, blank=True, null=True, default=0, verbose_name=_('Longitude'))
	latitude = models.CharField(max_length=100, blank=True, null=True, default=0, verbose_name=_('Latitude'))
	country = models.ForeignKey(Country, null=True, verbose_name=_('Country'))
	region = models.ForeignKey(Region, null=True, verbose_name=_('Region'))
	city = models.ForeignKey(City, null=True, verbose_name=_('City'))

	class Meta:
		db_table = "core_location"
		app_label = "core"
		verbose_name = _('Location')
        verbose_name_plural = _('Locations')

	def get_user(self):
		return self.user	

	def __unicode__(self):
		return self.address+' > '+self.region.name+'-'+self.city.name