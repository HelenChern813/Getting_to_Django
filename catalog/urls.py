from django.urls import path
from catalog.views import home, contacts, product_details
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path('products/<int:product_id>/', product_details, name='product_details')
]
