from django.shortcuts import render , redirect
from .forms import SignupForm , ActivateUser
from .models import Profile , Phones , Address
from products.models import Product , Reviews, Brand
from orders.models import Order
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            form.save()

    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})


def dashboard(request):
    new_products = Product.objects.filter(flag='New').count()
    sale_products = Product.objects.filter(flag='Sale').count()
    feature_products = Product.objects.filter(flag='Feature').count()
    brands = Brand.objects.all().count() 
    products = Product.objects.all().count()
    reviews = Reviews.objects.all().count()
    user = User.objects.all().count()
    orders = Order.objects.all().count()
    return render(request,'registration/dashboard.html',{
        'new_products':new_products ,
        'sale_products':sale_products ,
        'feature_products':feature_products,
        'user':user,
        'products':products,
        'reviews':reviews,
        'brands':brands,
        'orders':orders
    })