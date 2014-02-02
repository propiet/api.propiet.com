from django.db import models

# Operation Model
class Operation(models.Model):
	"""Class Operation
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""
	
	id = models.AutoField(primary_key=True, db_index=True)
	operation = models.CharField(max_length=100)	
   
	class Meta:
		db_table = "core_operation"
		app_label = "core"

	def __unicode__(self):
		return self.operation