from django import forms            
from core.models import Post

class PostStatusForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["status"]