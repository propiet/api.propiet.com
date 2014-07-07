# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.models import Location, Category, SubCategory, Feature, Service, Ambience
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Property Model
from core.tasks import update_post_on_zona_prop, delete_post_on_zona_prop


class Property(models.Model):
    """Class Property
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""

    PROPERTY_DESCRIPTION_MAP = {
        'zonaprop': {
            'lightness': {
                0: None,
                1: 'muy_luminoso',
                2: 'luminoso',
                3: 'poco_luminoso'
            },
            'orientation': {
                0: None,
                1: 'n',
                2: 's',
                3: 'e',
                4: 'o',
                5: 'ne',
                6: 'no',
                7: 'se',
                8: 'so',
            },
            'disposition': {
                0: None,
                1: 'frente',
                2: 'contrafrente',
                3: 'interno',
                4: 'lateral'
            },
            'quantity': {
                0: None,
                1: '1',
                2: '2',
                3: '3',
                4: '4',
                5: '5_mas'
            },
            'garage_coverage': {
                0: None,
                1: 'descubierta',
                2: 'cubierta',
                3: 'semi_cubierta'
            },
            'building_type': {
                0: None,
                1: 'entre_medianeras',
                2: 'torre',
                3: 'tipo_block',
                4: 'esquina',
                5: 'antiguo',
                6: 'inteligente',
                7: 'primera_categoria',
                8: 'standard'
            },
            'building_status': {
                0: None,
                1: 'reciclado',
                2: 'excelente',
                3: 'muy_bueno',
                4: 'bueno',
                5: 'regular',
                6: 'refaccionar',
            },
            'building_category': {
                0: None,
                1: 'excelente',
                2: 'muy_buena',
                3: 'buena',
                4: 'excelente',
                5: 'economica',
            },
            'roof_type': {
                '': None,
                '0': None,
                '1': 'chapa',
                '2': 'losa',
                '3': 'pizarra',
                '4': 'teja',
            },
            'industrial_roof_type': {
                '': None,
                '0': None,
                '1': 'astori',
                '2': 'bovedilla',
                '3': 'cabriada',
                '4': 'chapa',
                '5': 'dos_aguas',
                '6': 'fibrocemento',
                '7': 'galvanizado',
                '8': 'hormigon',
                '9': 'losa',
                '10': 'parabolico',
                '11': 'premoldeado',
                '12': 'tinglado',
                '14': 'tres_aguas',
                '15': 'zinc',
                '16': 'otro',
            },
            'gate_type': {
                '': None,
                '0': None,
                '1': 'Corredizo',
                '2': 'Levadizo',
            },
            'stage': {
                '': None,
                '0': None,
                '1': 'pozo',
                '2': 'construccion',
                '3': 'terminado',
            },
            'suitable': {
                0: None,
                1: 'si',
                2: 'no',
            }
        }
    }

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
        ('0', 'No especificado'),
        ('1', 'Chapa'),
        ('2', 'Losa'),
        ('3', 'Pizzarra'),
        ('4', 'Teja'),
    )
    GATE_TYPE = (
        ('0', 'No especificado'),
        ('1', 'Corredizo'),
        ('2', 'Levadizo'),
    )
    INDUSTRIAL_ROOF_TYPE = (
        ('0', 'No especificado'),
        ('1', 'Astori'),
        ('2', 'Bobedilla'),
        ('3', 'Cabriada'),
        ('4', 'Chapa'),
        ('5', 'Dos aguas'),
        ('6', 'Fibrocemento'),
        ('7', 'Galvanizado'),
        ('8', 'Hormigón'),
        ('9', 'Losa'),
        ('10', 'Parabolico'),
        ('11', 'Premoldeado'),
        ('12', 'Tinglado'),
        ('14', 'Tres aguas'),
        ('15', 'Zinc'),
        ('16', 'Otro'),
    )
    STAGE = (
        ('0', 'No especificado'),
        ('1', 'En Pozo'),
        ('2', 'En Construcción'),
        ('3', 'Terminado'),
    )
    DELIVERY = (
        ('0', 'No especificado'),
        ('2014', 2014),
        ('2015', 2015),
        ('2016', 2016),
        ('2017', 2017),
        ('2018', 2018),
        ('2019', 2019),
    )

    id = models.AutoField(primary_key=True, db_index=True)
    user = models.ForeignKey(User, verbose_name=_('User'))
    category = models.ForeignKey(Category, verbose_name=_('Category'))
    subcategory = models.ForeignKey(SubCategory, null=True, verbose_name=_('Subcategory'))
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    antiqueness = models.PositiveSmallIntegerField(blank=True, null=True, default=None, verbose_name=_('Antiqueness'))
    square_meters = models.FloatField(blank=True, null=True, default=None,verbose_name=_('Square Meters'))
    total_covered_meters = models.FloatField(blank=True, null=True, default=None, verbose_name=_('Total Covered Meters'))
    total_uncovered_meters = models.FloatField(blank=True, null=True, default=None, verbose_name=_('Total Uncovered Meters'))
    location = models.OneToOneField(Location, verbose_name=_('Location'))
    features = models.ManyToManyField(Feature, blank=True, verbose_name=_('Features'))
    services = models.ManyToManyField(Service, blank=True, verbose_name=_('Services'))
    ambiences = models.ManyToManyField(Ambience, blank=True, verbose_name=_('Ambiences'))
    lightness = models.PositiveSmallIntegerField(blank=True, null=True, max_length=1, choices=LIGHTNESS, default=0, verbose_name=_('Lightness'))
    orientation = models.PositiveSmallIntegerField(blank=True, null=True, max_length=1, choices=ORIENTATION_TYPE, default=0, verbose_name=_('Orientation'))
    disposition = models.PositiveSmallIntegerField(blank=True, null=True, max_length=1, choices=DISPOSITION_TYPE, default=0, verbose_name=_('Disposition'))
    quantityAmbiences = models.PositiveSmallIntegerField(blank=True, null=True, max_length=1, choices=QUANTITY, default=0, verbose_name=_('Quantity Ambiences'))
    quantityBathrooms = models.PositiveSmallIntegerField(blank=True, null=True, max_length=1, choices=QUANTITY, default=0, verbose_name=_('Quantity Bathrooms'))
    quantityBedrooms = models.PositiveSmallIntegerField(blank=True, null=True, max_length=1, choices=QUANTITY, default=0, verbose_name=_('Quantity Bedrooms'))
    quantityGarages = models.PositiveSmallIntegerField(blank=True, null=True, max_length=1, choices=QUANTITY, default=0, verbose_name=_('Quantity Garages'))
    garageCoverage = models.PositiveSmallIntegerField(blank=True, null=True, choices=COVERAGE, default=0, verbose_name=_('Garage Coverage'))        
    buildingType = models.PositiveSmallIntegerField(blank=True, null=True, max_length=1, choices=BUILDING_TYPE, default=0, verbose_name=_('Building Type'))
    buildingStatus = models.PositiveSmallIntegerField(blank=True, null=True, max_length=1, choices=BUILDING_STATUS, default=0, verbose_name=_('Building Status'))
    buildingCategory = models.PositiveSmallIntegerField(blank=True, null=True, max_length=1, choices=BUILDING_CATEGORY, default=0, verbose_name=_('Building Category'))
    apartmentsPerFloor = models.PositiveSmallIntegerField(blank=True, null=True, default=None, verbose_name=_('Apartments per Floor'))
    quantityBuildingFloors = models.PositiveSmallIntegerField(blank=True, null=True, default=None, verbose_name=_('Quantity Building Floors'))
    floorNumber = models.PositiveSmallIntegerField(blank=True, null=True, default=None, verbose_name=_('Floor Number'))
    quantityElevators = models.PositiveSmallIntegerField(null=True, blank=True, max_length=1, choices=QUANTITY, default=0, verbose_name=_('Quantity Elevators'))
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
    suitableProfessional = models.PositiveSmallIntegerField(blank=True, null=True, max_length=1, choices=SUITABLE, default=0, verbose_name=_('Suitable Professional'))
    commercialUsage = models.PositiveSmallIntegerField(max_length=1, choices=SUITABLE, blank=True, null=True, default=0, verbose_name=_('Commercial Usage'))
    suitableCredit = models.PositiveSmallIntegerField(max_length=1, choices=SUITABLE, blank=True, null=True, default=0, verbose_name=_('Suitable Credit'))
    providesFunding = models.PositiveSmallIntegerField(max_length=1, choices=SUITABLE, blank=True, null=True, default=0, verbose_name=_('Provides Funding'))

    class Meta:
        db_table = "core_property"
        app_label = "core"
        verbose_name = _('Property')
        verbose_name_plural = _('Properties')

    def get_user(self):
        return self.user

    def get_zonaprop_lightness(self):
        return self._get_zonaprop_property_value('lightness', self.lightness)

    def get_zonaprop_orientation(self):
        return self._get_zonaprop_property_value('orientation', self.orientation)

    def get_zonaprop_disposition(self):
        return self._get_zonaprop_property_value('disposition', self.disposition)

    def get_zonaprop_quantity_ambiences(self):
        return self._get_zonaprop_property_value('quantity', self.quantityAmbiences)

    def get_zonaprop_quantity_bathrooms(self):
        return self._get_zonaprop_property_value('quantity', self.quantityBathrooms)

    def get_zonaprop_quantity_bedrooms(self):
        return self._get_zonaprop_property_value('quantity', self.quantityBedrooms)

    def get_zonaprop_quantity_garages(self):
        return self._get_zonaprop_property_value('quantity', self.quantityGarages)

    def get_zonaprop_garage_coverage(self):
        return self._get_zonaprop_property_value('garage_coverage', self.garageCoverage)

    def get_zonaprop_building_type(self):
        return self._get_zonaprop_property_value('building_type', self.buildingType)

    def get_zonaprop_building_status(self):
        return self._get_zonaprop_property_value('building_status', self.buildingStatus)

    def get_zonaprop_building_category(self):
        return self._get_zonaprop_property_value('building_category', self.buildingCategory)

    def get_zonaprop_quantity_elevators(self):
        return self._get_zonaprop_property_value('quantity', self.quantityElevators)

    def get_zonaprop_roof_type(self):
        return self._get_zonaprop_property_value('roof_type', self.roofType)

    def get_zonaprop_industrial_roof_type(self):
        return self._get_zonaprop_property_value('industrial_roof_type', self.industrialRoofType)

    def get_zonaprop_gate_type(self):
        return self._get_zonaprop_property_value('gate_type', self.gateType)

    def get_zonaprop_stage(self):
        return self._get_zonaprop_property_value('stage', self.stage)

    def get_zonaprop_suitable_professional(self):
        return self._get_zonaprop_property_value('suitable', self.suitableProfessional)

    def get_zonaprop_commercial_usage(self):
        return self._get_zonaprop_property_value('suitable', self.commercialUsage)

    def get_zonaprop_suitable_credit(self):
        return self._get_zonaprop_property_value('suitable', self.suitableCredit)

    def get_zonaprop_provides_funding(self):
        return self._get_zonaprop_property_value('suitable', self.providesFunding)

    def get_zonaprop_property_type(self):
        if self.subcategory.get_zonaprop_subcategory():
            return self.category.get_zonaprop_category() + '_' + self.subcategory.get_zonaprop_subcategory()
        else:
            return self.category.get_zonaprop_category()

    def _get_zonaprop_property_value(self, property_set, property_key):
        return self.PROPERTY_DESCRIPTION_MAP['zonaprop'][property_set].get(property_key, None)

    #Required Fields defaults
    def get_zonaprop_hectares(self):
        #Obligatorio para Campos y Chacras
        if self.hectares is None and self.category_id == 7:
            return settings.ZONA_PROP_HECTARES_DEFAULT
        else:
            return self.hectares

    def get_zonaprop_ambiences(self):
        #Obligatorio para Departamentos y Country_Departamento
        if self.get_zonaprop_quantity_ambiences() is None and (self.category_id == 1 or self.subcategory_id == 15):
            return settings.ZONA_PROP_QUANTITY_AMBIENCES_DEFAULT
        else:
            return self.get_zonaprop_quantity_ambiences()

    def get_zonaprop_square_meters(self):
        #obligatorio para todos menos Campos y chacras
        if self.square_meters is None and not self.category_id == 7:
            return settings.ZONA_PROP_SQUARE_METERS_DEFAULT
        else:
            return self.square_meters

    def get_zonaprop_bedrooms(self):
        #obligatorio para todos menos Campos y chacras
        if self.get_zonaprop_quantity_bedrooms() is None and (
                self.category_id == 2 or self.category_id == 3 or self.category_id == 5 or self.subcategory_id == 14):
            return settings.ZONA_PROP_QUANTITY_BEDROOMS_DEFAULT
        else:
            return self.get_zonaprop_quantity_bedrooms()

    def get_zonaprop_covered_meters(self):
        #obligatorio para todos menos Campos y Chacras, Terrenos y lotes y Country Barrios Cerrados_Terreno
        if self.total_covered_meters is None and not (
                self.category_id == 7 or self.category_id == 6 or self.subcategory_id == 16):
            return settings.ZONA_PROP_COVERED_METERS_DEFAULT
        else:
            return self.total_covered_meters

    def __unicode__(self):
        if self.id is None:
            return "None"
        else:
            return self.category.name+'-'+self.location.address

    def __unicode__(self):
        if self.id is None:
            return "None"
        else:
            return self.category.name+'-'+self.location.address


@receiver(post_save, sender=Property)
@receiver(post_delete, sender=Property)
def property_post_connect(**kwargs):
    instance = kwargs['instance']
    if 'created' not in kwargs and instance.post_set.exists():
        # Its a deletion:
            post = instance.post_set.all()[0] #Asumo que hay un sólo post con esta property
            delete_post_on_zona_prop.delay(post)
    else:
        # Its a modification:
        created = kwargs.get('created', False)
        if not created and instance.post_set.exists():
            post = instance.post_set.all()[0]
            update_post_on_zona_prop.delay(post)