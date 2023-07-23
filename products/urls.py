from django.urls import path
from .views import ProductList , ProductDetail , BrandList , BrandDetail , post_list_debug

app_name = 'products'

urlpatterns = [
    path('debug',post_list_debug),
    path('',ProductList.as_view(),name = 'product_list'),
    path('<slug:slug>',ProductDetail.as_view(),name = 'product_detail'),
    
    path('brand/',BrandList.as_view(),name = 'brand_list'),
    path('brand/<slug:slug>',BrandDetail.as_view(),name = 'brand_detail'),
    
    
    
]