from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


# def HomePageView(request):
#     return HttpResponse("Hello, World")

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class IndexPageView(TemplateView):
    template_name = 'pages/index.html'
