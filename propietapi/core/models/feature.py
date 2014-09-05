# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Characteristic Model
class Feature(models.Model):
    """Class Feature
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""

    FEATURE_MAP = {
    'zonaprop': {
        1: 'aire_acondicionado',
        2: 'alarma',
        3: 'amoblado',
        4: 'calefaccion',
        5: 'cancha_deportes',
        6: 'gimnasio',
        7: 'hidromasaje',
        8: 'laundry',
        9: 'parrilla',
        10:'piscina',
        11: 'quincho',
        12: 'sala_juegos',
        13: 'sauna',
        14: 'solarium',
        15: 'sum',
        16: 'vigilancia'
        }
    }

    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=100, verbose_name=_('Name'))

    class Meta:
        db_table = "core_feature"
        app_label = "core"
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

    # def get_zonaprop_feature(self):
    #     return self.FEATURE_MAP['zonaprop'][self.id]

    def __unicode__(self):
        return self.name