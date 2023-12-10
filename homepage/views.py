from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "homepage/home.html")
def about(request):
    return render(request, "homepage/about.html")
def riceseed_info(request):
    return render(request, "homepage/riceseed_info.html")
def hardware_info(request):
    return render(request, "homepage/hardware_info.html")
