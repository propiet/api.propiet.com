from django import forms            
from core.models import PostPhoto

class PostPhotoForm(forms.ModelForm):
    class Meta:
        model = PostPhoto