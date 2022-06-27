from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post
from django.urls import reverse,reverse_lazy

# Create your views here.
class PostListView(ListView):
    model= Post
    template_name='blog/post_list.html'

class PostCreateView(CreateView):
    model = Post
    field="__all__"
    template_name='blog/form.html'
    sucess_url=reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model= Post
    template_name='post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    field = "__all__"
    success_url=reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    field="__all__"
    success_url=reverse_lazy("blog:all")
    template_name='post_confirm_delete.html'
