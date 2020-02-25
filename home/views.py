from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def bookings(request):
    return render(request, "login.html")

def clogin(request):
    return render(request, "clogin.html")

def pdp(request):
    return render(request, "pdp.html")

def tournament(request):
    return render(request, "tournament.html")
