from django import forms

class MyForm(forms.Form):
    place=forms.CharField(max_length=100)
