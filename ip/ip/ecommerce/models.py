from django.db import models
from users.models import User

class item(models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=7,decimal_places=2)
    seller = models.CharField(max_length=100)
    image = models.ImageField(default="default.png" ,upload_to="ecom_pics")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True)

    def __str__(self):
        return self.name

class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.id)

    @property
    def total_bill(self):
        cartitems = self.cart_item_set.all()
        total = 0
        for item in cartitems:
            total = total + item.total_price
        
        return total

    @property
    def total_quantity(self):
        cartitems = self.cart_item_set.all()
        total = 0
        for item in cartitems:
            total = total + item.quantity
        
        return total

class cart_item(models.Model):
    item = models.ForeignKey(item,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(cart,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=0, null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        total = self.quantity * self.item.price
        return total

class address(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(cart,on_delete=models.SET_NULL,null=True,blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    pincode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address
