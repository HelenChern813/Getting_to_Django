from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.models import Category, Product
from catalog.services import products_by_category

from .forms import ProductForm


class EditPublishView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden("У вас нет прав для отмены публикации.")

        product.publish = False
        product.save()

        return redirect("catalog:product_detail", pk=product.pk)


class ProductListView(ListView):
    model = Product
    template_name = "home_page.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = cache.get("products_queryset")
        if not queryset:
            queryset = super().get_queryset()
            cache.set("products_queryset", queryset, 60 * 15)
        return queryset


@method_decorator(cache_page(60 * 15), name="dispatch")
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_details.html"
    context_object_name = "product"
    login_url = reverse_lazy("catalog:error_registrations")


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy("catalog:error_registrations")

    def form_valid(self, form):
        prod = form.save()
        user = self.request.user
        prod.owner = user
        prod.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy("catalog:error_registrations")

    def dispatch(self, request, *args, **kwargs):
        product = super().get_object()

        if product.owner == self.request.user:
            return super().dispatch(request, *args, **kwargs)

        return HttpResponseForbidden("Вы не можете изменить этот продукт.")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy("catalog:error_registrations")

    def dispatch(self, request, *args, **kwargs):
        product = super().get_object()

        if product.owner == self.request.user or request.user.has_perm("catalog.can_delete_product"):
            return super().dispatch(request, *args, **kwargs)

        return HttpResponseForbidden("Вы не можете удалить этот продукт.")


class ProductByCategoryListView(ListView):
    model = Product
    template_name = "product_by_category_list.html"

    def get_queryset(self):
        category_id = self.request.GET.get("category")

        return products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context["categories"] = categories

        return context
