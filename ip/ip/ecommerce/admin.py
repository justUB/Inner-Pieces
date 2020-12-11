from django.contrib import admin
from .models import item,cart,cart_item,address

admin.site.register(item)
admin.site.register(cart)
admin.site.register(cart_item)
admin.site.register(address)
# Register your models here.
