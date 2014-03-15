from django.contrib.auth.models import User
from django.db import models
from core.models import SavedQuery

# Alert Model
class Alert(models.Model):
	"""Class Alert
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""
	
	ALERT_TYPE = (
		(0, 'ALERT_SEARCH'),
		(1, 'ALERT_NEWSLETTER'),
		)
	id = models.AutoField(primary_key=True, db_index=True)	
	user = models.ForeignKey(User)
	query = models.OneToOneField(SavedQuery)
	alert_type = models.IntegerField(max_length=1,choices=ALERT_TYPE)	
	creation_date = models.DateTimeField(auto_now=True)
	last_update = models.DateTimeField(auto_now=True)	

	class Meta:
		db_table = "core_alert"
		app_label = "core"

	def get_user(self):
		return self.user	

	def __unicode__(self):
		return self.query.name