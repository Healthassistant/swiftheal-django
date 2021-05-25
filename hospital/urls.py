from django.urls import path
from .views import hospital_signup

urlpatterns = [path("hospitals/", hospital_signup)]
