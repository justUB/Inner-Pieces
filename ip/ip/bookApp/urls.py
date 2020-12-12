from django.urls import path
from . import views as bookApp_views


urlpatterns = [
    path('',bookApp_views.mainPage,name='bookApp'),
    path('doctor/<doctor_name>',bookApp_views.doctor_profile,name='doctor'),
    path('booking/<doctor_name>',bookApp_views.booking, name='booking'),
    path('confirmation/<doctor_name>',bookApp_views.confirmation, name='confirmation'),
]
