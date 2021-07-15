from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    # if you set context_object_name you cannot access the data in template using lowercase
    # model name. for this model it is `post`. use-> post.tile, post.body, post.author etc
    # context_object_name = 'anything_you_want'
