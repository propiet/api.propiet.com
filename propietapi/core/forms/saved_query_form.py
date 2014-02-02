from django import forms            
from core.models import SavedQuery

class SavedQueryForm(forms.ModelForm):
    class Meta:
        model = SavedQuery