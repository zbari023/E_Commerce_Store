# it is the view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product



@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()[:10]     # as list of products
    data = ProductSerializer(products, many=True).data  # the list to json_data of products
    return Response({'data':data})
    
    

@api_view(['GET'])
def product_detail_api(request,product_id):
    querset = Product.objects.get(id=product_id)   # to get just a product
    data = ProductSerializer(querset).data 
    return Response({'data':data})