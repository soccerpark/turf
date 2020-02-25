from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from date.models import book
# Create your views here.

def date(request):
    return render(request, "date.html")

def logout(request):
    auth.logout(request);
    return redirect('/')

def booking(request):
    if request.method == 'POST':
        date = request.POST['date']
        etime = request.POST['etime']
        stime = request.POST['stime']
        username = request.POST['username']
        if book.objects.filter(date=date, stime=stime, etime=etime).exists():
          messages.info(request,'Slot Already Booked')
          return redirect('date')
        else:
            res = book(username = username, date = date, stime = stime, etime = etime)
            res.save();
            return render(request,'date.html')
            messages.info(request,'Slot Reserved')
    else:
        return render(request, 'date.html')
