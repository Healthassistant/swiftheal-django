from django.urls import path
from .views import doctor_signup, top_doctors

urlpatterns = [path("top_doctors/", top_doctors), path("doctors/", doctor_signup)]
