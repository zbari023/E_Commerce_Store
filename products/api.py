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
    
    