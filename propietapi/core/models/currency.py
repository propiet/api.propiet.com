from django.db import models
from django.utils.translation import ugettext_lazy as _

# Currency Model
class Currency(models.Model):
	"""Class Currency
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""
	
	id = models.AutoField(primary_key=True, db_index=True)
	symbol = models.CharField(max_length=10, verbose_name=_('Symbol'))
	name = models.CharField(max_length=100, verbose_name=_('Name'))
   
	class Meta:
		db_table = "core_currency"
		app_label = "core"
		verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')

	def __unicode__(self):
		return self.symbol