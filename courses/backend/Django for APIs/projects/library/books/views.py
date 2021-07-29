from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
from django.utils import timezone


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    # context_object_name = 'book_list'