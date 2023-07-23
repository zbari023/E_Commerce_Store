from django.shortcuts import render
from django.views import generic
from .models import Product , ProductsImages , Brand , Reviews
# Create your views here.




def post_list_debug(request):
    data = Product.objects.all()
    return render(request,'products/debug.html', {'data':data})
class ProductList(generic.ListView):
    model = Product
    paginate_by=100
    


class ProductDetail(generic.DetailView):
    model = Product
    
class BrandList(generic.ListView):
    model = Brand
    paginate_by=50
    
    
class BrandDetail(generic.ListView):
    model = Product
    template_name = 'products/brand_detail.html'
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context