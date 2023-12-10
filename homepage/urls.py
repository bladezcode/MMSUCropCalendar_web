from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("riceseed_info", views.riceseed_info, name="riceseed_info"),
    path("hardware_info", views.hardware_info, name="hardware_info"),
    
]
