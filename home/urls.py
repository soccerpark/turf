from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('Home/About/',views.about, name='about'),
        path('Home/bookings/',views.bookings, name='bookings'),
        path('Home/clogin/',views.clogin, name='clogin'),
        path('Home/pdp/',views.pdp, name='pdp'),
        path('Home/tournament/',views.tournament, name='tournament'),

]
