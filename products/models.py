from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=30000)
    sku = models.IntegerField()
    price = models.FloatField()
    

class ProductsImages(models.Model):
    pass 

class Brand(models.Model):
    pass

class Reviews(models.Model):
    pass