# it is the view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProductSerializer , BrandSerializer, BrandDetailSerializer
from .models import Product, Brand
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import ProductFilter
from .pagination import MyPagenation
from rest_framework.permissions import IsAuthenticated

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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['name','brand', 'flag','price']
    filterset_class = ProductFilter
    ordering_fields = ['price', 'flag']
    # search_fields = ['name', 'subtitle']   # custom filter
    # filter_backends = [filters.OrderingFilter]
    pagination_class = MyPagenation
   # permission_classes = [IsAuthenticated]
    
    

class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   # permission_classes = [IsAuthenticated]


class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    

class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer