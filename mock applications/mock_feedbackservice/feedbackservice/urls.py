from django.urls import path

from . import views

urlpatterns = [
    path('doctorsfeedback/',views.doctorsFeedback,name="doctorsFeedback"),
    path('',views.home,name="home"),
    
]