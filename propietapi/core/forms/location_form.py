from django import forms            
from core.models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location