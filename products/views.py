from django.shortcuts import render
from django.views import generic
from .models import Product , ProductsImage , Brand , Reviews
# Create your views here.


class ProductList(generic.ListView):
    model = Product


class ProductDetail(generic.DetailView):
    model = Product