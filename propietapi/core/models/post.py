from django.contrib.auth.models import User
from django.db import models
from core.models import Property, Category, Currency, Operation
from cities_light.models import Region, City

# Post Model
class Post(models.Model):
	"""Class Post
	@author: Lionel Cuevas <lionel@hoopemedia.com>"""

	STATUS = (
	 	(0, 'INACTIVE'),
        (1, 'NEW'),
        (2, 'PAUSED'),
        (3, 'PUBLISHED'),
        (4, 'SOLD'),
    )

	id = models.AutoField(primary_key=True, db_index=True)
	property = models.OneToOneField(Property)
	user = models.ForeignKey(User, related_name='post_user')
	agent = models.ForeignKey(User, blank=True, null=True, related_name='post_agent')
	category = models.ForeignKey(Category)
	operation = models.ForeignKey(Operation)
	price = models.FloatField(default=0)
	currency = models.ForeignKey(Currency)
	title = models.CharField(max_length=200)
	status = models.IntegerField(max_length=1, choices=STATUS)
	description = models.TextField(max_length=500)
	region = models.ForeignKey(Region, null=True)
	city = models.ForeignKey(City, null=True)
	creation_date = models.DateTimeField(auto_now=True)
	last_update = models.DateTimeField(auto_now=True)	

	class Meta:
		db_table = "core_post"
		app_label = "core"

	def get_user(self):
		return self.user	

	def __unicode__(self):
		return self.title