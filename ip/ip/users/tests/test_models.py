from django.test import TestCase,SimpleTestCase
from django.urls import resolve,reverse
from users.models import User, Patient, Doctor

class userTest(TestCase):
    def testfields(self):
        user = User()
        user.email = "TestItem"
        user.firstname = "Some test desc"
        user.lastname = "Gadgets"
        user.save()

        record = User.objects.get(pk=1)
        self.assertEqual(record,user)

class PatientTest(TestCase):
    def testfields(self):
        user = User.objects.create(username="Testuser", email = "Testuser@gmail.com")
        patient = Patient()
        patient.user = user
        patient.dob = '2017-12-11'
        patient.age = 20
        patient.gender = 'M'
        patient.occupation = 'h'
        patient.save()
        record = Patient.objects.get(pk=1)
        self.assertEqual(record,patient)

class DoctorTest(TestCase):
    def testfields(self):
        user = User.objects.create(username="Testuser", email = "Testuser@gmail.com")
        doctor = Doctor()
        doctor.user = user
        doctor.experience = 20
        doctor.hospital_name = 'h'
        doctor.specialization = 'h'
        doctor.consultation_fee = 20
        doctor.save()
        record = Doctor.objects.get(pk=1)
        self.assertEqual(record,doctor)