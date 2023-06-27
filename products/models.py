from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=30000)
    sku = models.IntegerField()
    price = models.FloatField()
    subtitle = models.TextField(max_length=600)
    image = models.ImageField(upload_to='products')
    brand = models.ForeignKey('Brand',on_delete=models.CASCADE,related_name='product_brand')
    def __str__(self):
        return self.name
    

class ProductsImages(models.Model):
    product = models.ForeignKey(Product,related_name='product_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand')
    def __str__(self):
        return self.name

class Reviews(models.Model):
    user = models.ForeignKey(User,related_name='user_review',on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,related_name='product_review',on_delete=models.SET_NULL,null=True,blank=True)
    review = models.TextField(max_length=500)
    rate = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    create_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user} = {self.product}"