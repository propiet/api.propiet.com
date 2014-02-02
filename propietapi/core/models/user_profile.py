from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
	
    user = models.ForeignKey(User, unique=True, primary_key=True, related_name='profile')
    phone = models.IntegerField(max_length=10, unique=False)

    class Meta:
    	db_table = "core_user_profile"
    	app_label = "core"

    def __unicode__(self):
		return self.user.username