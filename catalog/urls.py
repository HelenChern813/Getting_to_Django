from django.urls import path
from django.views.generic import TemplateView

from catalog.views import ProductListView, ProductDtailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", TemplateView.as_view(template_name="contacts.html"), name="contacts"),
    path("product/<int:pk>/", ProductDtailView.as_view(), name="product_detail"),
    path("product/new/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
