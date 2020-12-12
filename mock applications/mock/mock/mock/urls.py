"""mock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecom import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.register,name = "register"),
    path('home/',views.home,name = "home"),
    path('login/',views.login_view,name = "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='ecom/logout.html'), name='logout'),
    path('store/',views.store,name = "store"),
    path('order/<str:param1>/<str:param2>',views.order,name = "order"),
    path('cart/',views.cart,name = "cart"),
    path('confirm/',views.finalize,name='confirm'),
]
