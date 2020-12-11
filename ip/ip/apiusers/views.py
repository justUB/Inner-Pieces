from django.shortcuts import render,redirect
import json,requests

from .forms import UserRegisterForm,loginform#,UserInfoForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#tokey = {}
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #user_info_form = UserInfoForm(request.POST)
        if form.is_valid() :
            user = form.save()
            #user_info = user_info_form.save(commit=False)
            #user_info.user = user
            #user_info.save()
            

            return redirect('api_login')
    else:
        form = UserRegisterForm()
        #user_info_form = UserInfoForm()
    return render(request, 'register.html', {'form':form,})



def login_view(request):
    form = loginform(request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if request.user.tokey == '0':
        	data = {'username': username, 'password': password}
        	r = requests.post(url = "http://127.0.0.1:8000/api-token-auth/", data = data)
        	data = r.json()
        #global tokey
        	request.user.tokey = data['token'] 
        	print(request.user.tokey)
        	request.user.save()
        	#print(data['token'])
        #messages.success(request, f"Welcome {username}, You have been Logged In")
        return redirect('api_profile')
    else:
        form = loginform()
        #messages.error(request, f"Invalid Credentials")
    return render(request,'login.html',{'form':form})

@login_required
def profile(request):
	key = request.user.tokey
	return render(request, 'api token.html',{'key': key})

@login_required
def logout_view(request):
    logout(request)
    
    return redirect("api_login")
