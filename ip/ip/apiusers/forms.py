from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm 
from users.models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
''''
class APiUserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']

#class UserInfoForm(forms.ModelForm):

'''

  
class loginform(forms.Form): 
  
    username = forms.CharField(max_length = 200)
    password = forms.CharField(widget = forms.PasswordInput())