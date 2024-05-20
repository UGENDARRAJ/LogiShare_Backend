from django.contrib import admin
from .models import Shipment, Shipper, Customer 

# Register your models here.

admin.site.register(Shipment)
admin.site.register(Shipper)
admin.site.register(Customer)