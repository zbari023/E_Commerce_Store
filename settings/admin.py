from django.contrib import admin

# Register your models here.
from .models import Company, DeliveryFee

admin.site.register(Company)
admin.site.register(DeliveryFee)
