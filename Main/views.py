from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def contact_us(request):
    return render(request, "contactus.html")

def about_us(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")