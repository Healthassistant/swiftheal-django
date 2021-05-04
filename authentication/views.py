from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.utils import timezone

# Create your views here.
@api_view(["POST"])
def login(request):
    try:
        username = request.data["username"]
        password = request.data["password"]
    except:
        return Response({"message": "Invalid request"}, status=400)
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)

        if ((timezone.now() - token.created).total_seconds()) > 7 * 24 * 60 * 60:
            token.delete()
            return Response({"message": "Session has expired"}, status=401)

        return Response(
            {
                "username": user.username,
                "email": user.email,
                "authorization": token.key,
            },
            status=200,
        )
    else:
        return Response({"message": "Username or Password is incorrect"}, status=401)
