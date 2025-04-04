from django.shortcuts import render
from catalog.models import Product
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product
    template_name = 'home_page.html'
    context_object_name = 'products'


def contacts(request):
    return render(request, "contacts.html")


class ProductDtailView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'photo', 'category', 'price']
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'photo', 'category', 'price']
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
