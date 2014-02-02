from django.db import models
from core.models import Category

# SubCategory Model
class SubCategory(models.Model):
	"""Class SubCategory
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""
	
	id = models.AutoField(primary_key=True, db_index=True)
	category = models.ForeignKey(Category)
	name = models.CharField(max_length=100)	
   
	class Meta:
		db_table = "core_sub_category"
		app_label = "core"

	def __unicode__(self):
		return self.name