from django.contrib import admin
from .models import Order , OrderDetail , Cart , CartDetail , Coupon
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart)
admin.site.register(CartDetail)
admin.site.register(Coupon)
