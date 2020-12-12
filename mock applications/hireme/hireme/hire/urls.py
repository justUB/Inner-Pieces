from django.urls import path, include
from . import views

urlpatterns = [
    path('main',views.main, name="main"),
    path('index_view',views.index_view, name="index_view"),
    path('doctor/<doctor>',views.doctor_profile,name='doctor'),
]