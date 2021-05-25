from django.db.models.query import QuerySet
from rest_framework.fields import ReadOnlyField
from hospital.models import Hospital
from rest_framework import serializers
from .models import Doctor


class TopDoctorSerializer(serializers.ModelSerializer):
    Hospital = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Doctor
        fields = [
            "Doctor_ID",
            "Name",
            "Hospital",
            "Area_of_Specialisation",
            "Qualification",
            "Photo",
        ]


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
