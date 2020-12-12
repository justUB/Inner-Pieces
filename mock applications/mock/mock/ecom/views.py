from django.shortcuts import render,redirect
import json,requests

from .forms import UserRegisterForm,loginform,UserInfoForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect






headers = {'Authorization': 'Token f8bfa8f4f8576054c737ce6102d9045c710f7723'}

@login_required
def home(request):
    return render(request,'main.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        user_info_form = UserInfoForm(request.POST)
        if form.is_valid() and user_info_form.is_valid():
            user = form.save()
            user_info = user_info_form.save(commit=False)
            user_info.user = user
            user_info.save()

            return redirect('login')
    else:
        form = UserRegisterForm()
        user_info_form = UserInfoForm()
    return render(request, 'register.html', {'form':form, 'user_info_form': user_info_form})



def login_view(request):
    form = loginform(request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        #messages.success(request, f"Welcome {username}, You have been Logged In")
        return redirect('home')
    else:
        form = loginform()
        #messages.error(request, f"Invalid Credentials")
    return render(request,'login.html',{'form':form})


@login_required
def store(request):
    items = requests.get(url = "http://localhost:8000/ecom/api/",headers=headers)
    items = items.json()
    #print(items[0])
    return render(request,'store.html',{'items':items})

@login_required
def order(request,param1,param2):
    #x = slug.split("_")
    data = {}
    data['itemName'] = param1
    data['action'] = param2
    data['username'] = request.user.username
    data['email'] = request.user.user_info.email
    data = json.dumps(data)

    c_items = requests.post(url = "http://localhost:8000/ecom/api/cart_api/",headers=headers, data=data)
    items = requests.get(url = "http://localhost:8000/ecom/api/" ,headers=headers)
    items = items.json()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #return HttpResponseRedirect("")
    #return render(request,'store.html',{'items':items})

@login_required
def cart(request):
    data = {}
    data['username'] = request.user.username
    data['email'] = request.user.user_info.email
    data = json.dumps(data)
    print(data)
    c_items = requests.get(url = "http://localhost:8000/ecom/api/cart_api/",headers=headers,data=data) 
    #c_items = c_items.json()
    if c_items.status_code == 404 :
        c_items = None
    else: 
        c_items = c_items.json()
    
    items = requests.get(url = "http://localhost:8000/ecom/api/",headers=headers)
    items = items.json()
    order = requests.get(url = "http://localhost:8000/ecom/api/order_get/",headers=headers,data=data)
    #order = order.json()

    if order.status_code == 404 :
        order = None
    else: 
        order = order.json()
    return render(request,'cart.html',{'c_items':c_items,'items':items,'order':order,})


@login_required
def finalize(request):
    
    data = {}
    data['username'] = request.user.username
    data['email'] = request.user.user_info.email
    data = json.dumps(data)
    c = requests.post(url = "http://localhost:8000/ecom/api/chkout_api/",headers=headers,data=data)
    c = c.json()
    c_items = requests.get(url = "http://localhost:8000/ecom/api/cart_api/",headers=headers,data=data)
    items = requests.get(url = "http://localhost:8000/ecom/api/",headers=headers)
    items = items.json()
    if c_items.status_code == 404 :
        c_items = None
    else: 
        c_items = c_items.json()
    
    return render(request,'cart.html',{'c_items':c_items,'items':items,'c':c,})
