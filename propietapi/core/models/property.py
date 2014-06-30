# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.models import Location, Category, SubCategory, Feature, Service, Ambience
from django.utils.translation import ugettext_lazy as _

# Property Model
from core.tasks import create_property_on_zona_prop, update_property_on_zona_prop, delete_property_on_zona_prop


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
    COVERAGE = (
        (0, 'No especificado'),
        (1, 'Descubierta'),
        (2, 'Cubierta'),
        (3, 'Semicubierta'),        
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
    STAGE = (
        (0, 'No especificado'),
        (1, 'En Pozo'),
        (2, 'En Construcción'),
        (3, 'Terminado'),        
    )
    DELIVERY = (
        (0, 'No especificado'),
        (2014, 2014),
        (2015, 2015),
        (2016, 2016),
        (2017, 2017),
        (2018, 2018),
        (2019, 2019),
    )

    id = models.AutoField(primary_key=True, db_index=True)
    user = models.ForeignKey(User, verbose_name=_('User'))
    category = models.ForeignKey(Category, verbose_name=_('Category'))
    subcategory = models.ForeignKey(SubCategory, null=True, verbose_name=_('Subcategory'))
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    antiqueness = models.PositiveSmallIntegerField(blank=True, max_length=1, choices=ANTIQUENESS, default=0, verbose_name=_('Antiqueness'))
    square_meters = models.FloatField(blank=True, null=True, default=None,verbose_name=_('Square Meters'))
    total_covered_meters = models.FloatField(blank=True, null=True, default=None, verbose_name=_('Total Covered Meters'))
    total_uncovered_meters = models.FloatField(blank=True, null=True, default=None, verbose_name=_('Total Uncovered Meters'))
    location = models.OneToOneField(Location, verbose_name=_('Location'))
    features = models.ManyToManyField(Feature, blank=True, verbose_name=_('Features'))
    services = models.ManyToManyField(Service, blank=True, verbose_name=_('Services'))
    ambiences = models.ManyToManyField(Ambience, blank=True, verbose_name=_('Ambiences'))
    lightness = models.PositiveSmallIntegerField(blank=True, max_length=1, choices=LIGHTNESS, default=0, verbose_name=_('Lightness'))
    orientation = models.PositiveSmallIntegerField(blank=True, max_length=1, choices=ORIENTATION_TYPE, default=0, verbose_name=_('Orientation'))
    disposition = models.PositiveSmallIntegerField(blank=True, max_length=1, choices=DISPOSITION_TYPE, default=0, verbose_name=_('Disposition'))
    quantityAmbiences = models.PositiveSmallIntegerField(blank=True, max_length=1, choices=QUANTITY, default=0, verbose_name=_('Quantity Ambiences'))
    quantityBathrooms = models.PositiveSmallIntegerField(blank=True, max_length=1, choices=QUANTITY, default=0, verbose_name=_('Quantity Bathrooms'))
    quantityBedrooms = models.PositiveSmallIntegerField(blank=True, max_length=1, choices=QUANTITY, default=0, verbose_name=_('Quantity Bedrooms'))
    quantityGarages = models.PositiveSmallIntegerField(blank=True, max_length=1, choices=QUANTITY, default=0, verbose_name=_('Quantity Garages'))    
    garageCoverage = models.PositiveSmallIntegerField(blank=True, null=True, choices=COVERAGE, default=0, verbose_name=_('Garage Coverage'))        
    buildingType = models.PositiveSmallIntegerField(blank=True, max_length=1, choices=BUILDING_TYPE, default=0, verbose_name=_('Building Type'))    
    buildingStatus = models.PositiveSmallIntegerField(blank=True, max_length=1, choices=BUILDING_STATUS, default=0, verbose_name=_('Building Status'))
    buildingCategory = models.PositiveSmallIntegerField(blank=True, max_length=1, choices=BUILDING_CATEGORY, default=0, verbose_name=_('Building Category'))    
    apartmentsPerFloor = models.PositiveSmallIntegerField(blank=True, null=True, default=None, verbose_name=_('Apartments per Floor'))
    quantityBuildingFloors = models.PositiveSmallIntegerField(blank=True, null=True, default=None, verbose_name=_('Quantity Building Floors'))
    floorNumber = models.PositiveSmallIntegerField(blank=True, null=True, default=None, verbose_name=_('Floor Number'))
    quantityElevators = models.PositiveSmallIntegerField(blank=True, max_length=1, choices=QUANTITY, default=0, verbose_name=_('Quantity Elevators'))
    expenses = models.FloatField(blank=True, null=True, default=None, verbose_name=_('Expenses'))    
    roofType = models.CharField(blank=True, max_length=1, choices=ROOF_TYPE, default=0, verbose_name=_('Roof Type'))
    industrialRoofType = models.CharField(blank=True, max_length=1, choices=INDUSTRIAL_ROOF_TYPE, default=0, verbose_name=_('Industrial Roof Type'))
    roofHeight = models.FloatField(blank=True, null=True, default=None, verbose_name=_('Roof Height'))
    gateType = models.CharField(blank=True, max_length=1, choices=GATE_TYPE, default=0, verbose_name=_('Gate Type'))
    frontGround = models.FloatField(blank=True, null=True, default=None, verbose_name=_('Front Ground'))
    largeGround = models.FloatField(blank=True, null=True, default=None, verbose_name=_('Large Ground'))
    hectares = models.FloatField(blank=True, null=True, default=None, verbose_name=_('Hectares'))
    fot = models.FloatField(blank=True, null=True, default=None, verbose_name=_('FOT'))
    fos = models.FloatField(blank=True, null=True, default=None, verbose_name=_('FOS'))
    stage = models.CharField(blank=True, max_length=1, choices=STAGE, default=0, verbose_name=_('Stage'))
    deliveryYear = models.CharField(blank=True, max_length=1, choices=DELIVERY, default=0, verbose_name=_('Delivery Year'))
    suitableProfessional = models.PositiveSmallIntegerField(blank=True, max_length=1, choices=SUITABLE, default=0, verbose_name=_('Suitable Professional'))
    commercialUsage = models.PositiveSmallIntegerField(max_length=1, choices=SUITABLE, blank=True, default=0, verbose_name=_('Commercial Usage'))   
    suitableCredit = models.PositiveSmallIntegerField(max_length=1, choices=SUITABLE, blank=True, null=True, default=0, verbose_name=_('Suitable Credit'))
    providesFunding = models.PositiveSmallIntegerField(max_length=1, choices=SUITABLE, blank=True, null=True, default=0, verbose_name=_('Provides Funding'))

    class Meta:
        db_table = "core_property"
        app_label = "core"
        verbose_name = _('Property')
        verbose_name_plural = _('Properties')

    def get_user(self):
        return self.user    

    def __unicode__(self):
        if self.id is None:
            return "None"
        else:
            return self.category.name+'-'+self.location.address


@receiver(post_save, sender=Property)
@receiver(post_delete, sender=Property)
def property_post_connect(**kwargs):
    instance = kwargs['instance']
    if 'created' not in kwargs:
        # Its a deletion:
        delete_property_on_zona_prop.delay(instance)
    else:
        created = kwargs.get('created', False)
        if created:
            create_property_on_zona_prop.delay(instance)
        else:
            update_property_on_zona_prop.delay(instance)

