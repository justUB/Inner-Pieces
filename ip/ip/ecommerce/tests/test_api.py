import json

from ecommerce.models import User
from django.urls import reverse,resolve
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from ecommerce.api.serializers import *
from ecommerce.models import *
from ecommerce.api.views import *


class Test_store(APITestCase):
    def Test_store(self):
        url = reverse('api')
        print("api store view")
        self.assertEqual(resolve(url).func,api)

class Test_cart(APITestCase):
    def test_cart_get_view(self):
        url = reverse('cart_api')
        print("api cart view")
        self.assertEqual(resolve(url).func,cart_view)


    def test_cart_post_view(self):
        item.objects.create(category="books",name="Gita",desc="Test desc",price=123,seller="test",rating=3)

        data = {"itemName" : "Gita", "action" : "add", "username" : "Testcase", "email" : "apitestcaseemail@email.com"}
        
        response = self.client.post('/ecom/api/cart_api/', data = data,format = "json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        print("api cart post view")

class Test_chkout(APITestCase):
    def test_chkout_post_view(self):
        data = {"username" : "Testcase", "email" : "apitestcaseemail@email.com"}
        
        response = self.client.post('/ecom/api/chkout_api/', data = data,format = "json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        print("api checkout post view")