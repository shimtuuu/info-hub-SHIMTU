from django import forms
from .models import CustomUser

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "avatar", "bio"]
