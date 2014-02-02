from django.contrib.auth.models import User
from django.db import models
from core.models import Post

# Picture Model
class Picture(models.Model):
	"""Class Picture
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""
		
	id = models.AutoField(primary_key=True, db_index=True)
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)
	name = models.CharField(max_length=200, blank=True, null=True, default="pic")
	creation_date = models.DateTimeField(auto_now=True)
	last_update = models.DateTimeField(auto_now=True)
	file = models.FileField(upload_to=lambda instance, filename: 'post/{0}/{1}'.format(instance.post.pk, filename.replace(' ','_')))

	class Meta:
		db_table = "core_picture"
		app_label = "core"

	def get_user(self):
		return self.user	

	def __unicode__(self):
		return str(self.id)+'-'+self.name+'-'+self.post.title