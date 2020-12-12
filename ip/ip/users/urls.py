from django.urls import path, include


urlpatterns = [
    path('hireapi/',include('users.hireapi.urls'))
]