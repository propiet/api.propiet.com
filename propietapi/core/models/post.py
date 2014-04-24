# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from core.models import  Category, Currency, Operation, Property
from cities_light.models import Region, City
from django.utils.translation import ugettext_lazy as _

# Post Model
class Post(models.Model):
	"""Class Post
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""

	STATUS = (
	 	(0, 'ARCHIVADA'),
        (1, 'NUEVA'),
        (2, 'PAUSADA'),
        (3, 'PUBLICADA'),
        (4, 'FINALIZADA'),
    )

	id = models.AutoField(primary_key=True, db_index=True)
	property = models.ForeignKey(Property, verbose_name=_('Property'))
	user = models.ForeignKey(User, verbose_name=_('User'), related_name='post_user')
	agent = models.ForeignKey(User, verbose_name=_('Agent'), related_name='post_agent', default=None, blank=True, null=True)	
	category = models.ForeignKey(Category, verbose_name=_('Category'))
	operation = models.ForeignKey(Operation, verbose_name=_('Operation'))
	price = models.FloatField(verbose_name=_('Price'), default=0)
	currency = models.ForeignKey(Currency, verbose_name=_('Currency'))
	title = models.CharField(verbose_name=_('Title'), max_length=200)
	description = models.TextField(verbose_name=_('Description'), max_length=500)
	hidden_note = models.TextField(verbose_name=_('Hidden Note'), max_length=500, default=None, blank=True, null=True)
	status = models.PositiveSmallIntegerField(verbose_name=_('Status'), default=0, max_length=1, choices=STATUS)
	featured = models.BooleanField(verbose_name=_('Featured'), default=0)
	video_url = models.URLField(verbose_name=_('Video Url'), max_length=500, default=None, blank=True, null=True)
	map_image_url = models.URLField(verbose_name=_('Map Image Url'), max_length=500, default=None, blank=True, null=True)
	plane_url = models.URLField(verbose_name=_('Plane Url'), max_length=500, default=None, blank=True, null=True)
	region = models.ForeignKey(Region, verbose_name=_('Region'), null=True)
	city = models.ForeignKey(City, verbose_name=_('City'), null=True)
	creation_date = models.DateTimeField(auto_now_add=True)
	last_update = models.DateTimeField(auto_now=True)	

	class Meta:
		db_table = "core_post"
		app_label = "core"
		verbose_name = _('Post')
        verbose_name_plural = _('Posts')

	def get_user(self):
		return self.user	

	def __unicode__(self):		
		return unicode(str(self.title))