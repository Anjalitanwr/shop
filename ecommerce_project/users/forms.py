from django import forms
from .models import UserProfile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['fname', 'lname', 'image']
