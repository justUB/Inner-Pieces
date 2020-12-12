from rest_framework import serializers
from django.db import models
from users.models import Doctor, User
from feedback.models import Feedback 

class UserlistSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=200)
    lastname = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def create(self, validated_data):
        return User(**validated_data)

class DoctorlistSerializer(serializers.Serializer) :
    user = UserlistSerializer(read_only=True)
    experience = serializers.IntegerField()
    hospital_name = serializers.CharField(max_length=200)
    specialization = serializers.CharField(max_length=200)
    consultation_fee = serializers.IntegerField()

    def  create(self, validated_data) :
        return Doctor(**validated_data)

class FeedbackSerializer(serializers.Serializer) :
    doctor = DoctorlistSerializer(read_only=True)
    content = serializers.CharField()
    title = serializers.CharField(max_length=100)
    date_posted = serializers.CharField()

    def create(self, validated_data) :
        return Feedback(**validated_data)

    