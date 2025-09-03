from django import forms
from .models import URL_Box

class URL_Form(forms.ModelForm):
    class Meta:
        model=URL_Box
        fields='__all__'