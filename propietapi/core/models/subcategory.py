# -*- coding: utf-8 -*-
from django.db import models
from core.models import Category
from django.utils.translation import ugettext_lazy as _


# SubCategory Model
class SubCategory(models.Model):
    """Class SubCategory
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""

    SUBCATEGORY_MAP = {
        'zonaprop': {
            1: 'Duplex',
            2: 'Triplex',
            3: 'Loft',
            4: 'Piso',
            5: 'Semipiso',
            6: 'Penthouse',
            7: 'Otro',
            8: 'Duplex',
            9: 'Triplex',
            10: 'Chalet',
            11: 'Cabania',
            12: 'Casa',
            13: 'Casa',
            14: 'Casas',
            15: 'Departamentos',
            16: 'Terrenos',
            17: None,
            18: None,
            19: None,
            20: 'Galpones',
            21: 'Depósitos',
            22: 'Edificios industriales',
            23: None,
            24: None,
            25: None,
            26: None
        }
    }

    id = models.AutoField(primary_key=True, db_index=True)
    category = models.ForeignKey(Category, verbose_name=_('Category'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))

    class Meta:
        db_table = "core_sub_category"
        app_label = "core"
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')

    def get_zonaprop_subcategory(self):
        return self.SUBCATEGORY_MAP['zonaprop'][self.id]

    def __unicode__(self):
        return self.name