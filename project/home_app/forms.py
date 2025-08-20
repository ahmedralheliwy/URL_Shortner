from django import forms
from .models import URL_Box

class URL_Form(forms.ModelForm):
    class meta:
        fields='__all__'