from django.shortcuts import render
from catalog.models import Product


def home(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, "home_page.html", context)


def contacts(request):
    return render(request, "contacts.html")


def product_details(request, product_id):

    product = Product.objects.get(id=product_id)

    context = {
        'product': product
    }
    return render(request, 'product_details.html', context)
