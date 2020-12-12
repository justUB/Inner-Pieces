from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm 
from .models import User, Patient, Doctor

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','firstname','lastname','email','password1', 'password2']

class PatientRegisterForm(forms.ModelForm):

    class Meta:
        model = Patient
        CHOICES = [('M','Male'),('F','Female')]
        #gender = forms.ChoiceField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
        gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        fields = ['dob','gender','occupation']

        
        
        widgets = {
        'dob': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }

class DoctorRegisterForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ['experience','hospital_name','specialization','consultation_fee','is_interested']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','firstname','lastname','email','image']

class PatientUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        CHOICES = [('M','Male'),('F','Female')]
        #gender = forms.ChoiceField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
        gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        fields = ['dob','gender','occupation']


        widgets = {
            'dob': forms.DateInput(format=('%d/%m/%Y')),
        }

class DoctorUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Doctor
        fields = ['experience','hospital_name','consultation_fee','specialization']

class UserImageUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['image']

        
        