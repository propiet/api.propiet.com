# -*- coding: utf-8 -*-
from django.db import models
from core.models import Property


# Local Model
class Local(Property):
    """Class Local
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""

    QUANTITY = (
        (0, 'No especificado'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5 o más'),        
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
    DISPOSITION_TYPE = (
        (0, 'No especificado'),
        (1, 'Frente'),
        (2, 'Contrafrente'),
        (3, 'Interno'),
        (4, 'Lateral'),
    )
    SUITABLE = (
        (0, 'No especificado'),
        (1, 'Si'),
        (2, 'No'),        
    )
    
    quantityBathrooms = models.IntegerField(max_length=1, choices=QUANTITY, default=0)
    quantityGarages = models.IntegerField(max_length=1, choices=QUANTITY, default=0)    
    orientation = models.IntegerField(max_length=1, choices=ORIENTATION_TYPE, default=0)
    disposition = models.IntegerField(max_length=1, choices=DISPOSITION_TYPE, default=0)    
    buildingStatus = models.IntegerField(max_length=1, choices=BUILDING_STATUS, default=0)
    expenses = models.FloatField(blank=True, null=True)
    lightness = models.IntegerField(max_length=1, choices=LIGHTNESS, default=0)    

    class Meta:
        db_table = "core_property_local"
        app_label = "core"