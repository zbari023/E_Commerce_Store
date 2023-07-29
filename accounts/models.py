from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from utils.generate_code import generate_code


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='accounts')
    code = models.CharField(max_length=10,default=generate_code)

    def __str__(self):
        return str(self.user)



PHONE_CHOICES = (
    ('Primary' , 'Primary'),
    ('Secondary' , 'Secondary'),
    )

class Phones(models.Model):
    user = models.ForeignKey(User,related_name='user_phone',on_delete=models.CASCADE)
    type = models.CharField(max_length=10,choices=PHONE_CHOICES)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user)





ADDRESS_CHOICES = (
    ('Home' , 'Home'),
    ('Office' , 'Office'),
    ('Bussines' , 'Bussines'),
    ('Academy' , 'Academy'),
    ('Other' , 'Other'),
    )
class Address(models.Model):
    user = models.ForeignKey(User,related_name='user_address',on_delete=models.CASCADE)
    type = models.CharField(max_length=10,choices=ADDRESS_CHOICES)
    address = models.TextField(max_length=200)

    def __str__(self):
        return str(self.user)