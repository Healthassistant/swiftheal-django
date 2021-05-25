from hospital.models import Hospital
from rest_framework import serializers
from .models import Doctor


class TopDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["Name", "Area_of_Specialisation", "Qualification", "Photo"]

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'