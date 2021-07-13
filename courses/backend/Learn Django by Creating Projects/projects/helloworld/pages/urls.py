from django.urls import path
from . import views


urlpatterns = [
    # path('', views.HomePageView, name='home'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('index/', views.IndexPageView.as_view(), name='index'),
]
