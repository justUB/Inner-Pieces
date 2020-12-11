from django import forms
from django.forms import ModelForm 
from .models import address

class address_form(forms.ModelForm):
    class Meta:
        model = address
        fields = ['address','city','state','pincode']