from django.urls import path, include
from . import views

urlpatterns = [
    path('doctorslist',views.doctors_list_view, name="doctors_list_view"),
]