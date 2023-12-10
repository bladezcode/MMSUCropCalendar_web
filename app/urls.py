from django.urls import path
from . import views

urlpatterns = [
    path("", views.app, name="app"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("calendar", views.calendar, name="calendar"),
    path("sensors", views.sensors, name="sensors"),
    path("analytics", views.analytics, name="analytics"),
    path("info", views.info, name="info")
    
]

