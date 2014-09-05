# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Operation Model
class Operation(models.Model):
    """Class Operation
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""

    OPERATION_TYPE = {
    'zonaprop': {
        1: 'venta',
        2: 'alquiler',
        3: 'emprendimiento',
        }
    }

    id = models.AutoField(primary_key=True, db_index=True)
    operation = models.CharField(max_length=100, verbose_name=_('Operation'))

    class Meta:
        db_table = "core_operation"
        app_label = "core"
        verbose_name = _('Operation')
        verbose_name_plural = _('Operations')

    def __unicode__(self):
        return self.operation

    # def get_zonaprop_operation(self):
    #     return self.OPERATION_TYPE['zonaprop'][self.id]