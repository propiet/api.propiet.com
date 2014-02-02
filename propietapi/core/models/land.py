# -*- coding: utf-8 -*-
from django.db import models
from core.models import Property


# Land Model
class Land(Property):
    """Class Land
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""
    
    SUITABLE = (
        (0, 'No especificado'),
        (1, 'Si'),
        (2, 'No'),        
    )
    frontGround = models.FloatField(blank=True, null=True)
    largeGround = models.FloatField(blank=True, null=True)    
    commercialUsage = models.IntegerField(max_length=1, choices=SUITABLE)    

    class Meta:
        db_table = "core_property_land"
        app_label = "core"