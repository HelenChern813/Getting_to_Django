from django.urls import path
from blogs.views import BlogsUpdateView, BlogsCreateView, BlogsDeleteView, BlogsDetailView, BlogsListView
from blogs.apps import BlogsConfig


app_name = BlogsConfig.name

urlpatterns = [
    path("publications/", BlogsListView.as_view(), name="publication_list"),
    path("publication/<int:pk>/", BlogsDetailView.as_view(), name="publication_detail"),
    path("publication/new/", BlogsCreateView.as_view(), name="publication_create"),
    path("publication/<int:pk>/edit/", BlogsUpdateView.as_view(), name="publication_edit"),
    path("publication/<int:pk>/delete/", BlogsDeleteView.as_view(), name="publication_delete"),
]
