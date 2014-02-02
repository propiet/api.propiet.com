from django.db import models
from core.models import Property


# Field Model
class Field(Property):
    """Class Field
    @author: Lionel Cuevas <lionel@hoopemedia.com>"""
    
    SUITABLE = (
        (0, 'No especificado'),
        (1, 'Si'),
        (2, 'No'),        
    )
    
    hectares = models.FloatField()    

    class Meta:
        db_table = "core_property_field"
        app_label = "core"