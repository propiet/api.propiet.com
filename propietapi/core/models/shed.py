# -*- coding: utf-8 -*-
from django.db import models
from core.models import Property


# Shed Model
class Shed(Property):
    """Class Shed
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""

    DISPOSITION_TYPE = (
        (0, 'No especificado'),
        (1, 'Frente'),
        (2, 'Contrafrente'),
        (3, 'Interno'),
        (4, 'Lateral'),
    )
    UNITY_TYPE = (
        (0, 'No especificado'),
        (1, 'Loft'),
        (2, 'Departamento'),
        (3, 'Semipiso'),
        (4, 'Piso'),
        (5, 'Duplex'),
        (6, 'Penthouse'),
    )
    QUANTITY = (
        (0, 'No especificado'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5 o más'),        
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
    ROOF_TYPE = (
        (0, 'No especificado'),
        (1, 'Chapa'),
        (2, 'Losa'),
        (3, 'Pizzarra'),
        (4, 'Teja'),
    )
    GATE_TYPE = (
        (0, 'No especificado'),
        (1, 'Corredizo'),
        (2, 'Levadizo'),        
    )
    INDUSTRIAL_ROOF_TYPE = (
        (0, 'No especificado'),
        (1, 'Astori'),
        (2, 'Bobedilla'),
        (3, 'Cabriada'),
        (4, 'Chapa'),
        (5, 'Dos aguas'),
        (6, 'Fibrocemento'),
        (7, 'Galvanizado'),
        (8, 'Hormigón'),
        (9, 'Losa'),
        (10, 'Parabolico'),
        (11, 'Premoldeado'),
        (12, 'Tinglado'),
        (14, 'Tres aguas'),
        (15, 'Zinc'),
        (16, 'Otro'),
    )
    COVERAGE = (
        (0, 'Descubierta'),
        (1, 'Cubierta'),
        (2, 'Semicubierta'),        
    )
    fot = models.IntegerField()
    frontGround = models.IntegerField()
    largeGround = models.IntegerField()
    quantityAmbiences = models.IntegerField(max_length=1, choices=QUANTITY, default=0)
    quantityBedrooms = models.IntegerField(max_length=1, choices=QUANTITY, default=0)
    quantityBathrooms = models.IntegerField(max_length=1, choices=QUANTITY, default=0)
    quantityGarages = models.IntegerField(max_length=1, choices=QUANTITY, default=0)
    quantityShips = models.IntegerField(max_length=1, choices=QUANTITY, default=0)    
    garageCoverage = models.IntegerField(max_length=1, blank=True, choices=COVERAGE, default=0)
    unityType = models.IntegerField(max_length=1, choices=UNITY_TYPE, default=0)
    orientation = models.IntegerField(max_length=1, choices=ORIENTATION_TYPE, default=0)
    disposition = models.IntegerField(max_length=1, choices=DISPOSITION_TYPE, default=0)
    buildingType = models.IntegerField(max_length=1, choices=BUILDING_TYPE, default=0)
    buildingCondition = models.IntegerField(max_length=1, choices=BUILDING_STATUS, default=0)
    buildingStatus = models.IntegerField(max_length=1, choices=BUILDING_STATUS, default=0)
    buildingCategory = models.IntegerField(max_length=1, choices=BUILDING_CATEGORY, default=0)    
    apartmentsPerFloor = models.IntegerField(blank=True, null=True)
    quantityBuildingFloors = models.IntegerField(blank=True, null=True)
    floorNumber = models.IntegerField(blank=True, null=True)
    quantityElevators = models.IntegerField(max_length=1, choices=QUANTITY, default=0)
    expenses = models.FloatField(blank=True, null=True)
    suitableProfessional = models.IntegerField(blank=True, max_length=1, choices=SUITABLE, default=0)
    commercialUsage = models.IntegerField(blank=True, max_length=1, choices=SUITABLE, default=0)    
    lightness = models.IntegerField(max_length=1, choices=LIGHTNESS, default=0)
    roofType = models.IntegerField(max_length=1, choices=ROOF_TYPE, default=0)
    industrialRoofType = models.IntegerField(max_length=1, choices=INDUSTRIAL_ROOF_TYPE, default=0)
    roofHeight = models.FloatField(blank=True, null=True)
    gateType = models.IntegerField(max_length=1, choices=GATE_TYPE, default=0)    
    commercialUsage = models.IntegerField(max_length=1, choices=SUITABLE, default=0)    

    class Meta:
        db_table = "core_property_shed"
        app_label = "core"