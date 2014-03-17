# -*- coding: utf-8 -*-
from django.db import models
from core.models import Property


# Garage Model
class Garage(Property):
    """Class Garage
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""
    
    SUITABLE = (
        (0, 'No especificado'),
        (1, 'Si'),
        (2, 'No'),        
    )

    COVERAGE = (
        (0, 'Descubierta'),
        (1, 'Cubierta'),
        (2, 'Semicubierta'),        
    )

    garageCoverage = models.IntegerField(max_length=1, choices=COVERAGE, default=0)        
    expenses = models.FloatField(blank=True, null=True)            

    class Meta:
        db_table = "core_property_garage"
        app_label = "core"