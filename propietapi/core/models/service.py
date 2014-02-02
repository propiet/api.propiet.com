from django.db import models

# Service Model
class Service(models.Model):
	"""Class Service
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""
	
	id = models.AutoField(primary_key=True, db_index=True)
	name = models.CharField(max_length=100)
   
	class Meta:
		db_table = "core_service"
		app_label = "core"

	def __unicode__(self):
		return self.name