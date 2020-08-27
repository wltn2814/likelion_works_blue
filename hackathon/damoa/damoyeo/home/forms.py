from django import forms
from .models import Home
class HomeUpdate(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['title', 'body', 'kakaoid', 'phonenumber']