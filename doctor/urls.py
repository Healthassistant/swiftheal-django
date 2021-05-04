from django.urls import path
from .views import top_doctors

urlpatterns = [
    path("top_doctors/", top_doctors),
]
