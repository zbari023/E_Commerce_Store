from django.shortcuts import render
from products.models import Product , Brand , Reviews
# Create your views here.


def home(request):
    brands = Brand.objects.all()
    sale_products = Product.objects.filter(flag='sale')
    feature_products = Product.objects.filter(flag='feature')
    new_products = Product.objects.filter(flag='New')
    reviews = Reviews.objects.all()
    
    return render(request,'settings/home.html',{
        'brands':brands ,
        'sale_products':sale_products,
        'feature_products':feature_products,
        'new_products':new_products,
        'reviews':reviews,
        
    })