from django.db import models

# Create your models here.

class Userdata(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=25)

class Book_data(models.Model):
    fname=models.CharField(max_length=(50))
    lname=models.CharField(max_length=(50))
    email=models.EmailField()
    doctor=models.CharField(max_length=(50))
    amount=models.IntegerField()
    address=models.TextField()
    treat=models.CharField(max_length=(50))
    date=models.CharField(max_length=(50))
    contact=models.IntegerField()