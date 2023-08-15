from django.db import models
from django.utils import timezone
from accounts.models import Address
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.


ORDER_STATUS = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shippped'),
    ('Delivered','Delivered'),
    
)


class Order(models.Model):
    user = models.ForeignKey(User,related_name='user_order' , on_delete=models.SET_NULL , null=True , blank=True)
    code = models.CharField(max_length=30)
    status = models.CharField(max_length=30, choices=ORDER_STATUS)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True , blank=True)
    delivery_location = models.ForeignKey(Address,related_name='delivery_address', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return str(self.user)
    
    

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_detail' , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_product', on_delete=models.SET_NULL)
    price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField()
    def __str__(self):
        return str(self.order)
    
    
    
class Cart(models.Model):
    user = models.ForeignKey(User,related_name='user_cart' , on_delete=models.SET_NULL , null=True , blank=True)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)

    
    
class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_detail' , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_product', on_delete=models.SET_NULL)
    price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField()
    
    def __str__(self):
        return str(self.product)