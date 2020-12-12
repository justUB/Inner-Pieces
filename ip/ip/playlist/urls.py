from django.urls import path

from . import views as playlist_views

urlpatterns = [
    path('',playlist_views.playlist,name="playlist"),
]