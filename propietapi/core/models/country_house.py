# -*- coding: utf-8 -*-
from django.db import models
from core.models import Property


# CountryHouse Model
class CountryHouse(Property):
    """Class CountryHouse
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""

    QUANTITY = (
        (0, 'No especificado'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5 o más'),        
    )
    ROOF_TYPE = (
        (0, 'No especificado'),
        (1, 'Chapa'),
        (2, 'Losa'),
        (3, 'Pizzarra'),
        (4, 'Teja'),
    )    
    LIGHTNESS = (
        (0, 'No especificado'),
        (1, 'Muy luminoso'),
        (2, 'Luminoso'),
        (3, 'Poco luminoso'),
    )
    BUILDING_STATUS = (
        (0, 'No especificado'),
        (1, 'Reciclado'),
        (2, 'Excelente'),
        (3, 'Muy Bueno'),
        (4, 'Bueno'),
        (5, 'Regular'),
        (6, 'A Refaccionar'),        
    )    
    ORIENTATION_TYPE = (
        (0, 'No especificado'),
        (1, 'N'),
        (2, 'S'),
        (3, 'E'),
        (4, 'O'),
        (5, 'NE'),
        (6, 'NO'),
        (7, 'SE'),
        (8, 'SO'),
    )
    SUITABLE = (
        (0, 'No especificado'),
        (1, 'Si'),
        (2, 'No'),        
    )
    frontGround = models.FloatField(blank=True, null=True)
    largeGround = models.FloatField(blank=True, null=True)
    quantityBedrooms = models.IntegerField(max_length=1, choices=QUANTITY)
    quantityBathrooms = models.IntegerField(max_length=1, choices=QUANTITY)
    quantityFloors = models.IntegerField(max_length=1, choices=QUANTITY)
    roofType = models.IntegerField(max_length=1, choices=ROOF_TYPE)
    buildingStatus = models.IntegerField(max_length=1, choices=BUILDING_STATUS)
    orientation = models.IntegerField(max_length=1, choices=ORIENTATION_TYPE)        
    lightness = models.IntegerField(max_length=1, choices=LIGHTNESS)

    class Meta:
        db_table = "core_property_country_house"
        app_label = "core"