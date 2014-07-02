# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Category Model
class Category(models.Model):
    """Class Category
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""

    CATEGORY_MAP = {
        'zonaprop': {
            1: 'Departamentos',
            2: 'Casas',
            3: 'Casas',
            4: 'Countries y Barrios cerrados',
            5: 'Quintas',
            6: 'Terrenos y Lotes',
            7: 'Campos y Chacras',
            8: 'Galpones, Depósitos y Edificios industriales',
            9: 'Locales comerciales',
            10: 'Oficinas',
            11: 'Consultorios',
            12: 'Cocheras'
        }
    }

    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=100, verbose_name=_('Name'))

    class Meta:
        db_table = "core_category"
        app_label = "core"
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def get_zonaprop_category(self):
        return self.CATEGORY_MAP['zonaprop'][self.id]

    def __unicode__(self):
        return self.name