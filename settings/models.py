from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company')
    call_us = models.CharField(max_length=25, null=True , blank=True)
    email_us = models.CharField(max_length=25, null=True , blank=True)
    subtitle = models.TextField(max_length=200, null=True , blank=True)
    email = models.TextField(max_length=200, null=True , blank=True)
    phones = models.TextField(max_length=200, null=True , blank=True)
    address = models.TextField(max_length=200, null=True , blank=True)
    fb_link = models.URLField(null=True , blank=True)
    insta_link = models.URLField(null=True , blank=True)
    tiktok_link = models.URLField(null=True , blank=True)
    youtube_link = models.URLField(null=True , blank=True)
    android_store = models.URLField(null=True , blank=True)
    apple_store = models.URLField(null=True , blank=True)
    
    def __str__(self):
        return self.name
    
    
class DeliveryFee(models.Model):
    fee = models.FloatField()
    def __str__(self):
        return str(self.fee)
    