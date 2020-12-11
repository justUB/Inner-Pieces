from django.db import models
from users.models import Patient, Doctor
from django.utils import timezone

class Feedback(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    content = models.TextField()
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    #date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient.user.username} Feedback'

class home(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return f'{self.doctor.user.username} home'