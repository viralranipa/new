from dataclasses import field
from pyexpat import model
from django import forms
from .models import signup

class signupform(forms.ModelForm):
    class Meta:
        model=signup
        fields="__all__"