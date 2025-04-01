from django.shortcuts import render


def home(request):
    return render(request, "home_page.html")


def contacts(request):
    return render(request, "contacts.html")
