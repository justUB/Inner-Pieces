from django.test import TestCase, Client
from django.urls import reverse
from ecommerce.models import User


class testViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user =  User.objects.create(username = 'testcase', email = 'testcase@email.com',is_patient= 'True')

    def test_mainPage(self):
        client = Client()

        response = client.get(reverse('mainPage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookApp/bookApp.html', arg=['some-slug','some-slug'])


    def test_patient_register_view(self):
        client = Client()

        response = client.get(reverse('patient_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/patient_register.html')


