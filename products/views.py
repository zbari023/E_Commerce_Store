from django.shortcuts import render
from django.views import generic
from .models import Product , ProductsImages , Brand , Reviews
# Create your views here.


class ProductList(generic.ListView):
    model = Product


class ProductDetail(generic.DetailView):
    model = Product
    
class BrandList(generic.ListView):
    model = Brand
    
class BrandDetail(generic.ListView):
    model = Product
    template_name = 'products/brand_detail.html'
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset