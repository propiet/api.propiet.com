# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from cities_light.models import Country, Region, City
from django.utils.translation import ugettext_lazy as _


# Location Model
class Location(models.Model):
    """Class Location
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""

    LOCATION_MAP = {
        'zonaprop': {
            1: 3661, 2: 3700, 3: 3667, 4: 3683, 5: 3686, 6: 3659, 7: 3652, 8: 3682, 9: 3703, 10: 3693, 11: 13958,
            12: 3671, 13: 3665, 14: 3651, 15: 3678, 16: 3653, 17: 3691, 18: 3687, 19: 3654, 20: 3648, 21: 3676,
            22: 3676, 23: 3699, 24: 3695, 25: 3697, 26: 3674, 27: 3694, 28: 3688, 29: 3662, 30: 3644, 31: 3649,
            32: 3681, 33: 3670, 34: 3702, 35: 3655, 36: 3675, 37: 3656, 38: 3698, 39: 3679, 40: 3646, 41: 3689,
            42: 3696, 43: 3690, 44: 3663, 45: 3701, 46: 3658, 47: 3666, 48: 3669, 49: 3672, 50: 3660, 51: 3647,
            52: 3650, 53: 3685, 54: 3664, 55: 3668, 56: 3657, 57: 3645
        }
    }

    id = models.AutoField(primary_key=True, db_index=True)
    address = models.CharField(max_length=500, verbose_name=_('Address'))
    longitude = models.CharField(max_length=100, blank=True, null=True, default=0, verbose_name=_('Longitude'))
    latitude = models.CharField(max_length=100, blank=True, null=True, default=0, verbose_name=_('Latitude'))
    country = models.ForeignKey(Country, null=True, verbose_name=_('Country'))
    region = models.ForeignKey(Region, null=True, verbose_name=_('Region'))
    city = models.ForeignKey(City, null=True, verbose_name=_('City'))

    class Meta:
        db_table = "core_location"
        app_label = "core"
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    def get_user(self):
        return self.user

    # def get_zonaprop_cod(self):
    #     try:
    #         return self.LOCATION_MAP['zonaprop'][self.city_id]
    #     except KeyError:
    #         return None

    def __unicode__(self):
        return self.address + ' > ' + self.region.name + '-' + self.city.name