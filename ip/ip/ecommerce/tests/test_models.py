from django.test import TestCase,SimpleTestCase
from django.urls import resolve,reverse
from ecommerce.models import item,cart,User

class itemTest(TestCase):
    def testfields(self):
        Item = item()
        Item.name = "TestItem"
        Item.desc = "Some test desc"
        Item.category = "Gadgets"
        Item.price = 123
        Item.rating = 2
        Item.seller = "dev"
        Item.save()

        record = item.objects.get(pk=1)
        self.assertEqual(record,Item)

class OrderTest(TestCase):
    def testfields(self):
        user = User.objects.create(username="Testuser", email = "Testuser@gmail.com")
        Order = cart()
        Order.user = user
        Order.transaction_id = 12323
        Order.save()
        print(2)
        record = cart.objects.get(pk=1)
        self.assertEqual(record,Order)