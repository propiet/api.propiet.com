from django.db import models
from django.utils.translation import ugettext_lazy as _

# Category Model
class Category(models.Model):
	"""Class Category
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""
	
	id = models.AutoField(primary_key=True, db_index=True)
	name = models.CharField(max_length=100, verbose_name=_('Name'))
   
	class Meta:
		db_table = "core_category"
		app_label = "core"
		verbose_name = _('Category')
        verbose_name_plural = _('Categories')

	def __unicode__(self):
		return self.name