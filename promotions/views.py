from django.shortcuts import render
from .models import Product

def promotion_list_view(request):

    products = Product.objects.all()

    print(products)

    context = {
        "products": products
    }
    return render(request, "promotions/pages/home/index.html", context)

def product_detail_view(request, prod_id):
    product = Product.objects.get(pk=prod_id)

    print(product)
    context = {}
    context["product"] = product

    return render(request, "promotions/pages/product/index.html", context)