from django.shortcuts import render
from .models import Hospital
from .serializers import HospitalSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["POST"])
def hospital_signup(request):
    serializer = HospitalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
