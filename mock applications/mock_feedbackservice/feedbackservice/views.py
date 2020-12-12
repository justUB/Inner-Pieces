from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages 
import requests
import json 

headers = {'Authorization':'d90b4be92db2c0d8348fdcc4c22af22eb0428964'}

# Create your views here.
def doctorsFeedback1(request):

    if request.method == 'POST':
        srch = request.POST['srh']
        srch = srch.replace(" ","_")

        if srch :
            l = 'http://127.0.0.1:8000/feedbackapi/doctors_feedback/' + srch
            match = requests.get(url=l,headers=headers)
            match = match.json()
                        
            if match :
                return render(request,'feedbackservice/doctorsFeedback.html',{'feedback':match})
            else :
                messages.error(request,'no result found')
    #else :
     #   return HttpResponseRedirect('/doctorsfeedback/')

    return render(request,'feedbackservice/doctorsFeedback.html',)

def doctorsFeedback(request):

    
        
    l = 'http://127.0.0.1:8000/feedbackapi/doctors_feedback/The_seventh_sense_hospital' 
    #match = requests.get('http://127.0.0.1:8000/feedbackapi/doctors_feedback/The_seventh_sense_hospital')
    match = requests.get(url=l,headers=headers)
    match = match.json()
                
    if match :
        return render(request,'feedbackservice/doctorsFeedback.html',{'feedback':match})
    else :
        messages.error(request,'no result found')
    

def home(request):
    return render(request,'feedbackservice/index.html')