from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.filter(available=True)[:6]
    return render(request, 'home.html', {'products': products})

def products_view(request):
    products = Product.objects.filter(available=True)
    return render(request, 'store-templates/products.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store-templates/product_detail.html', {'product': product})
