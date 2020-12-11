from django.shortcuts import render, redirect
from .forms import FeedbackCreateForm
from django.contrib.auth.decorators import login_required
from .models import Feedback
from users.models import Doctor
# Create your views here.

def home(request):
	obj2  = Doctor.objects.all()
	count =  Doctor.objects.all().count()
	count2 = 1
	count3 = 2
	print(count)
	print(count2)
	return render(request, 'feedback/feedback.html', {'obj2':obj2, 'count': count})

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
			#else:
			#	print('not found hi')
			#	return render(request,)

	#return render(request, 'feedback/index.html',{'obj':obj})
	#comps = Company.objects.all()

#@login_required
def FeedbackCreateView(request,doctor_name):
	
	doctors  = Doctor.objects.all()
	feedback  = Feedback.objects.all()
	obj = []
	feedbacks_by_user = []
	flag = 0
	if True:
		for i in doctors:
			if i.user.username.capitalize() == doctor_name.capitalize():
				doctor = Doctor.objects.get(user = i.user)
				print('hi')
				print(doctor.user.username)
				print('hello')
				obj = Feedback.objects.filter(doctor = doctor).order_by('-date_posted')
				

				#if obj:
				#	for i in obj:
				#		if i.patient == request.user.patient:
				#			flag = 1
				#		else:
				#			print('you cannot write another feedback')
				if request.user.is_authenticated:
					feedbacks_by_user = Feedback.objects.filter(patient = request.user.patient)
				for i in feedbacks_by_user:
					print(i.patient)

				if request.method == 'POST' and request.user.is_authenticated and request.user.is_patient:

					

					form = FeedbackCreateForm(request.POST)
					
					if form.is_valid():
						feedback_model = form.save(commit=False)
						feedback_model.patient = request.user.patient
						feedback_model.doctor = doctor
						print('hi')
						print(request.user.patient.age)
						feedback_model.save()

						return redirect('create-feedback',doctor_name=doctor.user.username)
				else:
					form = FeedbackCreateForm()
				return render(request, 'feedback/create_feedback.html', {'form':form, 'obj':obj, 'feedbacks_by_user': feedbacks_by_user})
	#return render(request, 'feedback/create_feedback.html', {'obj':obj})

