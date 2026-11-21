from django.shortcuts import render
from django.http import JsonResponse

from products.models import Product, ProductDetail

# Create your views here.

def health_check(request):
    return JsonResponse({
        "status": "success",
        "message": "Django backend is running"
    })

def products(request):
    products = list(Product.objects.all().values());
    return JsonResponse({
        "status": "success",
        "products": products
    })

def product_details(request, product_id):
    product = list(ProductDetail.objects.filter(product_id=product_id).values())[0]
    return JsonResponse({
        "status": "success",
        "product":  product
    })

