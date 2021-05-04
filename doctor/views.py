from django.shortcuts import render
from .models import Doctor
from .serializers import TopDoctorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET"])
def top_doctors(request):
    doctors = Doctor.objects.all().order_by("?")[:8]
    serializer = TopDoctorSerializer(doctors, many=True)
    return Response(serializer.data)
