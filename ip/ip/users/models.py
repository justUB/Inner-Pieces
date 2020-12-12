from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
# Create your models here.



class User(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    tokey = models.CharField(max_length = 50, default='0')
    def __str__(self):
    	return f'{self.username} User'


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    dob = models.DateField()
    age = models.IntegerField()
    CHOICES = (('M', 'Male'),('F', 'Female'),)
    gender = models.CharField(max_length = 1, choices = CHOICES)
    occupation = models.CharField(max_length = 200)

    def __str__(self):
    	return f'{self.user.username} Patient'


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    experience = models.IntegerField()
    hospital_name = models.CharField(max_length = 200)
    specialization = models.CharField(max_length = 200)
    consultation_fee = models.IntegerField(validators=[MinValueValidator(0)])
    is_interested=models.BooleanField("is interested", default=False)
    
    def __str__(self):
    	return f'{self.user.username} Dcotor'

