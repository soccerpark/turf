from django.urls import path
from . import views
urlpatterns = [

        path('clogin',views.clogin, name='clogin'),
        path('cacc',views.cacc, name='cacc'),

]
