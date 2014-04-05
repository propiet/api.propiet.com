# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Operation Model
class Operation(models.Model):
	"""Class Operation
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""
	
	id = models.AutoField(primary_key=True, db_index=True)
	operation = models.CharField(max_length=100, verbose_name=_('Operation'))	
   
	class Meta:
		db_table = "core_operation"
		app_label = "core"
		verbose_name = _('Operation')
        verbose_name_plural = _('Operations')

	def __unicode__(self):
		return self.operation