from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

# SavedQuery Model
class SavedQuery(models.Model):
	"""Class SavedQuery
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""

	id = models.AutoField(primary_key=True, db_index=True)	
	user = models.ForeignKey(User, verbose_name=_('User'))
	name = models.CharField(max_length=200, verbose_name=_('Name'))
	query = models.TextField(verbose_name=_('Query'))
	creation_date = models.DateTimeField(auto_now_add=True)
	last_update = models.DateTimeField(auto_now=True)	

	class Meta:
		db_table = "core_saved_query"
		app_label = "core"
		verbose_name = _('Saved Query')
        verbose_name_plural = _('Saved Querys')

	def get_user(self):
		return self.user	

	def __unicode__(self):
		return self.name