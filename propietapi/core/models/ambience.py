from django.db import models

# Ambience Model
class Ambience(models.Model):
	"""Class Ambience
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""
	
	id = models.AutoField(primary_key=True, db_index=True)
	name = models.CharField(max_length=100)
   
	class Meta:
		db_table = "core_ambience"
		app_label = "core"

	def __unicode__(self):
		return self.name