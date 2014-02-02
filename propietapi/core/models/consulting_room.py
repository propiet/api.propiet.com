# -*- coding: utf-8 -*-
from django.db import models
from core.models import Property


# ConsultingRoom Model
class ConsultingRoom(Property):
    """Class ConsultingRoom
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""

    DISPOSITION_TYPE = (
        (0, 'No especificado'),
        (1, 'Frente'),
        (2, 'Contrafrente'),
        (3, 'Interno'),
        (4, 'Lateral')
        )
    QUANTITY = (
        (0, 'No especificado'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5 o más')
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
    BUILDING_TYPE = (
        (0, 'No especificado'),
        (1, 'Entre medianeras'),
        (2, 'Torre'),
        (3, 'Tipo Block'),
        (4, 'Esquina'),
        (5, 'Antiguo'),
        (6, 'Inteligente'),
        (7, 'Primera Categoria'),
        (8, 'Estándar'),
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
    BUILDING_CATEGORY = (
        (0, 'No especificado'),
        (1, 'Excelente'),
        (2, 'Muy Buena'),
        (3, 'Buena'),
        (4, 'Estándar'),
        (5, 'Económica'),        
    )
    SUITABLE = (
        (0, 'No especificado'),
        (1, 'Si'),
        (2, 'No'),        
    )
    LIGHTNESS = (
        (0, 'No especificado'),
        (1, 'Muy luminoso'),
        (2, 'Luminoso'),
        (3, 'Poco luminoso'),
    )
        
    quantityBathrooms = models.IntegerField(max_length=1, choices=QUANTITY)
    quantityGarages = models.IntegerField(max_length=1, choices=QUANTITY)    
    garageCoverage = models.FloatField(blank=True, null=True)    
    orientation = models.IntegerField(max_length=1, choices=ORIENTATION_TYPE)
    disposition = models.IntegerField(max_length=1, choices=DISPOSITION_TYPE)
    buildingType = models.IntegerField(max_length=1, choices=BUILDING_TYPE)
    buildingCondition = models.IntegerField(max_length=1, choices=BUILDING_STATUS)
    buildingStatus = models.IntegerField(max_length=1, choices=BUILDING_STATUS)
    buildingCategory = models.IntegerField(max_length=1, choices=BUILDING_CATEGORY)    
    apartmentsPerFloor = models.IntegerField(blank=True, null=True)
    quantityBuildingFloors = models.IntegerField(blank=True, null=True)
    floorNumber = models.IntegerField(blank=True, null=True)
    quantityElevators = models.IntegerField(max_length=1, choices=QUANTITY)
    expenses = models.FloatField(blank=True, null=True)    
    lightness = models.IntegerField(max_length=1, choices=LIGHTNESS)    

    class Meta:
        db_table = "core_property_consulting_room"
        app_label = "core"