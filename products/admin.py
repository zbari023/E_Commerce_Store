from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Product, ProductsImages, Brand, Reviews


class ProductsImagesAdmin(admin.TabularInline):
    model= ProductsImages

class ProductAdmin(SummernoteModelAdmin):
    list_display = ['name', 'price', 'flag','brand']
    list_filter = ['price', 'flag','brand']
    search_fields = ['name', 'subtitle']
    inlines= [ProductsImagesAdmin,]
    summernote_fields = '__all__'

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductsImages)
admin.site.register(Brand)
admin.site.register(Reviews)
