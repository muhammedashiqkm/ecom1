from django.shortcuts import render
from .models import product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_product=product.objects.order_by('priority')[:4]
    latest_product=product.objects.order_by('-id')[:4]
    context={
        'featured_products':featured_product,
        'latest_products':latest_product
    }
    return render(request,'index.html',context)

def list_products(request):
    page=0
    if request.GET:
        page=request.GET.get('page',1)
    product_list=product.objects.order_by('priority')
    product_Paginator=Paginator(product_list,2)
    product_list=product_Paginator.get_page(page)
    context={'products':product_list}
    return render(request,'products.html',context)

def details_product(request,pk):
    Product=product.objects.get(pk=pk)
    context={'product':Product}
    return render(request,'products_detail.html',context)
