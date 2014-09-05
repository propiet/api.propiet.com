# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Service Model
class Service(models.Model):
    """Class Service
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""

    SERVICE_MAP = {
    'zonaprop': {
        1: 'agua_corriente',
        2: 'desague_cloacal',
        3: 'gas_natural',
        4: 'internet',
        5: 'luz',
        6: 'pavimento',
        7: 'telefono',
        8: 'video_cable'
        }
    }

    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=100, verbose_name=_('Name'))

    class Meta:
        db_table = "core_service"
        app_label = "core"
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    # def get_zonaprop_service(self):
    #     return self.SERVICE_MAP['zonaprop'][self.id]

    def __unicode__(self):
            return self.name