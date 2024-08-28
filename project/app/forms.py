from django import forms
from .models import *

class employee_form(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    position=forms.CharField()

class model_form(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'
        