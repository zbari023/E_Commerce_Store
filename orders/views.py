from django.shortcuts import render , redirect

# Create your views here.
from django.views.generic import ListView
from .models import Order , Cart ,CartDetail
from products.models import Product



class OrderList(ListView):
    model = Order
    
    def get_queryset(self):
        queryset = super().get_queryset()    # return all orders
        queryset = queryset.filter(user=self.request.user) # filter the current user
        return queryset


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