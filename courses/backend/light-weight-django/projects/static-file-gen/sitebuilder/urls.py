from django.urls import path
from . import views

urlpatterns = (
    path('<str:slug>/',views.page, name='page'),
    path('', views.page, name='homepage')
)