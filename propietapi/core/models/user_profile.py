from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

class UserProfile(models.Model):
	
    user = models.ForeignKey(User, unique=True, primary_key=True, related_name='profile', verbose_name=_('User'))
    phone = models.TextField(max_length=40, unique=False, verbose_name=_('Phone'))
    agency_name = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name=_('Agency Name'))
    activation_key = models.CharField(max_length=40, blank=True, null=True, default=None, verbose_name=_('Activation Key'))
    key_expires = models.DateTimeField(default=None, blank=True, null=True, verbose_name=_('Activation Key Expires'))

    class Meta:
    	db_table = "core_user_profile"
    	app_label = "core"
    	verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')

    def __unicode__(self):
		return self.user.username