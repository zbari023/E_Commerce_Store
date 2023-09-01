# get the Date from the model (DB) and convert its to json
from rest_framework import serializers
from .models import Product , Brand
from django.db.models.aggregates import Avg 

class ProductSerializer(serializers.ModelSerializer):
   # brand = serializers.StringRelatedField()
    review_count = serializers.SerializerMethodField()
    avg_rate = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
        
    def get_review_count(self,object):
        review = object.product_review.all().count()
        return review
    def get_avg_rate(self,object):
        avg = object.product_review.aggregate(avg=Avg('rate'))
        if not avg['avg'] :
            result = 0
        else:
            result = round(avg['avg'],2)
        return result


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
    


class BrandDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(source='product_brand',many=True)
    class Meta:
        model = Brand
        fields = '__all__'
    