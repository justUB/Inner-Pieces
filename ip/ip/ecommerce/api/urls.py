from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('',views.api,name='api'),
    path('cart_api/',views.cart_view,name='cart_api'),
    path('order_get/',views.order_get,name='order_get'),
    path('chkout_api/',views.checkout_view,name='checkout_api'),
    
]