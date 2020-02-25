from django.urls import path
from . import views
urlpatterns = [

        path('date',views.date, name='date'),
        path('logout',views.logout, name='logout'),
        path('booking',views.booking, name='booking'),

]
