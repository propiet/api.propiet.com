# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from core.models import Location, Category, SubCategory, Feature, Service, Ambience


# Property Model
class Property(models.Model):
    """Class Property
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""
        
    ANTIQUENESS = (
        (0, 'No especificado'),
        (1, 'A Estrenar'),
        (2, '1 a 5'),
        (3, '6 a 15'),
        (4, '16 a 50'),
        (5, 'más de 50'),        
    )
    SUITABLE = (
        (0, 'No especificado'),
        (1, 'Si'),
        (2, 'No'),
    )

    id = models.AutoField(primary_key=True, db_index=True)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    subcategory = models.ForeignKey(SubCategory, null=True)
    creation_date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now=True)
    antiqueness = models.IntegerField(max_length=1, choices=ANTIQUENESS, default=0)
    square_meters = models.FloatField()
    total_meters = models.FloatField()
    total_uncovered_meters = models.FloatField(blank=True, null=True)
    location = models.OneToOneField(Location)
    features = models.ManyToManyField(Feature, blank=True)
    services = models.ManyToManyField(Service, blank=True)
    ambiences = models.ManyToManyField(Ambience, blank=True)    
    suitableCredit = models.IntegerField(max_length=1, choices=SUITABLE, blank=True, null=True, default=0)
    providesFunding = models.IntegerField(max_length=1, choices=SUITABLE, blank=True, null=True, default=0)

    class Meta:
        db_table = "core_property"
        app_label = "core"

    def get_user(self):
        return self.user    

    def __unicode__(self):
        return self.category.name+'-'+self.location.address