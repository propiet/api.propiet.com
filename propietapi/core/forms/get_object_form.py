from django.contrib.contenttypes.models import ContentType
from django import forms

def GetObjectForm(model,  excludes=None):  
    ctype = ContentType.objects.get(app_label="core", model=model)
    model_class = ctype.model_class( )
    class _ObjectForm( forms.ModelForm ):
        class Meta:
            model = model_class
            #excludes = excludes
    return _ObjectForm