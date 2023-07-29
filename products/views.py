from django.shortcuts import render, redirect
from django.views import generic
from .forms import ReviewForm
from .models import Product , ProductsImages , Brand , Reviews
from django.db.models.aggregates import Count , Sum , Avg , Max ,Min
from django.db.models import F , Q , Value , Func
# Create your views here.




def post_list_debug(request):   # QuerySet API reference
    # data = Product.objects.all()
    # data = Product.objects.filter(price__lt=30.6)    # filter return as list 
    # data = Product.objects.all().order_by('name')
    # data = Product.objects.select_related('brand').all() # onetoone and onetomany
    # data = Product.objects.aggregate(Count('id'))
    data = Product.objects.aggregate(Max('price'))
    
    
    
    
    return render(request,'products/debug.html', {'data':data})






class ProductList(generic.ListView):
    model = Product
    paginate_by=100



class ProductDetail(generic.DetailView):
    model = Product
    
    


def add_review(request,slug):
    product = Product.objects.get(slug=slug)
    form = ReviewForm(request.POST)
    if form.is_valid():
        myform = form.save(commit=False)
        myform.user = request.user
        myform.product = product
        myform.save()
        return redirect(f'/products/{product.slug}')



    
class BrandList(generic.ListView):
    model = Brand
    paginate_by=50
    def get_queryset(self):
        object_list = Brand.objects.annotate(posts_count=Count('product_brand'))
        return object_list
    
    
    
    
class BrandDetail(generic.ListView):
    model = Product
    template_name = 'products/brand_detail.html'
    
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(posts_count=Count('product_brand'))[0]
        return context