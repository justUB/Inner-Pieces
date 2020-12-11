from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    path('cart/', views.cart_page, name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('update_item/',views.updateitem,name='update_item'),
    path('process_order/',views.processOrder,name='process_order'),
    path('api/',include('ecommerce.api.urls'),)
]