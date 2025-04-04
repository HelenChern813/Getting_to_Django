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


def product_list(request, id_product):

    product = Product.objects.get(id=id_product)

    context = {
        'product': product
    }
    return render(request, 'product_list.html', context)
