from django.db import models

# Currency Model
class Currency(models.Model):
	"""Class Currency
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""
	
	id = models.AutoField(primary_key=True, db_index=True)
	symbol = models.CharField(max_length=10)
	name = models.CharField(max_length=100)
   
	class Meta:
		db_table = "core_currency"
		app_label = "core"

	def __unicode__(self):
		return self.symbol