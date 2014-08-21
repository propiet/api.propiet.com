from django import forms            
from django.contrib.auth.models import User
from core.models.user_profile import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["phone"]