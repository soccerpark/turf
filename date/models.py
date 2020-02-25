from django.db import models

# Create your models here.
class book(models.Model):
    username = models.CharField(max_length=150)
    date = models.DateField()
    stime = models.TimeField()
    etime =models.TimeField()
