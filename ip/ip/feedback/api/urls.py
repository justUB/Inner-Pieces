from django.urls import path

from . import views as feedback_API_views 

urlpatterns = [
    path('doctors_feedback/<slug:slug>',feedback_API_views.doctors_feedback,name="doctors_feedback"),
]