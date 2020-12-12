from django.test import SimpleTestCase
from django.urls import reverse, resolve

from users import views as user_views
from apiusers import views as apiuser_views

class TestUrls(SimpleTestCase) :
    def test_register_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEqual(resolve(url).func, user_views.register)

    def test_patient_register_is_resolved(self):
        url = reverse('patient_register')
        print(resolve(url))
        self.assertEqual(resolve(url).func, user_views.patient_register)
    
    def test_doctor_register_is_resolved(self):
        url = reverse('doctor_register')
        print(resolve(url))
        self.assertEqual(resolve(url).func, user_views.doctor_register)

    def test_profile_update_is_resolved(self):
        url = reverse('profile_update')
        print(resolve(url))
        self.assertEqual(resolve(url).func, user_views.profile_update)

    def test_get_profile_is_resolved(self):
        url = reverse('get_profile')
        print(resolve(url))
        self.assertEqual(resolve(url).func, user_views.get_doctor_profile)

    def test_api_register_is_resolved(self):
        url = reverse('api_register')
        print(resolve(url))
        self.assertEqual(resolve(url).func, apiuser_views.register)

    def test_api_login_is_resolved(self):
        url = reverse('api_login')
        print(resolve(url))
        self.assertEqual(resolve(url).func, apiuser_views.login_view)

    def test_api_logout_is_resolved(self):
        url = reverse('api_logout')
        print(resolve(url))
        self.assertEqual(resolve(url).func, apiuser_views.logout_view)

    def test_api_profile_is_resolved(self):
        url = reverse('api_profile')
        print(resolve(url))
        self.assertEqual(resolve(url).func, apiuser_views.profile)

