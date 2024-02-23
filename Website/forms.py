from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django import forms


class AvatarForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']
