from django.urls import path
from catalog.views import home, contacts, product_list
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts", contacts, name="contacts"),
    path('product_list/<int:id_product>', product_list, name='product_list')
]
