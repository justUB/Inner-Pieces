from django.shortcuts import render,redirect
from .forms import UserRegisterForm, PatientRegisterForm, DoctorRegisterForm, UserUpdateForm, PatientUpdateForm, DoctorUpdateForm, UserImageUpdateForm
from django.contrib.auth.decorators import login_required
from dateutil.relativedelta import relativedelta
from django.db import transaction
import datetime
from .models import Doctor
# Create your views here.


def register(request):
	return render(request, 'users/register.html', {'title':'Register Page'})

@transaction.atomic
def patient_register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		patient_form = PatientRegisterForm(request.POST)
		if form.is_valid() and patient_form.is_valid():
			user = form.save(commit=False)
			user.is_patient = True
			user.save()
			patient_model = patient_form.save(commit=False)
			today = datetime.date.today()
			delta = relativedelta(today, patient_model.dob)
			patient_model.age = delta.years
			patient_model.user = user
			patient_model.save()

			return redirect('login')
	else:
		form = UserRegisterForm()
		patient_form = PatientRegisterForm()
	return render(request, 'users/patient_register.html', {'form':form, 'patient_form': patient_form,'title':'Patient Register Page'})

@transaction.atomic
def doctor_register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		doctor_form = DoctorRegisterForm(request.POST)
		if form.is_valid() and doctor_form.is_valid():
			user = form.save(commit=False)
			user.is_doctor = True
			user.save()
			doctor_model = doctor_form.save(commit=False)
			doctor_model.user = user
			doctor_model.save()

			return redirect('login')
	else:
		form = UserRegisterForm()
		doctor_form = DoctorRegisterForm()
	return render(request, 'users/doctor_register.html', {'form':form, 'doctor_form': doctor_form,'title':'Dcotor Register Page'})

@login_required
def profile(request):
	if request.user.is_patient:
		return render(request, 'users/profile_patient.html')
	else:
		return render(request, 'users/profile_doctor.html')

@login_required
def profile_update(request):
	if request.user.is_patient:
		if request.method == 'POST':
			form = UserUpdateForm(request.POST,request.FILES,instance=request.user )
			patient_form = PatientUpdateForm(request.POST,instance = request.user.patient)
			
			if form.is_valid() and patient_form.is_valid():
				form.save()
				patient_form.save()
				#messages.success(request, f'Your Account has been Updated!')
				return redirect('profile')
		else:
			form = UserUpdateForm(instance=request.user)
			patient_form = PatientUpdateForm(instance = request.user.patient)
			print('form not valid')
			print(request.user.patient.dob)
			print(request.user.patient.dob.month)
			print(request.user.patient.dob.year)
			print(request.user.patient.dob.day)
		return render(request, 'users/profile_update.html',{'form':form, 'patient_form': patient_form})
	else:
		if request.method == 'POST':
			form = UserUpdateForm(request.POST,request.FILES,instance = request.user )
			doctor_form = DoctorUpdateForm(request.POST,instance = request.user.doctor )

			if form.is_valid() and doctor_form.is_valid():
				form.save()
				doctor_form.save()
				#messages.success(request, f'Your Account has been Updated!')
				return redirect('profile')
		else:
			form = UserUpdateForm(instance = request.user)
			doctor_form = DoctorUpdateForm(instance = request.user.doctor )
		return render(request, 'users/profile_update.html',{'form':form, 'doctor_form':doctor_form})


@login_required
def uploadPhoto(request):
	if request.method == 'POST':
		form = UserImageUpdateForm(request.POST ,request.FILES, instance = request.user )

		if form.is_valid():
			form.save()
				#messages.success(request, f'Your Account has been Updated!')
			return redirect('profile')
	else:
		form = UserImageUpdateForm(instance = request.user)
	return render(request, 'users/uploadPhoto.html',{'form':form})
	#return render(request, 'users/uploadPhoto.html')

def get_doctor_profile(request):
	obj  = Doctor.objects.all()
	return render(request, 'users/get_doctor_profile.html', {'obj': obj})
