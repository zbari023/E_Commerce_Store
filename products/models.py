from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

FLAG_TYPE = (
    ('New', 'New'),
    ('sale', 'sale'),
    ('feature', 'feature'),
)

# Create your models here.
class Product(models.Model):
    name = models.CharField(_('name'),max_length=100)
    description = models.TextField(_('decsription'),max_length=30000)
    sku = models.IntegerField(_('sku'))
    price = models.FloatField(_('price'))
    subtitle = models.TextField(_('subtitle'),max_length=600)
    image = models.ImageField(_('image'),upload_to='products')
    brand = models.ForeignKey('Brand',verbose_name=_('brand'),on_delete=models.CASCADE,related_name='product_brand')
    flag = models.CharField(_('Flag'),max_length=20,choices=FLAG_TYPE)
    tags = TaggableManager()
    slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
    

class ProductsImages(models.Model):
    product = models.ForeignKey(Product,verbose_name=_('product'),related_name='product_images',on_delete=models.CASCADE)
    image = models.ImageField(_('image'),upload_to='product_images')

class Brand(models.Model):
    name = models.CharField(_('name'),max_length=100)
    image = models.ImageField(_('image'),upload_to='brand')
    slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

class Reviews(models.Model):
    user = models.ForeignKey(User,verbose_name=_('user'),related_name='user_review',on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,verbose_name=_('product'),related_name='product_review',on_delete=models.SET_NULL,null=True,blank=True)
    review = models.TextField(_('review'),max_length=500)
    rate = models.IntegerField(_('rate'),validators=[MaxValueValidator(5),MinValueValidator(0)])
    create_date = models.DateTimeField(_('create date'),default=timezone.now)
    
    def __str__(self):
        return f"{self.user} = {self.product}"