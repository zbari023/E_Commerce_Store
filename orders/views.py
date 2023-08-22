from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Order



class OrderList(ListView):
    model = Order
