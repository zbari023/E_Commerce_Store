from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=30000)
    sku = models.IntegerField()
    price = models.FloatField()
    subtitle = models.TextField(max_length=600)
    brand = models.ForeignKey('Brand',on_delete=models.CASCADE,related_name='product_brand')
    def __str__(self):
        return self.name
    

class ProductsImages(models.Model):
    pass 

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand')
    def __str__(self):
        return self.name

class Reviews(models.Model):
    pass