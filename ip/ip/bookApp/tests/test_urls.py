from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bookApp.views import mainPage,doctor_profile,booking,confirmation

class TestUrls(SimpleTestCase):

    def test_bookApp(self):
        url=reverse('bookApp')
        self.assertEquals(resolve(url).func, mainPage)

    def test_doctor(self):
        url=reverse('doctor', args=['some-slug'])
        self.assertEquals(resolve(url).func, doctor_profile)

    def test_booking(self):
        url=reverse('booking', args=['some-slug'])
        self.assertEquals(resolve(url).func, booking)

    def test_doctor(self):
        url=reverse('confirmation', args=['some-slug'])
        self.assertEquals(resolve(url).func, confirmation)



