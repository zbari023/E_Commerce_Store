# it is the view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProductSerializer , BrandSerializer, BrandDetailSerializer
from .models import Product, Brand



""" @api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()[:10]     # as list of products
    data = ProductSerializer(products, many=True,context={'request':request}).data  # the list to json_data of products
    return Response({'data':data}) """
    
    

""" @api_view(['GET'])
def product_detail_api(request,product_id):
    querset = Product.objects.get(id=product_id)   # to get just a product
    data = ProductSerializer(querset,context={'request':request}).data 
    return Response({'data':data}) """


# class-based view 

class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()[:10]
    serializer_class = ProductSerializer

class ProductDetailAPI(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    

class BrandDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer