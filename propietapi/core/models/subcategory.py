from django.db import models
from core.models import Category
from django.utils.translation import ugettext_lazy as _

# SubCategory Model
class SubCategory(models.Model):
	"""Class SubCategory
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""
	
	id = models.AutoField(primary_key=True, db_index=True)
	category = models.ForeignKey(Category, verbose_name=_('Category'))
	name = models.CharField(max_length=100, verbose_name=_('Name'))	
   
	class Meta:
		db_table = "core_sub_category"
		app_label = "core"
		verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')

	def __unicode__(self):
		return self.name