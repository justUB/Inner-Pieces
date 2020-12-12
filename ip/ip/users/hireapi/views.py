from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import Doctor, User
from .serializers import UserlistSerializer, DoctorlistSerializer

@api_view(http_method_names=['GET',])
def doctors_list_view(request):
    data= Doctor.objects.all()
    serializer = DoctorlistSerializer(data, many=True)
    return Response(data=serializer.data)