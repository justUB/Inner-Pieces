from django.db import models
''''
from users.models import User
# Create your models here.

class User_info(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    
    def __str__(self):
    	return f'{self.user.username} user_info'
'''
