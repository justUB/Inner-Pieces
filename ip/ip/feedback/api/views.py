from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter


from django.contrib.auth.models import User
from feedback.models import Feedback
from users.models import Doctor
from .serializers import FeedbackSerializer, DoctorlistSerializer, UserlistSerializer
from django.core import serializers

@permission_classes([IsAuthenticated])
@api_view(http_method_names=['GET',])
def doctors_feedback(request, slug):
    slug = slug.replace("_"," ")
    print("printig slug replace ",slug.replace("_"," "))
    print(slug,"slug")
    l = Doctor.objects.filter(hospital_name=slug)
    
    data =[]
    for i in l:
        if(i.hospital_name==slug):
            data = Feedback.objects.filter(doctor=i)
            serializer = FeedbackSerializer(data, many=True)
            

    serializer = FeedbackSerializer(data, many=True)
    return Response(serializer.data)