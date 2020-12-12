from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm 
from .models import User_info


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1', 'password2']

class UserInfoForm(forms.ModelForm):

    class Meta:
        model = User_info
        fields = ['email']

  
class loginform(forms.Form): 
  
    username = forms.CharField(max_length = 200)
    password = forms.CharField(widget = forms.PasswordInput())