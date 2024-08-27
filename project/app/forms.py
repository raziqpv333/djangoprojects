from django import forms


class employee_form(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    position=forms.CharField()