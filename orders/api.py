from rest_framework import generics
from rest_framework.response import Response
from .models import Cart , CartDetail , Order , OrderDetail , Coupon
from .serializers import CartDetailSerializer , CartSerializer , OrderDetailSerializer,OrderSerializer
from django.contrib.auth.models import User
from products.models import Product
from settings.models import DeliveryFee
import datetime







class CartDetailCreateDeleteAPI(generics.GenericAPIView):
    serializer_class = CartSerializer
    def get(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart , created = Cart.objects.get_or_create(user=user,completed=False)
        data = CartSerializer(cart).data
        return Response({'Cart':data, 'Status':200})
        
    def post(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        product = Product.objects.get(id=request.data['product_id'])
        quantity = int(request.data['quantity'])
        cart = Cart.objects.get(user=user ,completed=False)
        cart_data , created = CartDetail.objects.get_or_create(cart=cart,product=product) 
        cart_data.price = product.price
        cart_data.quantity = quantity
        cart_data.total = round(quantity*product.price,2)
        cart_data.save()
        return Response({'status':200,'message':'Product was added seccessfuly'})
    
    def delete(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user ,completed=False)
        product = Product.objects.get(id=request.data['product_id'])
        cart_detail = CartDetail.objects.get(cart=cart , product=product)
        cart_detail.delete()
        return Response({'status':200,'message':'Product was added seccessfuly deleted'})

class OrderListAPI(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
    def list(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        queryset = self.get_queryset().filter(user=user)
        data = OrderSerializer(queryset,many=True).data
        return Response({'orders':data})
        

class OrderDetailAPI(generics.RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()


class CreateOrder(generics.GenericAPIView):
    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user,completed=False)
        cart_detail = CartDetail.objects.filter(cart=cart)
        
        # create order
        new_order = Order.objects.create(user=user)
        for object in cart_detail:
            OrderDetail.objects.create(
                order=new_order,
                product = object.product , 
                price = object.price , 
                quantity = object.quantity , 
                total = object.total
            )
            
        cart.completed = True
        cart.save()
        return Response({'status':200 , 'message':'order was completed successfully '})
    
    
    
class ApplyCoupon(generics.GenericAPIView):
    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user,completed=False)
        coupon  = Coupon.objects.get(code=request.data['coupon_code'])
        delivery_fee = DeliveryFee.objects.last()
        
        if coupon and coupon.quantity > 0:
            today_date = datetime.datetime.today().date()
            if today_date >= coupon.start_date and today_date <= coupon.end_date:
                code_value = cart.cart_total() / 100*coupon.percentage
                sub_total = cart.cart_total() -  code_value
                total = sub_total + delivery_fee.fee
                
                cart.coupon = coupon 
                cart.total_with_coupon = sub_total
                cart.save()
                return Response({'message':'coupon applied successfuly'})
            
            else:
                return Response({'message':'coupon date is not valid '})
            
        else:
            return Response({'message':'coupon not found'})