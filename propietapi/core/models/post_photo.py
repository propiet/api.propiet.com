import uuid
from django.contrib.auth.models import User
from django.db import models
from core.models import Post
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.translation import ugettext_lazy as _

# PostPhoto Model
class PostPhoto(models.Model):
	"""Class PostPhoto
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""
		
	id = models.AutoField(primary_key=True, db_index=True)	
	post = models.ForeignKey(Post, verbose_name=_('Post'), default=None, blank=True)
	creation_date = models.DateTimeField(auto_now_add=True)
	last_update = models.DateTimeField(auto_now=True)
	file = ProcessedImageField(processors=[ResizeToFill(800, 600)], format='JPEG', options={'quality': 75}, upload_to=lambda instance, filename: 'post/{0}/{1}'.format(instance.post.pk, str(uuid.uuid4())+'.jpg'), verbose_name=_('File'))
	
	class Meta:
		db_table = "core_post_photo"
		app_label = "core"
		verbose_name = _('Photo')
        verbose_name_plural = _('Photos')

	def __unicode__(self):
		return str(self.id)