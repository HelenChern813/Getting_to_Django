from blogs.models import Blogs
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BlogsCreateView(CreateView):
    model = Blogs
    fields = ["title", "product", "contents", "preview"]
    template_name = "publication_form.html"
    success_url = reverse_lazy("blogs:publication_list")


class BlogsDetailView(DetailView):
    model = Blogs
    template_name = "publication_detail.html"
    context_object_name = "blogs"

    def get_object(self, queryset=None):

        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogsUpdateView(UpdateView):
    model = Blogs
    fields = ["title", "product", "contents", "preview"]
    template_name = "publication_form.html"
    success_url = reverse_lazy("blogs:publication_list")

    def get_success_url(self):
        return reverse("blogs:publication_detail", args=[self.object.pk])


class BlogsDeleteView(DeleteView):
    model = Blogs
    template_name = "publication_confirm_delete.html"
    success_url = reverse_lazy("blogs:publication_list")


class BlogsListView(ListView):
    model = Blogs
    template_name = "publication_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Blogs.objects.filter(is_active=True)
