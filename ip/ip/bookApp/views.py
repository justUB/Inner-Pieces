from django.shortcuts import render, redirect
from users.models import Doctor
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def mainPage(request):
    obj2 = Doctor.objects.all()
    count =  Doctor.objects.all().count()
    return render(request, 'bookApp/bookApp.html', {'obj2':obj2, 'count': count})

def doctor_profile(request,doctor_name):
    obj  = Doctor.objects.all()
    doctor = []
    if True:
        for i in obj:
            if i.user.username.capitalize() == doctor_name.capitalize():
                doctor = Doctor.objects.get(user = i.user)
                print('hi')
                print(doctor.user.username)
                print('hello')       
                return render(request,'users/get_doctor_profile.html',{'doctor': doctor})

def booking(request,doctor_name):
    obj  = Doctor.objects.all()
    doctor = []
    if True:
        for i in obj:
            if i.user.username.capitalize() == doctor_name.capitalize():
                doctor = Doctor.objects.get(user = i.user)
                return render(request, 'bookApp/booking.html',{'doctor': doctor})

def confirmation(request,doctor_name):   
    obj  = Doctor.objects.all()
    doctor = []
    if True:
        for i in obj:
            if i.user.username.capitalize() == doctor_name.capitalize():
                doctor = Doctor.objects.get(user = i.user) 
                if request.method == 'POST':
                    Your_Name = request.POST.get('Your-Name', 'my')
                    Your_Phone = request.POST.get('Your-Phone')
                    Your_Email = request.POST.get('Your-Email')
                    Your_Address = request.POST.get('Your-Address')
                    your_schedule = request.POST.get('your-schedule')
                    Date = str(request.POST.get('Date'))
                    Your_message = request.POST.get('Your-message')

                    Appointment =  "Patient Details: \n\n Name: " + Your_Name  + "\n Date: "+ Date + "\n Time: "+ your_schedule + "\n Email: "+ Your_Email + "\n Phone: "+ Your_Phone + "\n Message:"+ Your_message 
                    
                    send_mail(
                        'Appointment request',
                         Appointment,
                        'innerpiecess@gmail.com',
                        [doctor.user.email],
                        fail_silently=True
                    )
                    
                    Patient_Appointment =  "Your Appointment Details: \n\n Name: " + Your_Name  + "\n Email: "+ Your_Email + "\n Phone: "+ Your_Phone + "\n Message:"+ Your_message 
                    
                    send_mail(
                        'Appointment details',
                         Patient_Appointment,
                        'innerpiecess@gmail.com',
                        [Your_Email],
                        fail_silently=True
                    )
        
            
                    return render(request, 'bookApp/confirmation.html', {'Your_Name':Your_Name,'Your_Phone':Your_Phone,'Your_Email':Your_Email,'Your_Address':Your_Address,'your_schedule':your_schedule,'Date':Date,'Your_message':Your_message,'doctor_name': doctor_name})
                else:
                    return render(request, 'bookApp/booking.html',{'doctor_name': doctor.user.username})