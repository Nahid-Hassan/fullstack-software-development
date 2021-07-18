from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy
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


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    # show all the field in the form
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body']
    # success_message = ugettext_lazy('Widget was successfully updated')
    # success_url = reverse('post_edit')

    # def has_permission(self, request):
        # return request.user.is_active and request.user.is_staff


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
