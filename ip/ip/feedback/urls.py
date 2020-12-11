from django.urls import path
from . import views as feedback_views

urlpatterns = [
    path('',feedback_views.home,name='feedback'),
    path('doctor/<doctor_name>',feedback_views.doctor_profile,name='doctor'),
    path('new/<doctor_name>', feedback_views.FeedbackCreateView, name='create-feedback'),
]
