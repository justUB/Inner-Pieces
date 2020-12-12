from django.test import TestCase, Client
from django.urls import reverse
from ecommerce.models import User,cart_item,cart
import json

class testViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user =  User.objects.create(username = 'testcase', email = 'testcase@email.com',is_patient= 'True')

    def test_register_view(self):
        client = Client()

        response = client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_patient_register_view(self):
        client = Client()

        response = client.get(reverse('patient_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/patient_register.html')

    def test_doctor_register_view(self):
        client = Client()

        response = client.get(reverse('doctor_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/doctor_register.html')

    def test_api_register_view(self):
        client = Client()

        response = client.get(reverse('api_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_api_login_view(self):
        client = Client()

        response = client.get(reverse('api_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    




        


