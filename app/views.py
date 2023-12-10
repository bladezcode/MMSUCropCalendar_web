from django.shortcuts import render, HttpResponse
from app.mqtt_client import start_mqtt_client

def your_view(request):
    # Call the function to start the MQTT client
    start_mqtt_client()
    # Other view logic




# Create your views here.
def app(request):
    return render(request, "app/base.html")
def dashboard(request):
    return render(request, "app/dashboard.html")
def calendar(request):
    return render(request, "app/calendar.html")
def sensors(request):
    return render(request, "app/sensors.html")
def analytics(request):
    return render(request, "app/analytics.html")
def info(request):
    return render(request, "app/info.html")

