from django import forms            
from core.models import Post

class PostAgentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["agent","status"]