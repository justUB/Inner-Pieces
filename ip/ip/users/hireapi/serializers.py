from rest_framework import serializers 
from users.models import Doctor, User

class UserlistSerializer(serializers.Serializer):
    username = serializers. CharField()
    email = serializers .EmailField(max_length=60)
    firstname = serializers .CharField(max_length = 200)
    lastname = serializers .CharField(max_length = 200)
    is_patient = serializers .BooleanField()
    is_doctor = serializers .BooleanField()
    image = serializers .ImageField()

    def create(self, validated_data):
        return User(**validated_data)

class DoctorlistSerializer(serializers.Serializer):
    user = UserlistSerializer(read_only = True)
    experience = serializers .IntegerField()
    hospital_name = serializers .CharField(max_length = 200)
    specialization = serializers .CharField(max_length = 200)
    consultation_fee = serializers .IntegerField()
    is_interested=serializers .BooleanField("is interested")

    def create(self, validated_data):
        return Doctor(**validated_data)
