# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Ambience Model
class Ambience(models.Model):
    """Class Feature
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""

    AMBIENCE_MAP = {
        'zonaprop': {
            1: 'altillo',
            2: 'balcon',
            3: 'baulera',
            4: 'cocina',
            5: 'hall',
            6: 'jardin',
            7: 'patio',
            8: 'sotano',
            9: 'terraza',
            10: 'toilette',
            11: 'comedor',
            12: 'comedor_diario',
            13: 'dependencia_servicio',
            14: 'dormitorio_suite',
            15: 'escritorio',
            16: 'hall',
            17: 'lavadero',
            18: 'living',
            19: 'living_comedor',
            21: 'vestidor'
        }
    }

    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=100, verbose_name=_('Name'))

    class Meta:
        db_table = "core_ambience"
        app_label = "core"
        verbose_name = _('Ambience')
        verbose_name_plural = _('Ambiences')

    # def get_zonaprop_ambience(self):
    #     return self.AMBIENCE_MAP['zonaprop'][self.id]

    def __unicode__(self):
        return self.name
