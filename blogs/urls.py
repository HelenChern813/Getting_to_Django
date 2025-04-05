from django.urls import path
# from blogs.views import
from blogs.apps import BlogsConfig


app_name = BlogsConfig.name

# urlpatterns = [
#     path("", ProductListView.as_view(), name="product_list"),
#     path("contacts/", contacts, name="contacts"),
#     path('product/<int:pk>/', ProductDtailView.as_view(), name='product_detail'),
#     path('product/new/', ProductCreateView.as_view(), name='product_create'),
#     path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
#     path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')
# ]