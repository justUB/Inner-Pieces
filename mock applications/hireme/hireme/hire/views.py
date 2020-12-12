from django.shortcuts import render
import requests
# Create your views here.

def get_psychologists():
    psy = requests.get("http://127.0.0.1:8000/users/hireapi/doctorslist")
    return psy.json()

def index_view(request):
    context = {'psylist' : get_psychologists()}
    return render(request, 'hire/psycho.html', context=context)

def main(request):
    return render(request, 'hire/main.html')

def doctor_profile(request,doctor):
    return render(request,'hire/get_doctor_profile.html',{'doctor': doctor})