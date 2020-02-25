from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from coachaccounts.models import coach
# Create your views here.

def clogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        cac = auth.authenticate(username=username,password=password)

        if cac is not None:
            auth.login(request, cac)
            return redirect('cacc')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('clogin')

    else:
        return render(request,'clogin.html')

def cacc(request):
    return render(request, "attendance.html")
