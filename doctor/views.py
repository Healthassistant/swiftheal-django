from django.shortcuts import render
from .models import Doctor
from .serializers import TopDoctorSerializer, DoctorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET"])
def top_doctors(request):
    doctors = Doctor.objects.all().order_by("?")[:8]
    serializer = TopDoctorSerializer(doctors, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def doctor_signup(request):
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save();
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)