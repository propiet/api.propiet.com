from django import forms            
from core.models import Alert

class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert