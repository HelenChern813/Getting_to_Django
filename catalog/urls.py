from django.urls import path
from django.views.generic import TemplateView

from catalog.apps import CatalogConfig
from catalog.views import (EditPublishView, ProductByCategoryListView, ProductCreateView, ProductDeleteView,
                           ProductDetailView, ProductListView, ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", TemplateView.as_view(template_name="contacts.html"), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/new/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path(
        "error_registrations/",
        TemplateView.as_view(template_name="error_registrations.html"),
        name="error_registrations",
    ),
    path("product/unpublish_product/<int:pk>/", EditPublishView.as_view(), name="can_unpublish_product"),
    path("product/category_products/", ProductByCategoryListView.as_view(), name="category_products"),
]
