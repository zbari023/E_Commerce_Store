from django.shortcuts import render , redirect
from django.views.generic import ListView
from .models import Order , Cart , CartDetail , Coupon
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from settings.models import DeliveryFee
import datetime
from django.http import JsonResponse
from django.template.loader import render_to_string


class OrderList(LoginRequiredMixin, ListView):
    model = Order
    paginate_by = 1
    def get_queryset(self):
        queryset = super().get_queryset()    # return all orders
        queryset = queryset.filter(user=self.request.user) # filter the current user
        return queryset

def chackout_page(request):
    cart = Cart.objects.get(user=request.user , completed=False)
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last()
    
    
    if request.method == 'POST':
        code = request.POST['coupon']
        coupon = Coupon.objects.get(code=code)
        if coupon and coupon.quantity > 0:
            today_date = datetime.datetime.today().date()
            if today_date >= coupon.start_date and today_date <= coupon.end_date:
                code_value = cart.cart_total() / 100*coupon.percentage
                sub_total = cart.cart_total() -  code_value
                total = sub_total + delivery_fee.fee
                
                cart.coupon = coupon 
                cart.total_with_coupon = sub_total
                cart.save()

                html = render_to_string('include/checkout_table.html',{
                'cart_detail':cart_detail , 
                'delivery_fee' : delivery_fee , 
                'sub_total': round(sub_total,2) , 
                'total': round(total,2) , 
                'discount': round(code_value,2) , 
                request:request
                })
                return JsonResponse({'result':html})
    
    
    sub_total = cart.cart_total()
    discount = 0
    total = sub_total + delivery_fee.fee
    
    return render(request,'orders/checkout.html',{
        'cart_detail':cart_detail , 
        'delivery_fee' : delivery_fee , 
        'sub_total': round(sub_total,2) , 
        'total': round(total,2) , 
        'discount': round(discount,2)
        })
    
    
def add_to_cart(request):
    # get data from frontend
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = request.POST['quantity']
    # get cart data
    cart = Cart.objects.get(user=request.user,completed=False)
    cart_detail , created = CartDetail.objects.get_or_create(cart=cart , product=product)
    cart_detail.quantity = quantity
    cart_detail.price = product.price
    cart_detail.total = round(int(quantity) * product.price,2)
    cart_detail.save()
    return redirect(f'/products/{product.slug}')