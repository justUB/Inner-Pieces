from django.test import TestCase,SimpleTestCase
from django.urls import resolve,reverse
from ecommerce.views import store,cart_page,checkout,updateitem,processOrder

class TestUrls(SimpleTestCase):
    def test_store_url_resolve(self):
        url = reverse('store')
        print("Store url test")
        self.assertEqual(resolve(url).func,store)

    def test_cart_url_resolve(self):
        url = reverse('cart')
        print("cart url test")
        self.assertEqual(resolve(url).func,cart_page)

    def test_checkout_url_resolve(self):
        url = reverse('checkout')
        print("checkout url test")
        self.assertEqual(resolve(url).func,checkout)

    def test_upIt_url_resolve(self):
        url = reverse('update_item')
        print("update item url test")
        self.assertEqual(resolve(url).func,updateitem)

    def test_pOrd_url_resolve(self):
        url = reverse('process_order')
        print("process order url test")
        self.assertEqual(resolve(url).func,processOrder)