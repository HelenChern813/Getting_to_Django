from django.shortcuts import render
from catalog.models import Product
from django.shortcuts import get_object_or_404


def home(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, "home_page.html", context)


def contacts(request):
    return render(request, "contacts.html")


def product_details(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product
    }
    return render(request, 'product_details.html', context)
