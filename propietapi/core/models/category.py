from django.db import models

# Category Model
class Category(models.Model):
	"""Class Category
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""
	
	id = models.AutoField(primary_key=True, db_index=True)
	name = models.CharField(max_length=100)
   
	class Meta:
		db_table = "core_category"
		app_label = "core"

	def __unicode__(self):
		return self.name