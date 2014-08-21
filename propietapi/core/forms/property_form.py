from django import forms            
from core.models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property