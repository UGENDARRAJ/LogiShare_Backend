from django.db import models

# Create your models here.

class Datas(models.Model):
    Type=models.CharField(max_length=20,default="MiniTruck")
    Length=models.IntegerField(default="0")
    Width=models.IntegerField(default="0")
    Height=models.IntegerField(default="0")
    Weight=models.IntegerField(default="0")
    Quantity = models.IntegerField(default="0")
    Pickup = models.CharField(max_length=20,default="Pick")
    Drop = models.CharField(max_length=20,default="Drop")