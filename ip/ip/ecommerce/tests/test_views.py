from django.test import TestCase, Client
from django.urls import reverse
from ecommerce.models import User,cart_item,cart
import json

class testViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user =  User.objects.create(username = 'testcase', email = 'testcase@email.com')

    def test_store_view(self):
        client = Client()

        response = client.get(reverse('store'))
        print("Store view test")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecom.html')

    def test_cartPage_view(self):
        client = Client()

        response = client.get(reverse('cart'))
        print("cart page view test")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    def test_checkout_view(self):
        client = Client()

        response = client.get(reverse('checkout'))
        print("checkout view test")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')

    '''def test_upItem_view(self):
        client = Client()

        order = cart.objects.create(user = self.user, complete=False)

        response = client.post(reverse('update_item',{
            'itemName' : "Peace of Mind",
            'action' : "add",
        }))'''


        


