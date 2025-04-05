from blogs.models import Blogs
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BlogsCreateView(CreateView):
    model = Blogs
    fields = ['title', 'product', 'contents', 'preview']
    template_name = 'publication_form.html'
    success_url = reverse_lazy('blogs:publication_list')


class BlogsDetailView(DetailView):
    model = Blogs
    template_name = 'publication_detail.html'
    context_object_name = 'blogs'


class BlogsUpdateView(UpdateView):
    model = Blogs
    fields = ['title', 'product', 'contents', 'preview']
    template_name = 'publication_form.html'
    success_url = reverse_lazy('blogs:publication_list')


class BlogsDeleteView(DeleteView):
    model = Blogs
    template_name = 'publication_confirm_delete.html'
    success_url = reverse_lazy('blogs:publication_list')


class BlogsListView(ListView):
    model = Blogs
    template_name = 'publication_list.html'
    context_object_name = 'blogs'
