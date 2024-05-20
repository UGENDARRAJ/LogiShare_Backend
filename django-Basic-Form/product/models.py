from django.db import models

# Create your models here.

class Shipment(models.Model):
    Type=models.CharField(max_length=20,default="MiniTruck")
    Length=models.IntegerField(default="0")
    Width=models.IntegerField(default="0")
    Height=models.IntegerField(default="0")
    Weight=models.IntegerField(default="0")
    Quantity = models.IntegerField(default="0")
    Pickup = models.CharField(max_length=20,default="Pick")
    Drop = models.CharField(max_length=20,default="Drop")
    
    
class Shipper(models.Model):
    username = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    
class Customer(models.Model):
    username = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    token = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return self.username