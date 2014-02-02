from django.contrib.auth.models import User
from django.db import models

# SavedQuery Model
class SavedQuery(models.Model):
	"""Class SavedQuery
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""

	id = models.AutoField(primary_key=True, db_index=True)	
	user = models.ForeignKey(User)
	name = models.CharField(max_length=200)
	query = models.TextField()
	creation_date = models.DateTimeField(auto_now=True)
	last_update = models.DateTimeField(auto_now=True)	

	class Meta:
		db_table = "core_saved_query"
		app_label = "core"

	def get_user(self):
		return self.user	

	def __unicode__(self):
		return self.name